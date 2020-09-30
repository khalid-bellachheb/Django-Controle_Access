
import folium

villes={
    'Brest' : (48.3885,-4.4841),
    "Rennes": (48.1089,-1.6782),
    "Paris": (48.8550,2.3542),
    "Mannheim":(49.4874,8.4643)
}

m = folium.Map(location=[48.3577, -4.5659])

for ville, coords in villes.items():
    folium.Marker(coords, popup=f'<b>{ville}</b><br>{coords}',
     tooltip=ville,
     icon=folium.Icon(color='red', icon='info-sign')
     ).add_to(m)

m.save("osm.html")