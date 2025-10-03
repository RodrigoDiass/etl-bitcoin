import requests
from datetime import datetime
import json


def bitcoin_api_extraction(url): 
    response = requests.get(url)
    data = response.json()['data']
    data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data

if __name__ == '__main__':
    url = 'https://api.coinbase.com/v2/prices/spot'
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    bitcoin_data = bitcoin_api_extraction(url)
    file_path = f'data/extraction_btc_value_{current_datetime}.json'
    with open(file_path, 'w') as j:
        json.dump(bitcoin_data, j, indent=4)