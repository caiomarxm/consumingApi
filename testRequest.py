from app.config import config
from app.modules import hg_api
import requests

hg = hg_api.hgApi(config.hgApiKey)

print(hg.dolarQuotation())

response = requests.get('https://api.hgbrasil.com/finance/quotations?key=12b04fd9')

print(response.body)
