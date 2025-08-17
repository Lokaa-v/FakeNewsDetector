# 📰 Fake News Detector  

An **AI-powered Fake News Detection System** designed to classify news articles as *real* or *fake*. This project helps combat misinformation by analyzing text, URLs, or uploaded documents and providing a **confidence score** for predictions.  

---

## 🚀 Features  

- ✅ **Text-based Detection** – Paste an article and check authenticity  
- ✅ **URL-based News Checker** – Enter a news URL for analysis  
- ✅ **File Upload Support** – Upload text files (.txt) for bulk analysis  
- ✅ **Confidence Score** – Get probability-based results for higher trust  
- ✅ **User-Friendly Interface** – Simple, clean, and fast UI for end users  

---

## 🛠️ Tech Stack  

- **Frontend:** HTML, CSS, JavaScript (or React if used)  
- **Backend:** Python (Flask / Django)  
- **Machine Learning:** Scikit-learn, Pandas, NumPy  
- **Model:** TF-IDF Vectorization + Classification (Logistic Regression / Naive Bayes / SVM)  
- **Database (Optional):** SQLite / MongoDB for logging results  

---

## 📸 Screenshots  

> Add screenshots of your project here 👇  

![Homepage](assets/homepage.png)  
*Fake News Detector – Homepage*  

![Prediction Result](assets/result.png)  
*Prediction Result with Confidence Score*  

---

## 📂 Project Structure  

```bash
Fake-News-Detector/
│── data/                 # Dataset files (train/test CSVs)
│── models/               # Saved ML models
│── static/               # CSS, JS, Images
│── templates/            # HTML files
│── app.py                # Main Flask/Django app
│── requirements.txt      # Dependencies
│── README.md             # Project documentation

