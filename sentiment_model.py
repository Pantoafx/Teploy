import pickle
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Load model and vectorizer
model = pickle.load(open('svm_model.pkl', 'rb'))

def preprocess_text(text):
    # Proses teks sesuai langkah preprocessing di notebook
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    text = text.strip()
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    text = stemmer.stem(text)
    return text

def analyze_sentiment(text):
    text = preprocess_text(text)
    text_vector = vectorizer.transform([text])
    sentiment = model.predict(text_vector)
    return sentiment[0]
