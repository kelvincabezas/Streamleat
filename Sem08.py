import streamlit as st
import pandas as pd

#Titulo al app
st.title("K-Means Clustering con Streamlit")

#subir archivo excel
uploaded_file = st.file_uploader("subir un archivo excel",type=["xlsx"])