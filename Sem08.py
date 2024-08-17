import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px

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

#Normalizar los datos

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

#Seleccion del numero de cluster
st.write("### selecciona el numero de  clusters")
num_clusters = st.slider("Numero de cluster ",min_value = 2 , max_value = 10 ,value =3)

#aplicando el k-means
KMeans=KMeans(num_clusters= num_clusters , random_state= 42)
clusters = KMeans.fit_predict(df_scaled)

# anadir cluster al DF original
df['cluster'] = clusters

st.write("### Datos con el cluster asignado")
st.write(df.head())

#Visualizacion de los cluster (solo si tiene dos dimensiones)
if df_scaled.shape[1]>= 2 :
    df_plot = pd.DataFrame(df_scaled, columns=[f'PC{i+1}'for i in range(df_scaled.shape[1])])
    df_plot['cluster'] = clusters
    fig = px.scatter(df_plot , x = 'PC1' , y='PC2' , color = 'Cluster',title = 'Visualizacion de cluster')
    st.plotly_chart(fig)
else:
    st.write("los datos deben tener al menos 2 columnas numericas para visualziar los cluster")



