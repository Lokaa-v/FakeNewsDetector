import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib



# Load datasets
fake_df = pd.read_csv("Fake.csv")
real_df = pd.read_csv("True.csv")

# Add labels: 0 = Fake, 1 = Real
fake_df["label"] = 0
real_df["label"] = 1

# Combine and shuffle
df = pd.concat([fake_df, real_df], ignore_index=True)
df["text"] = df["title"] + " " + df["text"]  # Merge title + body
df = df[["text", "label"]].sample(frac=1).reset_index(drop=True)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.25)

# Model pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english", max_df=0.7)),
    ("nb", MultinomialNB())
])



# Train and save
model.fit(X_train, y_train)
joblib.dump(model, "model.pkl")
print("✅ Real-world model saved as model.pkl")
