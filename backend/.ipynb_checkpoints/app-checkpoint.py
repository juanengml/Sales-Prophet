from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
import dataset
from prophet import Prophet

app = Flask(__name__)
api = Api(app)

class Vendas(Resource):
    def __init__(self):
        # Cria uma conexão com o banco de dados
        self.db = dataset.connect('sqlite:///vendas-prod.db')
        # Obtém a tabela 'vendas'
        self.table = self.db['vendas']

    def post(self):
        # Recebe dados dos meses passados e cadastra as vendas no banco
        data = request.get_json()
        self.table.insert_many(data['data'])
        return {'message': 'Vendas cadastradas com sucesso.'}

    def get(self):
        # Lista todas as vendas cadastradas no banco
        vendas = [dict(v) for v in self.table.all()]
        return {'vendas': vendas}

    def delete(self):
        # Recebe ids das vendas e deleta do banco
        data = request.get_json()
        for venda in data:
            self.table.delete(id=venda['id'])
        return {'message': 'Vendas deletadas com sucesso.'}

    def put(self):
        # Recebe ids das vendas e atualiza as vendas no banco
        data = request.get_json()
        for venda in data:
            self.table.update(venda, ['id'])
        return {'message': 'Vendas atualizadas com sucesso.'}


class Forecast(Resource):

    def __init__(self):
        # Cria uma conexão com o banco de dados
        self.db = dataset.connect('sqlite:///vendas-prod.db')
        # Obtém a tabela 'vendas'
        self.table = self.db['vendas']

    def post(self):
        # Recebe data inicial e data final e faz a previsão de vendas
        data = request.get_json()
        data_inicial = data['data_inicial']
        data_final = data['data_final']

        # Consulta o banco de dados e cria um DataFrame pandas com as vendas
        vendas = list(self.table.all())
        vendas_df = pd.DataFrame(vendas, columns=['id', 'date', 'venda_total', 'dados_mercado', 'localidade'])
        vendas_df['date'] = pd.to_datetime(vendas_df['date'])  # converte as datas para o formato datetime
        vendas_df = vendas_df[['date', 'venda_total']].rename(columns={'date': 'ds', 'venda_total': 'y'})

        # Cria o modelo Prophet e treina com os dados existentes
        m = Prophet()
        m.fit(vendas_df)

        # Cria as datas futuras para fazer as previsões
        future = m.make_future_dataframe(periods=(pd.to_datetime(data_final) - pd.to_datetime(data_inicial)).days + 1)

        # Faz as previsões usando o modelo Prophet
        forecast = m.predict(future)

        # Converte as previsões em um dicionário JSON
        forecast_json = forecast[['ds', 'yhat']].rename(columns={'ds': 'date', 'yhat': 'venda_total'})
        forecast_json['date'] = forecast_json['date'].dt.strftime('%Y-%m-%d')  # converte a coluna 'date' para string
        forecast_json = forecast_json.to_dict('records')

        return {'previsao': forecast_json}


api.add_resource(Vendas, '/vendas')
api.add_resource(Forecast, '/forecast')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)

