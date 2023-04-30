import pandas as pd 
from prophet import Prophet

class FeatureEngineer(object):
    def __init__(self):
        self.model = Prophet()

    def transformation(self, vendas):
        vendas_df = pd.DataFrame(vendas, columns=['id', 'date', 'venda_total', 'dados_mercado', 'localidade'])
        vendas_df['date'] = pd.to_datetime(vendas_df['date'])  # converte as datas para o formato datetime
        vendas_df = vendas_df[['date', 'venda_total']].rename(columns={'date': 'ds', 'venda_total': 'y'})
        return vendas_df

    def train(self, vendas_df):
        self.model.fit(vendas_df)
    
    def _format(self,forecast):
        forecast_json = forecast[['ds', 'yhat']].rename(columns={'ds': 'date', 'yhat': 'venda_total'})
        forecast_json['date'] = forecast_json['date'].dt.strftime('%Y-%m-%d')  # converte a coluna 'date' para string
        forecast_json = forecast_json.to_dict('records')
        return forecast_json

    def _convert_datetime(self, data_inicial, data_final):
        self.pd_data_final = pd.to_datetime(data_final)
        self.pd_data_inicial = pd.to_datetime(data_inicial)
        
    def previsao(self, data_inicial, data_final):
        self._convert_datetime(data_inicial, data_final)
        future = self.model.make_future_dataframe(periods=(self.pd_data_final - self.pd_data_inicial).days + 1)
        forecast = self.model.predict(future)
        forecast_json = self._format(forecast)
        return forecast_json
        
        
        