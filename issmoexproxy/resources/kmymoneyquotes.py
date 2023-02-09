from twisted.web import resource
import json
import requests


class KMyMoneyQuotes(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        board, security = request.postpath[0].decode().split(':')

        # /iss/engines/[engine]/markets/[market]/boards/[board]/securities/[security]
        market = 'shares'

        if board in ('TQOB', 'TQCB'):
            market = 'bonds'

        engine = 'stock'
        url = "http://iss.moex.com/iss/engines/{engine}/markets/{market}/boards/{board}/securities.json?" \
              "securities={security}".format(engine=engine, market=market, board=board, security=security)
        print(url)
        data = requests.get(url).json()
        columns = data["securities"]["columns"]
        # PREVADMITTEDQUOTE - Признаваемая котировка предыдущего дня
        # PREVLEGALCLOSEPRICE - Цена закрытия предыдущего дня
        # SECID -
        # PREVDATE - даты цены закрытия
        index_price = columns.index('PREVLEGALCLOSEPRICE')
        index_date = columns.index('PREVDATE')
        index_id = columns.index('SECID')

        sec = data["securities"]["data"][0]

        ret = 'date={0} price={1} id={2}'.format(sec[index_date], sec[index_price], sec[index_id])
        return ret.encode()

