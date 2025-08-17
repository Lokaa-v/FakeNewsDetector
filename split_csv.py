import os
import pandas as pd

def split_csv_by_size(file_path, max_mb=10):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    print(f"Splitting {file_path} ...")

    df = pd.read_csv(file_path)

    row_size = df.memory_usage(deep=True).sum() / len(df)
    max_bytes = max_mb * 1024 * 1024
    rows_per_chunk = int(max_bytes / row_size)

    print(f"Each row ≈ {int(row_size)} bytes → {rows_per_chunk} rows per file")

    for i in range(0, len(df), rows_per_chunk):
        chunk = df.iloc[i:i+rows_per_chunk]
        out_file = f"{base_name}_part_{i//rows_per_chunk+1}.csv"
        chunk.to_csv(out_file, index=False)
        size_mb = os.path.getsize(out_file) / (1024*1024)
        print(f"✅ Created {out_file} ({size_mb:.2f} MB)")

# Automatically split all CSVs in folder
for file in os.listdir("."):
    if file.endswith(".csv"):
        if os.path.getsize(file) > 25 * 1024 * 1024:  # only split if >25MB
            split_csv_by_size(file, max_mb=10)

print("🎉 Done! All big files have been split under 25MB.")
