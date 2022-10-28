from conf import settings


async def app(scope, receive, send):

    # print(scope)

    request = settings.REQUEST(scope, settings)
    router = settings.ROUTER

    # print(request.headers)

    assert request.type == 'http'

    response = router.get_reponse(request, settings)

    await send(response.start)

    await send(response.body)
