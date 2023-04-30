from lmodel.service import consulta_registros
from lmodel.service import forecast_consulta
import plotly.express as px
import pandas as pd
import streamlit as st
import numpy as np

def plot_grafico_vendas():
    df = consulta_registros()[['venda_total','date','localidade']]
    st.bar_chart(df.tail(50), x='date', y='venda_total')

def quantidade_registros():
    df = consulta_registros()
    return len(df)

def forecast_registros():
    df_previsao = forecast_consulta().tail(200)
    
    st.line_chart(df_previsao,x="date", y="venda_total")
 
def kpi_painel():
    df = consulta_registros()
    kpis = {
        "total_vendas": {
            "value": len(df),
            "delta": df.tail(1).max().to_dict()['localidade']
        },
        "maior_venda": {
            "value": df.max().to_dict()['venda_total'], 
            "delta": f"{df.max().to_dict()['dados_mercado']} {df.max().to_dict()['localidade']}"
        },
        "menor_venda": {
            "value":df.min().to_dict()['venda_total'],
            "delta":f"- {df.min().to_dict()['dados_mercado']} {df.min().to_dict()['localidade']}",
        }
    }
    return kpis
    
    