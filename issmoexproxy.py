from twisted.web import server, resource
from twisted.internet import reactor, task
from resources.kmymoneyquotes import KMyMoneyQuotes


class IisMoexProxy(resource.Resource):
    def render_GET(self, _request):
        return b'<html><head><title>IIS MOEX proxy</title></head><body>IIS MOEX proxy</body></html>'


def main():
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

if __name__ == "__main__":
    main()