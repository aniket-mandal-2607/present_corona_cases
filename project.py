import folium
import pandas as pd

def y(point,i,color):
    str1="""{}
    Cases: {}
    Deaths: {}
    Recovered: {}""".format(country['location'][i],country['confirmed'][i],country['dead'][i],country['recovered'][i])
    folium.Marker(location=point,
                  popup=str1,
                  icon=folium.Icon(color=color, icon='tint', icon_color='purple')
    ).add_to(vmap)

country=pd.read_csv('countries.csv')
vmap=folium.Map(location=[0.00,0.00], zoom_start=1)
coor=country[['latitude','longitude']]
i=0
for point in place:
    if country['confirmed'][i]>50000:
        y(point,i,'darkred')
    elif country['confirmed'][i]>25000:
        y(point,i,'red')
    elif country['confirmed'][i]>10000:
        y(point,i,'orange')
    else:
        y(point,i,'green')
        
    i+=1

vmap.save('index.html')
