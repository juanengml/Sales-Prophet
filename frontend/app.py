import streamlit as st
import requests
import pandas as pd
from datetime import datetime 
import plotly.express as px
from lmodel.model import plot_grafico_vendas
from lmodel.model import cadastro_vendas, visualiza_vendas, forecast_registros
from lmodel.model import update_vendas, deleta_vendas, quantidade_registros
import numpy as np


#API_URL = "http://sales-prophet-backend:5000/vendas"
API_URL = "http://localhost:5000/vendas"
st.set_page_config(
    page_title = 'Sales Prohphet',
    page_icon = '🛍️',
    layout = 'wide'
)

    
def main():
    #st.title("Sales Prophet")
    st.markdown("<h1 style='text-align: center; color: white;'>💳  &nbsp Sales Prophet  &nbsp 🛍️</h1>", unsafe_allow_html=True)

    st.divider()  # 👈 Draws a horizontal rule
    st.markdown("<h2 style='text-align: center; color: white;'> Gerenciamento e previsão de vendas </h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'> Tornando seu negócio mais eficiente e lucrativo. </h3>", unsafe_allow_html=True)

    st.divider()  # 👈 Draws a horizontal rule
    dados_A, dados_B, dados_C = st.columns(3)
    total, crud = st.columns(2)    
    
    with dados_A:
        st.subheader("Total de Vendas")
        st.info('6')

    
    with dados_B:
        st.subheader("Maior Venda")
        st.success('500')

    with dados_C:
        st.subheader("Menor Venda")
        st.warning('250')


    st.divider()  # 👈 Draws a horizontal rule

    with total:
        
        crud_menu = st.selectbox('Menu', ['Cadastrar', 'Atualizar','Deletar'])
        if crud_menu == 'Cadastrar':
            cadastro_vendas()
        if crud_menu == "Atualizar":
            update_vendas()
        if crud_menu == "Deletar":
            deleta_vendas()

    with crud:
        graficos_menu = st.selectbox('Relatorio', ["historico","previsão"])
        if graficos_menu == "historico":
            chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["a", "b", "c"])

            st.bar_chart(chart_data)
        if graficos_menu == "previsão":
            forecast_registros()

            

    with st.expander("Historico de Vendas",expanded=True):
        visualiza_vendas()    

    
    
    
            

if __name__ == "__main__":
    main()

