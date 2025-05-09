import streamlit as st
import pandas as pd
import plotly.express as px

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de anuncios de venta de coches')

# Botón para histograma
if st.button('Mostrar histograma de odómetro'):
    st.write('Histograma del odómetro')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Mostrar gráfico de dispersión odómetro vs precio'):
    st.write('Gráfico de dispersión: odómetro vs precio')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)