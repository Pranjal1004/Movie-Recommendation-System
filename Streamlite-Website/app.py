import streamlit as st
import numpy as np
import pandas as pd

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
        return None
    else:
        movie_id = result[0].id
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
        # extracting data in json format
        data_json = response.json()
        # Actually there's a key "id" which basically holds the movie id and another key "imdb_id"
        # which holds the movie's imdb id.
        if not (data_json["poster_path"] is None):
            return "https://image.tmdb.org/t/p/w500/" + data_json["poster_path"]
        else:
            return None

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
        lst2 = lst[1:11]
        movies = []
        movie_posters = []
        for i in range(len(lst2)):
            if not  (extract_poster(data.movie_title[lst2[i][0]]) is None) :
             movie_posters.append(extract_poster(data.movie_title[lst2[i][0]]))
             movies.append(data.movie_title[lst2[i][0]].title())
            else:
                movie_posters.append("Poster Unavailable!")
                movies.append(movies[0])
            
        return movies, movie_posters

movie_data = pd.read_csv("movie_data_upto_2022_march.csv")
st.title("Movie Recommendation system")
movie_selected = st.selectbox("Search a movie", movie_data.movie_title.values)
if st.button("Search"):
        st.header('Here are some suggestions')
        movies, posters = recommend(movie_selected)
        col1, col2, col3= st.columns(spec=3, gap="small")
        with col1:
            st.text(movies[0])
            if not("https" in posters[0]):
                st.text(posters[0])
            else:
                st.image(posters[0],width=200)
        with col2:
            st.text(movies[1])
            if not("https" in posters[1]):
                st.text(posters[1])
            else:
                st.image(posters[1],width=200)
        with col3:
            st.text(movies[2])
            if not("https" in posters[2]):
                st.text(posters[2])
            else:
                st.image(posters[2],width=200)
        with col1:
            st.text(movies[3])
            if not("https" in posters[3]):
                st.text(posters[3])
            else:
                st.image(posters[3],width=200)
        with col2:
            st.text(movies[4])
            if not("https" in posters[4]):
                st.text(posters[4])
            else:
                st.image(posters[4],width=200)
        with col3:
            st.text(movies[5])
            if not("https" in posters[5]):
                st.text(posters[5])
            else:
                st.image(posters[5],width=200)
        with col1:
            st.text(movies[6])
            if not("https" in posters[6]):
                st.text(posters[6])
            else:
                st.image(posters[6],width=200)
        with col2:
            st.text(movies[7])
            if not("https" in posters[7]):
                st.text(posters[7])
            else:
                st.image(posters[7],width=200)
        with col3:
            st.text(movies[8])
            if not("https" in posters[8]):
                st.text(posters[8])
            else:
                st.image(posters[8],width=200)
        with col1:
            st.text(movies[9])
            if not("https" in posters[9]):
                st.text(posters[9])
            else:
                st.image(posters[9],width=200)

