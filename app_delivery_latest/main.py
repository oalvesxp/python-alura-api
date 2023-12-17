import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    data_json = response.json()

    data = {}
    for item in data_json:
        name = item['Company']
        
        if name not in data:
            data[name] = []
        
        data[name].append({
            "item": item['Item'],
            'price': item['price'],
            'description': item['description']
        })

else:
    print(f'Erro {response.status_code}')

for name, value in data.items():
    file_name = f'{name}.json'
    with open(file_name, 'w') as file:
        json.dump(value, file, indent=4)

