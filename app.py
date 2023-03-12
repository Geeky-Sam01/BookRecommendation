import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.set_page_config(layout="wide")
st.title("Books Recommender System")
st.markdown("""
<style>
.big-font {
    font-size:30px !important;
}
.color-div{
    background-color:white;
}
</style>
""", unsafe_allow_html=True)

add_selectbox = st.sidebar.selectbox(
    "Enter a book name",
    (" ","Harry Potter", "The Davinci Code")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a Method for filtering: ",
        ("Collaborative Filtering", "Content based Filtering","Popularity based Filtering")
    )
st.markdown('<p class="big-font">This is a collaborative filtering system.Know more about the system <a href="#">here</a>.</p>', unsafe_allow_html=True)


movies_list = pickle.load(open('books.pkl','rt'))