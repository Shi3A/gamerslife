# coding=utf-8
from django.http import HttpResponse


def index(request):
    """
    Front page
    :param request:
    :return: HttpResponse
    """
    return HttpResponse("Index page")
