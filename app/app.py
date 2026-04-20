import streamlit as st
import os
import pickle
import pandas as pd

# ---------------- BASE PATH (FIXED FOR DEPLOYMENT) ---------------- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_DIR = os.path.join(BASE_DIR, "..", "artifacts")

movies_path = os.path.join(ARTIFACTS_DIR, "movies.pkl")
similarity_path = os.path.join(ARTIFACTS_DIR, "similarity.pkl")

# ---------------- SAFETY CHECK ---------------- #
if not os.path.exists(movies_path) or not os.path.exists(similarity_path):
    st.error("Model files not found! Please ensure artifacts/ is uploaded in GitHub.")
    st.stop()

# ---------------- LOAD DATA ---------------- #
movies = pickle.load(open(movies_path, "rb"))
similarity = pickle.load(open(similarity_path, "rb"))

# ---------------- POSTER FUNCTION ---------------- #
def fetch_poster(movie_title):
    return "https://placehold.co/300x450/png?text=Movie"

# ---------------- RECOMMENDATION ENGINE ---------------- #
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movies_list:
        title = movies.iloc[i[0]].title
        names.append(title)
        posters.append(fetch_poster(title))

    return names, posters

# ---------------- UI ---------------- #
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommendation System")
st.write("Get similar movie suggestions instantly")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_container_width=True)
            st.markdown(
                f"<div style='text-align: center; font-weight: bold;'>{names[i]}</div>",
                unsafe_allow_html=True
            )