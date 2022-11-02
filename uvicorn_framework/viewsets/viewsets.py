class ViewSet:

    HTTP_METHOD_GET = 'get'
    HTTP_METHOD_POST = 'post'

    HTTP_METHODS = [
        HTTP_METHOD_GET,
        HTTP_METHOD_POST,
    ]

    def __init__(self, request):
        self.request = request

    def get_context(self):
        return {
            'request': self.request
        }
