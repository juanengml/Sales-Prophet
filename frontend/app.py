import requests
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
from lmodel.model import update_vendas
from lmodel.model import deleta_vendas
from lmodel.model import cadastro_vendas
from lmodel.model import visualiza_vendas
from lmodel.report import plot_grafico_vendas
from lmodel.report import quantidade_registros
from lmodel.report import forecast_registros


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
        st.info(' ')
        st.metric(label="Total", value="6", delta="+1 CARNE")
    
    with dados_B:
        st.subheader("Maior Venda")
        st.success(' ')
        st.metric(label="Alta", value="500", delta="+1 ABC")


    with dados_C:
        st.subheader("Menor Venda")
        st.warning(' ')
        st.metric(label="Baixa", value="250", delta="-1 ARROZ")



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
        graficos_menu = st.selectbox('Relatorio', ["Histórico","Previsão"])
        if graficos_menu == "Histórico":
            plot_grafico_vendas()

        if graficos_menu == "Previsão":
            forecast_registros()

            

    with st.expander("Historico de Vendas",expanded=True):
        visualiza_vendas()    

    
    
    
            

if __name__ == "__main__":
    main()

