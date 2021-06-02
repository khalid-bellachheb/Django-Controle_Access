from django.shortcuts import render
#import sys
# Create your views here.
def Accueil(request):
    context={}
#    sys.stderr.write('log mgs')
    print("autre chose")
    return render(request,'accueil/accueil.html',context)


