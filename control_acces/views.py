from django.shortcuts import render

import folium

from django.views.generic import TemplateView
# Create your views here.
'''
def Control_acces(request):
    context={}
    return render(request,'control_acces/control_acces.html',context)
'''

class FoliumView(TemplateView):
    template_name = "control_acces/control_acces.html"

    def get_context_data(self, **kwargs):
        # définir les villes dans la carte
        villes={
        'Brest' : (48.3885,-4.4841),
        "Rennes": (48.1089,-1.6782),
        "Paris": (48.8550,2.3542),
        "Mannheim":(49.4874,8.4643)}
        # Créer un object figure
        figure = folium.Figure()
        # Posionner la carte sur la ville de Brest
        m = folium.Map(location=[48.3577, -4.5659],width='60%', height='60%', left='20%', top='0%')
        m.add_to(figure)
        # Afficher les villes
        for ville, coords in villes.items():
            folium.Marker(coords, popup=f'<b>{ville}</b><br>{coords}',
            tooltip=ville,
            icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)
        figure.render()
        return {"control_acces": figure}