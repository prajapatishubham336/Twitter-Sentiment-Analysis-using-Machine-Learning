# Twitter-Sentiment-Analysis-using-Machine-Learning
This project is a Sentiment Analysis System built using Machine Learning. It analyzes Twitter text data and predicts whether the sentiment is Positive, Negative, or Neutral.

📌 **Project Overview**

This project is a Machine Learning-based Sentiment Analysis System that analyzes Twitter text data and classifies it into Positive, Negative, or Neutral sentiments.

With the rapid growth of social media, users express opinions on various topics online. This system leverages Natural Language Processing (NLP) techniques to process and understand human language, enabling automatic sentiment detection from raw text data.

🎯 **Objective**

* To build an automated system for sentiment classification
* To apply text preprocessing and NLP techniques
* To convert text data into numerical features using TF-IDF
* To train a model that provides accurate predictions
* To enable real-time sentiment prediction from user input

**🚀 Features**

* Efficient text preprocessing and cleaning
* Feature extraction using TF-IDF Vectorizer
* Machine Learning model (LinearSVC) for classification
* High accuracy prediction (~80–90%)
* Real-time prediction using user input
* Model saving and loading using Joblib

🛠️ **Technologies Used**

* **Python** – Core programming language
* **Pandas** – Data manipulation and preprocessing
* **NumPy** – Numerical operations
* **Scikit-learn** – Machine Learning algorithms and evaluation
* **TF-IDF Vectorizer** – Text feature extraction
* **Joblib** – Model persistence

📂 **Dataset**

* Twitter Sentiment Dataset containing tweets and sentiment labels
Columns used:
* text → Tweet content
* sentiment → Label (Positive / Negative / Neutral / Irrelevant)

🔹 **Data Preprocessing Steps:**

* Removed missing/null values
* Removed “Irrelevant” class for better accuracy
* Converted text to lowercase
* Removed:

  * URLs
  * User mentions (@username)
  * Hashtags (#topic)
  * Special characters and numbers

⚙️ **How It Works**

1. **Data Preprocessing**
   Raw text data is cleaned and normalized to remove noise and irrelevant information.

2. **Feature Extraction**
   Text is converted into numerical form using TF-IDF, which captures the importance of words in the dataset.

3. **Model Training**
   A Linear Support Vector Classifier (LinearSVC) is trained on the processed data.
   Class balancing is used to handle uneven data distribution.

4. **Prediction**

* User inputs text
* Text is cleaned and transformed
* Model predicts sentiment label

📊 **Model Performance**

* **Accuracy**: ~80–90%

**Evaluation Metrics**:

* Precision → Measures correctness of positive predictions
* Recall → Measures how well all positives are detected
* F1-score → Balance between precision and recall
* Confusion Matrix → Detailed class-wise performance

💻 **How to Run**

**Step 1: Install dependencies**

pip install pandas numpy scikit-learn joblib

**Step 2: Run the script**

python your_file_name.py

🔮 **Example**

Input:

I love this product!

Output:

Positive

💾 **Model Saving**

The trained model and vectorizer are saved using Joblib for future use:

* sentiment_model.pkl
* tfidf_vectorizer.pkl
* label_map.pkl

This avoids retraining and enables fast deployment.

📈 **Future Improvements**

* Implement Deep Learning models (LSTM, BERT)
* Build a Web App using Streamlit
* Integrate real-time Twitter API for live sentiment analysis
* Improve accuracy with advanced NLP techniques

📚 **References**

* Scikit-learn Documentation: https://scikit-learn.org/stable/
* Pandas Documentation: https://pandas.pydata.org/docs/
* Natural Language Processing with Python (NLTK Book)
* Kaggle Datasets (Twitter Sentiment Analysis)
* Jurafsky & Martin, Speech and Language Processing

⭐ **Conclusion**

This project demonstrates how Machine Learning and NLP techniques can be effectively used to build a real-world sentiment analysis system. It highlights the importance of text preprocessing, feature extraction, and model selection in achieving accurate results.
