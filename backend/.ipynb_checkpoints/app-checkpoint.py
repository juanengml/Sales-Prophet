from flask import Flask, request
from flask_restful import Resource, Api
from lmodel.database import Database
from lmodel.business import FeatureEngineer

app = Flask(__name__)
api = Api(app)

class Vendas(Resource):
    def __init__(self):
        # Cria uma conexão com o banco de dados
        self.vendas = Database()

    def post(self):
        # Recebe dados dos meses passados e cadastra as vendas no banco
        data = request.get_json()
        print(data)
        self.vendas.insere_items(data)
        return {'message': 'Vendas cadastradas com sucesso.'}

    def get(self):
        # Lista todas as vendas cadastradas no banco
        return {'vendas': self.vendas.busca_items()}

    def delete(self):
        # Recebe ids das vendas e deleta do banco
        self.vendas.deleta_item(request.get_json())
        return {'message': 'Vendas deletadas com sucesso.'}

    def put(self):
        # Recebe ids das vendas e atualiza as vendas no banco
        data = request.get_json()
        self.vendas.atualiza_item(data)
        return {'message': 'Vendas atualizadas com sucesso.'}


class Forecast(Resource):

    def __init__(self):
        # Cria uma conexão com o banco de dados
        self.vendas = Database()
        self.feature_engineer = FeatureEngineer()

    def post(self):
        # Recebe data inicial e data final e faz a previsão de vendas
        data = request.get_json()
        data_inicial = data['data_inicial']
        data_final = data['data_final']

        vendas = self.vendas.busca_completa()
        vendas_df = self.feature_engineer.transformation(vendas)
        self.feature_engineer.train(vendas_df)
        forecast_json = self.feature_engineer.previsao(data_inicial, data_final)
        return {'previsao': forecast_json}


api.add_resource(Vendas, '/vendas')
api.add_resource(Forecast, '/forecast')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)

