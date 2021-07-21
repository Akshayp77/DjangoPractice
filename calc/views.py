from django.shortcuts import render
from django.http import HttpResponse

def Index(request):
    return HttpResponse("Hello World")
def add(request):
    if request.method == 'GET':
        val1=request.GET['num1']
        val2=request.GET['num2']

        return HttpResponse(int(val1)+int(val2))
    else:
        return HttpResponse("No response")