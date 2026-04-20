import streamlit as st
import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

<<<<<<< HEAD
if not os.path.exists("artifacts/similarity.pkl"):
    os.system("python src/model.py")

=======
>>>>>>> 8e7a4f7f8d27fd09975f26a21c6dece6d436772d
movies = pickle.load(open(os.path.join(BASE_DIR, '..', 'artifacts', 'movies.pkl'), 'rb'))
similarity = pickle.load(open(os.path.join(BASE_DIR, '..', 'artifacts', 'similarity.pkl'), 'rb'))

# placeholder poster (stable)
def fetch_poster(movie_title):
    return "https://placehold.co/300x450/png?text=Movie"

# recommendation function
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
            st.image(posters[i], width='stretch')
            st.markdown(
                f"<div style='text-align: center; font-weight: bold;'>{names[i]}</div>",
                unsafe_allow_html=True
            )