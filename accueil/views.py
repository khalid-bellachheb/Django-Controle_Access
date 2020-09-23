from django.shortcuts import render

# Create your views here.
def Accueil(request):
    context={}
    return render(request,'accueil/accueil.html',context)


