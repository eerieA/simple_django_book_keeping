# primer\views.py
from django.http import HttpResponse


def say_hello(request):
    message = "hello world"

    return HttpResponse(message, content_type="text/plain")
