import json
import requests
import pandas as pd


def get_dados_cep(cep):
    url_api = f'http://www.viacep.com.br/ws/{cep}/json/'
    req = requests.get(url_api)
    if req.status_code == 200:
        dados_json = json.loads(req.text)
        return dados_json

def get_dados_endereco(uf, cidade, rua):
    url_api = f'http://www.viacep.com.br/ws/{uf}/{cidade}/{rua}/json/'
    req = requests.get(url_api)
    if req.status_code == 200:
        dados_json = json.loads(req.text)
        return dados_json



cep = get_dados_endereco("SP", "São Paulo", "Avenida+São+João")
df = pd.DataFrame(cep)
df.to_excel("busca.xlsx", index = False)