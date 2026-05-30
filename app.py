import streamlit as st
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="IMDB Movie Review Sentiment Analysis",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Load model
model = load_model('simple_rnn_model.h5')

# Load the IMDB dataset word index
word_index = imdb.get_word_index()

# Sidebar
st.sidebar.title("About Project")
st.sidebar.write("""
                 This project uses:
                 - TensorFlow
                 - Keras
                 - Simple RNN
                 - Embedding Layer
                 - IMDB Dataset
                 - Streamlit
                 """)

st.sidebar.write("Model Accuracy: 85%+")

# Title
st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review to predict its sentiment (positive or negative).")

# Function to preprocess user input review text
def preprocess_review(review_text):
    # Convert the review text to lowercase and split it into words
    words = review_text.lower().split()
    # Convert words to indices using the IMDB word index
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    # Pad or truncate the sequence to a fixed length
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

# User input for review text
user_review = st.text_area(
    "Enter Movie Review",
    height=150,
    placeholder="Type your movie review here..."
)

# Example reviews for testing
with st.expander("Example Reviews"):
    st.write("1. This movie was fantastic! I loved it.")
    st.write("2. The plot was terrible and the acting was worse.")
    st.write("3. An average movie with some good moments.")
    st.write("4. Absolutely brilliant! A must-watch.")
    st.write("5. I didn't like this movie at all.")

# Predict button
if st.button("Predict Sentiment"):
    if user_review.strip() == "":
        st.warning("Please enter a movie review before clicking the button.")
    else:
        with st.spinner("Analyzing Review..."):
            preprocessed_review = preprocess_review(user_review)
            prediction = model.predict(preprocessed_review)
            confidence = float(prediction[0][0])
            sentiment = "Positive Review" if confidence >= 0.5 else "Negative Review"

            st.subheader("Prediction Result")
            if confidence >= 0.5:
                st.success(f"Sentiment: {sentiment} (Confidence: {confidence:.4f})")
            else:
                st.error(f"Sentiment: {sentiment} (Confidence: {confidence:.4f})")

            st.progress(confidence)

            st.write(f"Confidence Score: {confidence:.4f}")

            st.write("Note: The confidence score indicates how strongly the model predicts the sentiment. A score closer to 1 means a stronger positive sentiment, while a score closer to 0 indicates a stronger negative sentiment.")