from django.http import HttpResponse
from django.shortcuts import render

# Check if authenticated
# Check request valid
# Collect data from DB
# Render response


# def = define
# request 를 넣어서 response 에 답해준다
def hello_world(request):
    return render(request, 'accountapp/hello_world.html')
