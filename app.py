import streamlit as st
import pickle
import pandas as pd

st.title("Cine Matchc")
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(selected_movie):
   movie_idx = movies[movies['title'] == selected_movie].index[0]
   distances = similarity[movie_idx]
   movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
   recomended_movies = []
   for i in movie_list:
      recomended_movies.append(movies.iloc[i[0]].title)
   return recomended_movies




import streamlit as st

selected_movie = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values,
)


if st.button("Recommend Movie"):
    recommendation = recommend(selected_movie)
    for movi in recommendation:
       st.write(movi)