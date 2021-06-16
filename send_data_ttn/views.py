from django.shortcuts import render
#import sys
# Create your views here.
def Accueil(request):
    context={}
    return render(request,'send_data_ttn/send_data_ttn.html',context)