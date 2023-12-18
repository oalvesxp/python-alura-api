from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint para testes...
    '''
    return {'Hello':'world'}

@app.get('/api/company/')
def get_company(eatery: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes.
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        data_json = response.json()
        if eatery is None:
            return {'Dados':data_json}

        data = []
        for item in data_json:
            if item['Company'] == eatery:
                data.append({
                    "item": item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'Restaurante':eatery, 'Cardápio': data}
    
    else:
        return{'Erro':f'{response.status_code} - {response.text}'}