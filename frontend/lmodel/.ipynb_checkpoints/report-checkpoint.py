from lmodel.service import consulta_registros
import plotly.express as px
import pandas as pd
import streamlit as st
import numpy as np

def plot_grafico_vendas():
    df = consulta_registros()[['venda_total','date','localidade']]
    st.area_chart(df.tail(50), x='date', y='venda_total')

def quantidade_registros():
    df = consulta_registros()
    return len(df)

def forecast_registros():
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['data', 'forecast', 'status'])
    st.area_chart(chart_data)
 