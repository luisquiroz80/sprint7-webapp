import streamlit as st
import pandas as pd
import plotly.express as px

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de anuncios de venta de coches')

# Casilla para histograma
if st.checkbox('Mostrar histograma de odómetro'):
    st.write('Histograma del odómetro')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla para gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión odómetro vs precio'):
    st.write('Gráfico de dispersión: odómetro vs precio')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)