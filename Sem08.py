import streamlit as st
import pandas as pd

#Titulo al app
st.title("K-Means Clustering con Streamlit")

#subir archivo excel
uploaded_file = st.file_uploader("subir un archivo excel",type=["xlsx"])

if uploaded_file isnotNone:
    #Leer archivo
    pd=pd.read_excel(uploaded_file)

    st.write("### vista previa de los datos")
    st.write(df.head())
    
