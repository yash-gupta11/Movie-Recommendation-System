import pandas as pd
import numpy as np
import streamlit as st
import pickle 
import requests
def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data= data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path




def recommend(name):
    index = movies[movies['title'] == name].index[0]
    x = sorted(enumerate(similarity[index]),reverse=True,key=lambda x : x[1])
    recommended_movie_name = []
    for i in x[0:5]:
        k = i[0]
        recommended_movie_name.append(movies.iloc[k].title)  
    return recommended_movie_name

st.title("Movie Recommendation System")

movies = pickle.load(open('movies_list.pkl','rb'))
similarity=  pickle.load(open('similarity.pkl','rb'))

name = st.selectbox('Please enter the Movies',movies['title'].values)
if st.button('show recommendation'):
    st.write('Here the top 5 recommended movies enjoy !') 
    recommended_movie_name = recommend(name)
    for i in recommended_movie_name:
        st.write(i)





