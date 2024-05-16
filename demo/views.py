from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def greet(request):
    return render(request, 'demo/hello.html', {"name": "vera"})


def greet_me(request, name):
    return HttpResponse(f"Hello {name}")
