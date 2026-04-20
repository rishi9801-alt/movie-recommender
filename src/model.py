
import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess

def create_model():
    # ✅ FIX: ensure folder exists
    os.makedirs('artifacts', exist_ok=True)

    # load processed data
    new_df = preprocess()

    # vectorization
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(new_df['tags']).toarray()

    # similarity matrix
    similarity = cosine_similarity(vectors)

    # save files
    with open('artifacts/movies.pkl', 'wb') as f:
        pickle.dump(new_df, f)

    with open('artifacts/similarity.pkl', 'wb') as f:
        pickle.dump(similarity, f)

    print("Model created and saved successfully!")

def create_model():
    new_df = preprocess()

    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(new_df['tags']).toarray()

    similarity = cosine_similarity(vectors)

    # save files
    pickle.dump(new_df, open('artifacts/movies.pkl', 'wb'))
    pickle.dump(similarity, open('artifacts/similarity.pkl', 'wb'))

    print("Model created and saved!")

if __name__ == "__main__":
    create_model()