import streamlit as st
import pandas as pd

#Titulo al app
st.title("K-Means Clustering con Streamlit")

#subir archivo excel
uploaded_file = st.file_uploader("subir un archivo excel",type=["xlsx"])

if uploaded_file is not None:
    #Leer archivo
    pd=pd.read_excel(uploaded_file)

    st.write("### vista previa de los datos")
    st.write(df.head())

    #seleccionar columnas categoricas
    categoria_columns = df.select_dtypes(include=['object']).columns.tolist()

    if categoria_columns:
        st.wirte("### columnas categoricas identificadas")
        st.write(categoria_columns)

        #convertir columnas categorixa a dumies
        df=pd.get_dumies(df,columns=categoria_columns)
        sr.write("### Datos despues de la conversion  a dumies")
        st.write(df.head())
    else:
        st.write("no se encontraron columnas en los datos")



