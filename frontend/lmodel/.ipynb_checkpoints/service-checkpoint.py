import requests 
import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import datetime 

API_URL = "http://sales-prophet-backend:5000/vendas"

API_FORECAST = 'http://sales-prophet-backend:5000/forecast'

def cadastro_post(data_formatada, venda_total, dados_mercado, localidade):
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
    return  response

def consulta_registros():
    response = requests.get(API_URL).json()
    df = pd.DataFrame(response["vendas"])
    return df

def visualizar_get():
    response = requests.get(API_URL)
    if response.status_code == 200:
        vendas = response.json()["vendas"]
        if len(vendas) > 0:
            df = pd.DataFrame(vendas).tail(10)
            return df
        else:
            return response.text
    else:
        return response.text

def detelar_request(venda_ids):
    venda_ids = venda_ids.split(",")
    data_dict = [{"id": int(id.strip())} for id in venda_ids]
    response = requests.delete(API_URL, json=data_dict)
    return response
    

def update_put(id, data, venda_total, dados_mercado, localidade):
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
    return response

def forecast_consulta():    
    df = consulta_registros()
    data_inicial = df.max().date
    data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").date()
    data_final = data_inicial + relativedelta(months=3)
    data_final = data_final.strftime('%Y-%m-%d')
    data_inicial = data_inicial.strftime('%Y-%m-%d')

    data = {'data_inicial': data_inicial, 'data_final': data_final}
    # Faça a requisição POST com o objeto JSON no corpo da requisição
    response = requests.post(API_FORECAST, json=data)
    previsao = response.json()
    df_previsao = pd.DataFrame.from_dict(previsao['previsao'])
    media = df_previsao['venda_total'][df_previsao.venda_total > 0].mean()
    df_previsao.loc[df_previsao.venda_total < 0, 'venda_total'] = media
    return df_previsao
