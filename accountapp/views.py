from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# def = define
# request 를 넣어서 response 에 답해준다
def hello_world(request):
    return HttpResponse("Hello World!!")
