from twisted.web import resource


class IisMoexProxy(resource.Resource):
    def render_GET(self, _request):
        return b'<html><head><title>IIS MOEX proxy</title></head><body>IIS MOEX proxy</body></html>'

if __name__ == "__main__":
    from issmoexproxy import main
    main()