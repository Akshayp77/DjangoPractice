from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
def Index(request):
    return HttpResponse("Hello World")
@csrf_exempt
def add(request):
    if request.method == 'GET':
        val1=request.GET['num1']
        val2=request.GET['num2']

        return HttpResponse(int(val1)+int(val2))
    elif request.method == 'POST':
        
        print("+"*20)
        print(request)
        print("+"*20)
        val1=request.POST['num1']
        val2=request.POST['num2']

        return HttpResponse(int(val1)+int(val2))
    else:
        return HttpResponse()
