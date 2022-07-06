import json
import requests

class HgApi():
    _key = None
    _error = False

    def __init__(self, key=None):
        if key:
            self._key = key

    def getKey(self):
        return self._key

    def getUrl(self, endpoint='finance/quotations'):
        url = f"https://api.hgbrasil.com/{endpoint}?format=json&key={self._key}"
        return url

    def request(self, endpoint='', params = {}):
        url = f"https://api.hgbrasil.com/{endpoint}?format=json&key={self._key}"
        if params:
            # Tratamento dos Parâmetros...
            pass
        try:
            response = requests.get(url)
            data = json.loads(response)
            return data
        except:
            self._error = True
            return False

    def dolarQuotation(self):
        data = self.request('finance/quotations')
        if data:
            # Verificação dos dados...
            pass
        
    def isError(self):
        return self._error
