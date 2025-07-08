import streamlit as st
import pandas as pd
import plotly.express as px

# leer el archivo csv
car_data = pd.read_csv('vehicles_us.csv')

# encabezado
st.header('Análisis interactivo de anuncios de autos en EE.UU.')

# boton para histograma
hist_button = st.button('Construir histograma de kilometraje')

if hist_button:
    st.write('Creando histograma del kilometraje')
    fig = px.histogram(car_data, x='odometer', nbins=50,
                       title='Distribución del kilometraje')
    st.plotly_chart(fig, use_container_width=True)

# Boton para grafico de dispersion
scatter_button = st.button('Construir gráfico de dispersión Precio vs Año')

if scatter_button:
    st.write('Creando gráfico de dispersión Precio vs Año del modelo')
    fig2 = px.scatter(car_data, x='model_year', y='price', color='fuel',
                      title='Precio vs Año por tipo de combustible')
    st.plotly_chart(fig2, use_container_width=True)
