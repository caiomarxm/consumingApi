import json
import requests

class hgApi():
    __key = None
    __error = False

    def __init__(self, key=None):
        if key:
            self.__key = key

    def getKey(self):
        return self.__key

    def getUrl(self, endpoint='finance/quotations'):
        url = f"https://api.hgbrasil.com/{endpoint}?format=json&key={self.__key}"
        return url

    def request(self, endpoint='', params = {}):
        url = f"https://api.hgbrasil.com/{endpoint}?format=json&key={self.__key}"
        if params:
            # Tratamento dos Parâmetros...
            pass
        try:
            response = requests.get(url)
            data = json.loads(response)
            return data
        except:
            self.__error = True
            return False

    def dolarQuotation(self):
        data = self.request('finance/quotations')
        if data:
            # Verificação dos dados...
            pass
        
    def isError(self):
        return self.__error
