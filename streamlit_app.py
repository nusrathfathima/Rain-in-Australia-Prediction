import streamlit as st
from streamlit_folium import folium_static

from pycaret.classification import *
import numpy as np
import pandas as pd

@st.cache
def load_data():
    df = pd.read_csv("data/aus_clean_data.csv")
    return df


@st.cache
def load_map_data():
    df = pd.read_csv("data/aus_clean_map_data.csv")
    return df



# Main Frontpage
st.title("Australia Rain Prediction")
image = Image.open("data/plots.jpg")
placeholder = st.image(image)

st.sidebar.header("Dataset")
if st.sidebar.checkbox("Show Data"):
    placeholder.empty()
    st.write("## Dataset")
    st.write(data.head())