# coding=utf-8
from django.http import HttpResponse


def index(request):
    """
    Контроллер главной страницы
    :param request:
    :return: HttpResponse
    """
    return HttpResponse("Index page")
