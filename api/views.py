from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from data_ttn.models import data_ttn

def decrypte_Autorisation(auto):
    if (auto == "1"):
        return "Accés autorisé"
    if (auto == "0"):
        return 'Accés non autorisé'
    return ''

def decrypte_Badge(bad):
    return 

def decrypte_Porte(por):
    if (por == "A"):
        return "A"
    if (por == "B"):
        return "B"
    if (por == "C"):
        return "C"
    if (por == "D"):
        return "D"
    if (por == "E"):
        return "E"
    return ""

def decrypte_Zone(zon):
    if (zon == "1"):
        return "Zone 1"
    if (zon == "2"):
        return "Zone 2"
    if (zon == "3"):
        return "Zone 3"
    return ""

def decrypte_status(sta):
    if (sta == "E"):
        return "Employé(e)"
    if (sta == "V"):
        return "Visiteur"
    return ""
# Create your views here.
# api/up
@csrf_exempt 
def save_data(request):
    if request.method=='POST':
        data = json.loads(request.body.decode('utf-8'))
        auto=decrypte_Autorisation(data["uplink_message"]["decoded_payload"]["Autorisation"])
        bad=data["uplink_message"]["decoded_payload"]["Badge"]
        por=decrypte_Porte(data["uplink_message"]["decoded_payload"]["Porte"])
        zon=decrypte_Zone(data["uplink_message"]["decoded_payload"]["Zone"])
        sta=decrypte_status(data["uplink_message"]["decoded_payload"]["status"])
        obj=data_ttn(badge=bad,Autorisation=auto,Porte=por, Zone=zon,status=sta)
        obj.save()
        
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
def save_faceRecognition_data(request):
    if request.method=='POST':
        print("face Recognition id was send")
        data = json.loads(request.body.decode('utf-8'))
        data = json.loads(data)
        d=data_ttn.objects.filter(badge=data["Badge"])
        if d :
            for dd in d :
                dd.matricule_id=data["Nom"]
                dd.save()
        else:
            print("send right data")
        print(data)
        
    return HttpResponse("ok")
