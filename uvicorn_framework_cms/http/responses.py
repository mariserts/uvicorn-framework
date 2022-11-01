from uvicorn_framework.http.responses import Response



class PermissionDeniedResponse(Response):

    def __init__(self, content='Permission denied'):
        super().__init__(None, content, status=403)
