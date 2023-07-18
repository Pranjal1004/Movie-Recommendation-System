import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tmdbv3api import TMDb
import json
import requests
tmdb = TMDb()
tmdb.api_key = "4bfa18d4dd4f5d041a3d88cfb6728654"

from tmdbv3api import Movie
tmdb_movie = Movie()
def extract_poster(x):
    result = tmdb_movie.search(x)
    if not result:
        # This "if not result" condition is specifically added for 2020 data as for some movie we don't get result on TMBb
        return np.NaN
    else:
        movie_id = result[0].id
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
        # extracting data in json format
        data_json = response.json()
        # Actually there's a key "id" which basically holds the movie id and another key "imdb_id"
        # which holds the movie's imdb id.

        return "https://image.tmdb.org/t/p/w500/" + data_json["poster_path"]

def create_similarity():
    data = pd.read_csv("movie_data_upto_2022_march.csv")
    cv = CountVectorizer()
    c_matrix = cv.fit_transform(data["combine"])
    similarity = cosine_similarity(c_matrix)
    return data, similarity

def recommend(m):
    data, similarity = create_similarity()
    m = m.lower()
    if m not in data.movie_title.unique():
        return "Sorry, we dont have your movie."
    else:
        data = data
        similarity = similarity
        i = data.movie_title.loc[data.movie_title == m].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x : x[1], reverse=True)
        lst = lst[1:11]
        movies = []
        movie_posters = []
        for i in range(len(lst)):
            movies.append(data.movie_title[lst[i][0]].title())
            movie_posters.append(extract_poster(data.movie_title[lst[i][0]]))
        return movies, movie_posters

def app(movie_name):
    # if st.button("Search"):
        st.header('Here are some suggestions')
        movie_selected = movie_name
        movies, posters = recommend(movie_selected)
        col1, col2, col3, col4= st.columns(4)
        with col1:
            st.text(movies[0],)
            st.image(posters[0],width=150)
        with col2:
            st.text(movies[1])
            st.image(posters[1],width=150)
        with col3:
            st.text(movies[2])
            st.image(posters[2],width=150)
        with col4:
            st.text(movies[3])
            st.image(posters[3],width=150)
        with col1:
            st.text(movies[4])
            st.image(posters[4],width=150)
        with col2:
            st.text(movies[5])
            st.image(posters[5],width=150)
        with col3:
            st.text(movies[6])
            st.image(posters[6],width=150)
        with col4:
            st.text(movies[7])
            st.image(posters[7],width=150)
        with col1:
            st.text(movies[8])
            st.image(posters[8],width=150)
        with col2:
            st.text(movies[9])
            st.image(posters[9],width=150)

