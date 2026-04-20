# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Machine Learning and Streamlit that suggests similar movies based on user selection.

---

## 🚀 Features

- Recommend movies based on similarity
- Uses content-based filtering (NLP)
- Clean and interactive UI using Streamlit
- Fast recommendations using precomputed similarity matrix

---

## 🧠 How It Works

- Extracts important features like:
  - Genre
  - Keywords
  - Cast
  - Overview
- Combines them into a single text (tags)
- Converts text into vectors using **CountVectorizer**
- Calculates similarity using **Cosine Similarity**
- Recommends top 5 similar movies

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit

---

## 📂 Project Structure
movie-recommender/
│
├── app/
├── src/
├── artifacts/
├── data/
├── requirements.txt
└── README.md


---

## 🚀 Live Demo

👉 [Click here to try the app](https://movie-recommender-33hsun7xreyuzyt7o3qqgy.streamlit.app)

---

## 📸 Project Screenshot

![Movie Recommender](assets/app.png)

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/rishi9801-alt/movie-recommender.git
cd movie-recommender
