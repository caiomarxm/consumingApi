from app.config import config
from app.modules import hg_api
from requests import *

key = config.hgApiKey
hg = hg_api.HgApi(key)

response = get('https://api.hgbrasil.com/finance/quotations?key=12b04fd9')
data = response.json()

dolar = data['results']['currencies']['USD']

print(dolar)
