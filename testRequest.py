from app.config import config
from app.modules import hg_api

key = config.hgApiKey
hg = hg_api.HgApi(key)
url = hg.getUrl('finance/quotations')

response = hg.dolarQuotation()
print(response)
