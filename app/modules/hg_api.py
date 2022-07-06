import requests

class HgApi():
    _key = None
    _error = False

    def __init__(self, key=None):
        if key:
            self._key = key

    def getKey(self):
        return self._key

    def getUrl(self, endpoint=''):
        url = f"https://api.hgbrasil.com/{endpoint}?format=json&key={self._key}"
        return url

    def request(self, endpoint='', params = {}):
        url = f"https://api.hgbrasil.com/{endpoint}?format=json&key={self._key}"
        try:
            return requests.get(url, params)
        except:
            self._error = True
            return False

    def dolarQuotation(self, params={'fields': 'only_results,USD'}):
        data = self.request('finance/quotations', params)
        if data:
            return data.json()
        return False
        
    def isError(self):
        return self._error
