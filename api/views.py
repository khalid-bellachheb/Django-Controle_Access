from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt 
def save_data(request):
    if (True):
        if request.method=='POST':
            print(request.body)
    return HttpResponse(ok)
