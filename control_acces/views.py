from django.shortcuts import render,redirect
# Open street map module
import folium
from folium import plugins
from folium.features import DivIcon
# TTN API
import requests
import json
#
from django.views.generic import TemplateView
from django.views.generic.list import ListView
# Create your views here.

from data_ttn.models import data_ttn




def TTN_API():
    print("TTN API Function")
    headers = {
        'Accept': 'application/json',
        'Authorization': 'key ttn-account-v2.QgWpB8kKKfhXnndMVKweVz2YKlu3hu-vTU_00-zNRmE',
    }

    params = (
        ('last', '1m'),
    )

    response = requests.get('https://pre2020.data.thethingsnetwork.org/api/v2/query/stm32', headers=headers, params=params)

    if(str(response)=="<Response [200]>"):
        ## Read the responses into a Pandas Dataframe
        res=response.json()
        for x in res :
            obj=data_ttn(device_id=x["device_id"],badge=x["badge"],Autorisation=x["authorisation"],Porte=x["porte"], Zone=x["zone"])
            obj.save()
            print('Response==[200]')
        else :
            print("Response!=[200]")
            


def my_view(request):
        print("my redirect view")
        return redirect("control_acces")


class FoliumVListView(ListView):
    template_name = "control_acces/control_acces.html"
    #https://docs.djangoproject.com/fr/3.1/ref/class-based-views/generic-display/#listview
    model = data_ttn

    def get_context_data(self, **kwargs):
        data=data_ttn.objects.filter(Porte='C')
        port_c=data.last()
        data=data_ttn.objects.filter(Porte='A')
        port_a=data.last()
        #self.object_list = self.get_queryset().latest('Porte')
        #for x in self.object_list:
        #    print(x)
        print("port c",port_c)
        print("port a",port_a)
        print('folium view')
        # définir les villes dans la carte
        villes={
        'Brest' : (48.3885,-4.4841),
        "Paris": (48.8550,2.3542),
        "Rabat":(34.0169,-6.8019)}
        # les points de polygon
        locations = [[5.22252,-52.77741],
                 [5.22287,-52.78058],
                 [5.22431,-52.78165],
                 [5.22624,-52.78087],
                 [5.22604,-52.77859],
                 [5.2282,-52.7781],
                 [5.2272,-52.7756],
                 [5.2256,-52.7762],
                 [5.22358,-52.77628],
                 [5.22252,-52.77741]
                 ]
        # les points des ports
        ports={
        'E' : [5.22766,-52.77771],
        "D": [5.22640,-52.77815],
        #'C':[5.22612,-52.77661],
        'B':[5.2238,-52.7767]
        #'A':[5.2230,-52.7779]
        }
        # les points des zones
        Zones={
        'Zone 1' : [5.22446,-52.77619],
        'Zone 2':[5.22494,-52.78015],
        "Zone 3": [5.22716,-52.77746]}
        # Créer un object figure
        figure = folium.Figure()
        # Posionner la carte sur Guyane
        m = folium.Map(location=[5.2254,-52.7773],width='60%', height='70%', 
        left='22%', top='0%',zoom_start=16,control_scale=True)
        m.add_to(figure)
        # Afficher les villes
        for ville, coords in villes.items():
            folium.Marker(coords, popup=f'<b>{ville}</b><br>{coords}',
            tooltip=ville,
            icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)
        # Créer un cercle dans la carte
        #folium.CircleMarker( location=[5.22370,-52.77830], radius=12, fill=False ,weight=5,).add_to(m)
        # Controler les couches sur la carte 
        folium.raster_layers.TileLayer('OpenStreetMap').add_to(m)
        folium.raster_layers.TileLayer('CartoDB positron').add_to(m)
        folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
        #folium.raster_layers.TileLayer('Mapbox Bright').add_to(m)
        folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
        folium.LayerControl().add_to(m)
        # Ajouter Geocoder
        #plugins.Geocoder().add_to(m)
        # Géolocaliser l'utilisateur.
        folium.plugins.LocateControl().add_to(m)
        # Trace un rectangle
        #folium.vector_layers.Rectangle
        folium.vector_layers.Polygon(locations=locations, tooltip='Centre Spatial Guyannais' ).add_to(m)

        """
        for data in data_ttn :
            print(data.Porte)"""
        #port = data_ttn.get_deferred_fields(self)
        #print(port)
        # ///////////// Port A /////////////
        html=f'<p>Device Id : {port_a.device_id}</p><p>Port : {port_a.Porte}</p><p>{port_a.Zone}</p> <form action="accueil/" method="GET"><button type="submit" onclick="window.parent.location.href= \'http://127.0.0.1:8000/send_data_ttn/\';"> Get acces <script></script></button></form>'
        iframe = folium.IFrame(html=html, width=160, height=180)
        popup = folium.Popup(iframe, max_width=2650)
        folium.vector_layers.Circle(location=[5.2230,-52.7779],radius=30, tooltip='A',color='#ff3333').add_to(m)
        folium.Marker([5.2230,-52.7779], popup=popup,#f'<p>Device Id : {port_a.device_id}</p><p>Badge : {port_a.badge}</p><p>Port : {port_a.Porte}</p>',
            tooltip='A',
            icon=folium.Icon(color="green",icon="check", prefix='fa'),
             html='<div style="font-size: 24pt">%s</div>' % 'text'
            ).add_to(m)

        # ///////////// Port C /////////////
        html=f'<p>Device Id : {port_c.device_id}</p><p>Badge : {port_c.badge}</p><p>Port : {port_c.Porte}</p><p>{port_c.Autorisation}</p><p>{port_c.Zone}</p>'
        iframe = folium.IFrame(html=html, width=160, height=180)
        popup = folium.Popup(iframe, max_width=2650)
        folium.vector_layers.Circle(location=[5.22612,-52.77661],radius=30, tooltip='A',color='#ff3333').add_to(m)
        folium.Marker([5.22612,-52.77661], popup=popup,#f'<p>Device Id : {port_a.device_id}</p><p>Badge : {port_a.badge}</p><p>Port : {port_a.Porte}</p>',
            tooltip='C',
            icon=folium.Icon(color="orange",icon="minus", prefix='fa'),
             html='<div style="font-size: 12pt">%s</div>' % 'text'
            ).add_to(m)

        # affichage des cercles et des markeur
        for  port_name, port in ports.items():
            folium.vector_layers.Circle(location=port,radius=30, tooltip=port_name,color='#ff3333').add_to(m)
            folium.Marker(port, popup=f'<b>{port}</b><br>Port {port_name}',
            tooltip=port_name,
            icon=folium.Icon(color="red",icon="wrench", prefix='fa'),
             html='<div style="font-size: 24pt">%s</div>' % 'text'
            ).add_to(m)
            
        # labels
        for zone_name,zone_coords in Zones.items():
            folium.map.Marker(zone_coords, 
            icon=DivIcon(
                icon_size=(120,36),
                icon_anchor=(0,0),
                html='<div style="font-size: 14pt">%s</div>' % zone_name,
                )
            ).add_to(m)
        # "user-times" and "user-o" , "wrench"
        figure.render()
        return {"control_acces": figure}
