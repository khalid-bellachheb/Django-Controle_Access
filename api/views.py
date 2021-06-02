from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt 
def save_data(request):
    if (True):
        if request.method=='POST':
            data = json.loads(request.body.decode('utf-8'))
            print('Autorisation ': data["uplink_message"]["decoded_payload"]["Autorisation"])
    return HttpResponse("ok")
