import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header("Cuadro de Mandos - Anuncios de Venta de Coches")

# Crear casillas de verificación
show_histogram = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

# Si la casilla de histograma está marcada
if show_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Si la casilla de dispersión está marcada
if show_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
