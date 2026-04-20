import pickle

movies = pickle.load(open('artifacts/movies.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

def recommend(movie):
    movie = movie.lower()

    if movie not in movies['title'].str.lower().values:
        return ["Movie not found"]

    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)

    return recommended