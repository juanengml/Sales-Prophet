import requests 
import pandas as pd
#API_URL = "http://sales-prophet-backend:5000/vendas"

API_URL = "http://localhost:5000/vendas"


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
        