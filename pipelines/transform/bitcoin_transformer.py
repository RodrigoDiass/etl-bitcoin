from pydantic import BaseModel, PositiveFloat, ValidationError
from datetime import datetime
import json
from glob import glob

class BitcoinModel(BaseModel):
    amount: PositiveFloat
    base: str
    currency: str
    timestamp: datetime

try:
    file_path = 'data/extraction_btc_value*.json'
    files = glob(file_path)
    latest_file = max(files)
    print(f"Getting file {latest_file}")
except ValidationError as e:
    print(f'Error finding file: {e}')
try:
    with open(latest_file, 'r') as f:
        data = json.load(f)
    BitcoinModel(**data)
    print('Data Validation Sucessfull!')
except ValidationError as e:    
    print(e)


