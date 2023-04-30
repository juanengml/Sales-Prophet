import dataset

class Database(object):

     def __init__(self):
        self.db = dataset.connect('sqlite:///vendas-prod.db')
        # Obtém a tabela 'vendas'
        self.table = self.db['vendas']

     def insere_items(self, data):
        self.table.insert_many(data['data'])
     
     def busca_items(self):
        return  [dict(v) for v in self.table.all()]
    
     def deleta_item(self, data):
        for venda in data:
            self.table.delete(id=venda['id'])
     
     def atualiza_item(self, data):
        for venda in data:
            self.table.update(venda, ['id'])

     def busca_completa(self):
        return list(self.table.all())