from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(
        "<html>Welcome to Newspaper agency</html>"
    )
