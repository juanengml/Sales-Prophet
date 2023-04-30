import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime 
from lmodel.service import cadastro_post, visualizar_get, detelar_request, update_put
import numpy as np
#API_URL = "http://sales-prophet-backend:5000/vendas"

API_URL = "http://localhost:5000/vendas"

def cadastro_vendas():
    
    data = st.date_input("Selecione uma data")
    data_formatada = datetime.strftime(data, "%Y-%m-%d")

    venda_total = st.number_input("Valor Total")
    dados_mercado = st.text_input("Nome da Loja")
    localidade = st.selectbox("Localidade", ["SP", "PR", "MG","RO"])
    
    if st.button("Cadastrar"):
        response = cadastro_post(data_formatada, venda_total, dados_mercado, localidade)

        if response.status_code == 200:
            st.success("Vendas cadastradas com sucesso!")
        else:
            st.error("Erro ao cadastrar vendas.")
            st.error(response.text)
 

def visualiza_vendas():
    # Tabela para visualizar as vendas cadastradas
    result = visualizar_get()
    if isinstance(result, pd.DataFrame):
        st.table(result)
    else:
        st.error(result)

def deleta_vendas():
    # Formulário para deletar vendas
    venda_ids = st.text_input("IDs das vendas (separados por vírgula)")
    if st.button("Deletar"):
        response = detelar_request(venda_ids)
        if response.status_code == 200:
            st.success("Vendas deletadas com sucesso!")
        else:
            st.error("Erro ao deletar vendas.")
            st.error(response.text)
    
def update_vendas():
    # Formulário para atualizar vendas
    st.write("Digite os novos valores para as vendas. O ID é obrigatório.")
    id = st.text_input("ID")
    data = st.text_input("Data (YYYY-MM-DD)")
    venda_total = st.number_input("Valor Total")
    dados_mercado = st.text_input("Nome da Loja")
    localidade = st.selectbox("Localidade", ["SP", "PR", "MG"])
    if st.button("Atualizar"):
        response = update_put(id, data, venda_total, dados_mercado, localidade)
        if response.status_code == 200:
            st.success("Vendas atualizadas com sucesso!")
        else:
            st.error("Erro ao atualizar vendas.")
            st.error(response.text)
