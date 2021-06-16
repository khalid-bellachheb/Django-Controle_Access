from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from data_ttn.models import data_ttn


# Create your views here.
# api/up
@csrf_exempt 
def save_data(request):
    if request.method=='POST':
        data = json.loads(request.body.decode('utf-8'))
        print('Autorisation : ', data["uplink_message"]["decoded_payload"]["Autorisation"])
        print('Badge : ', data["uplink_message"]["decoded_payload"]["Badge"])
        print('Porte :  ', data["uplink_message"]["decoded_payload"]["Porte"])
        print('Zone :  ', data["uplink_message"]["decoded_payload"]["Zone"])
        
    return HttpResponse("ok")

# api/matricule
@csrf_exempt 
def save_maricule_data(request):
    if request.method=='POST':
        print("matricule id was send")
        data = json.loads(request.body.decode('utf-8'))
        data = json.loads(data)
        d=data_ttn.objects.filter(badge=data["Badge"])
        if d :
            for dd in d :
                dd.matricule_id=data["matricule_id"]
                dd.save()
        else:
            print("send right data")
        
    return HttpResponse("ok")

# api/facialRecognition
@csrf_exempt 
def save_maricule_data(request):
    if request.method=='POST':
        print("face Recognition id was send")
        data = json.loads(request.body.decode('utf-8'))
        data = json.loads(data)
        print(data)
        
    return HttpResponse("ok")
