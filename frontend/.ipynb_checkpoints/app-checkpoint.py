import streamlit as st
import requests
import pandas as pd
from datetime import datetime 
import plotly.express as px

API_URL = "http://sales-prophet-backend:5000/vendas"


def cadastro_vendas():
    
    # Formulário para cadastrar vendas
    data = st.date_input("Selecione uma data")
    data_formatada = datetime.strftime(data, "%Y-%m-%d")

    venda_total = st.number_input("Valor Total")
    dados_mercado = st.text_input("Dados de Mercado")
    localidade = st.selectbox("Localidade", ["SP", "PR", "MG"])
    
    if st.button("Cadastrar"):
        data_dict = {
            "data": [
                {
                    "date": data_formatada,
                    "venda_total": venda_total,
                    "dados_mercado": dados_mercado,
                    "localidade": localidade
                }
            ]
        }
        response = requests.post(API_URL, json=data_dict)
        if response.status_code == 200:
            st.success("Vendas cadastradas com sucesso!")
        else:
            st.error("Erro ao cadastrar vendas.")
            st.error(response.text)

def plot_grafico_vendas(limite):
    response = requests.get(API_URL).json()
    df = pd.DataFrame(response["vendas"])
    fig = px.line(df.head(int(limite)), x='date', y='venda_total', title='Vendas Totais')
    img = fig.to_image(format="png")
    st.image(img, use_column_width=True)

    #st.plotly_chart(fig)

def quantidade_registros():
    response = requests.get(API_URL).json()
    df = pd.DataFrame(response["vendas"])
    return len(df)

def visualiza_vendas():
    # Tabela para visualizar as vendas cadastradas
    response = requests.get(API_URL)
    if response.status_code == 200:
        vendas = response.json()["vendas"]
        if len(vendas) > 0:
            df = pd.DataFrame(vendas)
            st.table(df.head(10))
        else:
            st.info("Nenhuma venda cadastrada.")
    else:
        st.error("Erro ao buscar vendas cadastradas.")
        st.error(response.text)

def deleta_vendas():
    # Formulário para deletar vendas
    venda_ids = st.text_input("IDs das vendas (separados por vírgula)")
    if st.button("Deletar"):
        venda_ids = venda_ids.split(",")
        data_dict = [{"id": int(id.strip())} for id in venda_ids]
        response = requests.delete(API_URL, json=data_dict)
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
    dados_mercado = st.text_input("Dados de Mercado")
    localidade = st.selectbox("Localidade", ["SP", "PR", "MG"])
    if st.button("Atualizar"):
        data_dict = [
            {
                "id": id,
                "date": data,
                "venda_total": venda_total,
                "dados_mercado": dados_mercado,
                "localidade": localidade
            }
        ]
        response = requests.put(API_URL, json=data_dict)
        if response.status_code == 200:
            st.success("Vendas atualizadas com sucesso!")
        else:
            st.error("Erro ao atualizar vendas.")
            st.error(response.text)
    
def main():
    st.title("Sales Prophet")
    st.expander('Test', expanded=False)
    st.header("Gerenciamento e previsão de vendas: tornando seu negócio mais eficiente e lucrativo.")
    
    total, crud = st.columns(2)
    with total:
        st.header("Vendas", anchor=False)
        st.warning(f"Total de Vendas **{quantidade_registros()}**")
        limite = st.number_input("limite")
        plot_grafico_vendas(limite)
        
        
    with crud:
        crud = st.selectbox('Menu', ['Cadastrar', 'Atualizar','Deletar'])
        if crud == 'Cadastrar':
            cadastro_vendas()
        if crud == "Atualizar":
            update_vendas()
        if crud == "Deletar":
            deleta_vendas()
    
    visualiza_vendas()    

    
    
    
            

if __name__ == "__main__":
    main()

