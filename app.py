
import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image


# Function to fetch movie poster using TMDB API
def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=9ea2c4901ac130ce721a0bc9dabd126f&language=en-US")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# Movie recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies, recommended_movies_poster


# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Page title and description
st.title("🎬 Movie Recommender System")
st.markdown("<h2 style='text-align: center; color: #4A90E2;'>Find your next favorite movie</h2>",
            unsafe_allow_html=True)

# Select movie from dropdown
selected_movie_name = st.selectbox(
    'Choose a movie to get recommendations:',
    movies['title'].values
)

# Recommend button
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Display recommended movies in a styled layout
    st.markdown("<h3 style='text-align: center; color: #4A90E2;'>Recommended Movies</h3>", unsafe_allow_html=True)

    # Use columns for displaying each recommended movie
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]

    for col, name, poster in zip(columns, names, posters):
        with col:
            st.image(poster, use_container_width=True)  # Updated parameter
            st.markdown(f"<h4 style='text-align: center; color: #FF6347;'>{name}</h4>", unsafe_allow_html=True)


st.write("Built with 😍 by Arpit")