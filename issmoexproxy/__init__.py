from twisted.web import server
from twisted.internet import reactor
from issmoexproxy.resources.kmymoneyquotes import KMyMoneyQuotes
from issmoexproxy.proxy import IisMoexProxy


def main():
    """
    Точка входа
    :return:
    """
    try:
        root = IisMoexProxy()
        root.putChild(b'', root)

        quotes = KMyMoneyQuotes()
        root.putChild(b'quotes', quotes)

        site = server.Site(root)
        reactor.listenTCP(8080, site)

        reactor.run()
    except KeyboardInterrupt:
        reactor.stop()
