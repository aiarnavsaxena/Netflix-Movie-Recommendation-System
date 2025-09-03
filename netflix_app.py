import pickle
import numpy as np
import pandas as pd
import streamlit as st 



# Load the model 
data = pickle.load(open('movie_list.pkl', mode='rb'))
# print(data.head())



# Load Similarity 
similarity  = pickle.load(open('similarity.pkl', mode='rb'))
# print(similarity)

# Final Function to recommend 5 similar movies
def recommend(movie):
    
    movie_index = data[data['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(enumerate(distance), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(data.iloc[i[0]].title)

    return recommended_movies





# Streamlit web-App 

st.title('Movie Recommendation System')
selected_movie = st.selectbox("Select movie using the dropdown box: ", data['title'].values)

btn = st.button("Recommend")

if btn:
    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)