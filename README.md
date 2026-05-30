# 🎬 IMDB Movie Review Sentiment Analysis Using Simple RNN

An end-to-end Deep Learning and NLP project that performs sentiment analysis on IMDB movie reviews using a Simple Recurrent Neural Network (RNN) with TensorFlow/Keras and Streamlit deployment.

---

# 🚀 Live Demo

Add your deployed Streamlit app link here:

```bash
https://your-app-link.streamlit.app/
```

---

# 📌 Project Overview

This project predicts whether a movie review is **Positive** or **Negative** using a Deep Learning model trained on the IMDB movie review dataset.

The application includes:

* Natural Language Processing (NLP)
* Word Embedding
* Simple RNN Architecture
* Sentiment Prediction
* Streamlit Web Application
* End-to-End Deployment

---

# 🧠 Problem Statement

Movie reviews contain valuable insights about audience opinions.
The goal of this project is to build a Deep Learning model capable of understanding textual sentiment and classifying reviews into:

* ✅ Positive Sentiment
* ❌ Negative Sentiment

---

# 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Streamlit
* Deep Learning
* NLP
* Simple RNN
* Embedding Layers

---

# 📂 Dataset

Dataset used:

* IMDB Movie Review Dataset
* 50,000 movie reviews
* Binary classification dataset

Dataset Source:

```python
from tensorflow.keras.datasets import imdb
```

---

# 🧩 Project Workflow

## 1️⃣ Data Loading

* Loaded IMDB dataset from TensorFlow/Keras
* Limited vocabulary size to top 10,000 words

---

## 2️⃣ Feature Engineering

* Word Index Mapping
* Integer Encoding
* Sequence Padding

```python
sequence.pad_sequences()
```

---

## 3️⃣ Word Embedding

Implemented Embedding Layers to convert word indices into dense vector representations.

```python
Embedding(max_features, 128)
```

---

## 4️⃣ Simple RNN Model Training

Built and trained a Simple RNN model for sentiment classification.

### Model Architecture

* Embedding Layer
* SimpleRNN Layer
* Dense Output Layer

---

## 5️⃣ Model Evaluation

* Binary Crossentropy Loss
* Adam Optimizer
* Accuracy Metrics
* EarlyStopping Callback

---

## 6️⃣ Sentiment Prediction

Created preprocessing and prediction pipelines for custom user reviews.

Example:

```python
"This movie was fantastic!"
```

Prediction Output:

```bash
Positive 😊
```

---

## 7️⃣ Streamlit Web Application

Developed an interactive web application using Streamlit.

Features:

* User Review Input
* Real-Time Sentiment Prediction
* Confidence Score
* Interactive UI
* Deep Learning Inference

---

# 🧱 Model Architecture

```text
Embedding Layer
        ↓
SimpleRNN Layer
        ↓
Dense Output Layer
```

---

# 📸 Application Screenshots

## Home Page

Add screenshot here:

```bash
screenshots/home.png
```

---

## Prediction Result

Add screenshot here:

```bash
screenshots/result.png
```

---

# 📊 Example Prediction

| Review                             | Prediction  |
| ---------------------------------- | ----------- |
| "This movie was amazing!"          | Positive 😊 |
| "Worst movie I have ever watched." | Negative 😔 |

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/simple-rnn-sentiment-analysis.git
```

---

## Navigate to Project Folder

```bash
cd simple-rnn-sentiment-analysis
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📦 Project Structure

```bash
simple-rnn-sentiment-analysis/
│
├── app.py
├── simple_rnn_model.h5
├── requirements.txt
├── runtime.txt
├── README.md
├── .gitignore
└── notebooks/
```

---

# 🌐 Deployment

This project is deployed using Streamlit Community Cloud.

## Deployment Steps

1. Push code to GitHub
2. Login to Streamlit Cloud
3. Connect GitHub repository
4. Select `app.py`
5. Deploy application

---

# 📈 Future Improvements

* LSTM Implementation
* GRU Networks
* Bidirectional RNN
* Attention Mechanism
* Transformer Models
* BERT Integration
* HuggingFace Transformers
* Docker Deployment
* CI/CD Integration

---

# 🎯 Learning Outcomes

Through this project, I learned:

* NLP preprocessing
* Word embeddings
* Sequence modeling
* Recurrent Neural Networks
* Deep Learning workflows
* TensorFlow/Keras implementation
* Streamlit deployment
* End-to-End ML project development

---

# 👨‍💻 Author

## Waqar Ahmad

AI & Machine Learning Engineer | Full-Stack Developer

* GitHub: https://github.com/wikkikhan
* LinkedIn: https://www.linkedin.com/in/waqar583

---

# ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub.

---

# 📜 License

This project is licensed under the MIT License.