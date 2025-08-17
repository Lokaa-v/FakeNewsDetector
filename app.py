from flask import Flask, render_template, request
import joblib
from newspaper import Article
from werkzeug.utils import secure_filename
import os



app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news']
        
        # Predict label and confidence
        prediction = model.predict([news_text])[0]
        prediction_proba = model.predict_proba([news_text])[0]
        confidence = round(max(prediction_proba) * 100, 2)

        result = "Real News 🟢" if prediction == 1 else "Fake News 🔴"
        return render_template('index.html', prediction=result, confidence=confidence)
    
@app.route('/predict_url', methods=['POST'])
def predict_url():
    if request.method == 'POST':
        url = request.form['url']

        try:
            article = Article(url)
            article.download()
            article.parse()
            news_text = article.text

            prediction = model.predict([news_text])[0]
            prediction_proba = model.predict_proba([news_text])[0]
            confidence = round(max(prediction_proba) * 100, 2)

            result = "Real News 🟢" if prediction == 1 else "Fake News 🔴"
            return render_template('index.html', prediction=result, confidence=confidence)
        except Exception as e:
            return render_template('index.html', prediction="❌ Error: Unable to extract article from URL.", confidence=None)

@app.route('/predict_file', methods=['POST'])
def predict_file():
    if 'newsfile' not in request.files:
        return render_template('index.html', prediction="❌ No file uploaded", confidence=None)

    file = request.files['newsfile']

    if file.filename == '':
        return render_template('index.html', prediction="❌ No file selected", confidence=None)

    if file and file.filename.endswith('.txt'):
        filename = secure_filename(file.filename)
        filepath = os.path.join("uploads", filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(filepath)

        with open(filepath, 'r', encoding='utf-8') as f:
            news_text = f.read()

        prediction = model.predict([news_text])[0]
        prediction_proba = model.predict_proba([news_text])[0]
        confidence = round(max(prediction_proba) * 100, 2)
        result = "Real News 🟢" if prediction == 1 else "Fake News 🔴"

        os.remove(filepath)  # Clean up uploaded file
        return render_template('index.html', prediction=result, confidence=confidence)
    else:
        return render_template('index.html', prediction="❌ Only .txt files are supported.", confidence=None)


if __name__ == '__main__':
    app.run(debug=True)
