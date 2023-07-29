import pandas as pd
import streamlit as st
import pickle
import pandas
movies_dict = pickle.load(open('movie_dict.pkl' , 'rb'))
similarity = pickle.load(open('similarity.pkl' , 'rb'))

movies = pd.DataFrame(movies_dict)

st.title('Movie-Recommender-System')

selected_movie_name = st.selectbox("How wouly you like to be connected" ,
                       movies['title'].values)

def recommend(movie_name, movies):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]
#     return movie_list
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies;

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name , movies )
    for i in recommendations:

        st.write(i)   