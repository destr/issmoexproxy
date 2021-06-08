from twisted.web import resource
import json
import requests

class KMyMoneyQuotes(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        board, security = request.postpath[0].decode().split(':')

        # /iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]
        market = 'shares'
        engine = 'stock'
        url = f"http://iss.moex.com/iss/engines/{engine}/markets/{market}/boards/{board}/securities.json?securities={security}"
        print(url)
        data = requests.get(url).json()
        sec = data["securities"]["data"][0]
        ret = 'date={0} price={1} id={2}'.format(sec[17], sec[23], sec[0])
        return ret.encode()

