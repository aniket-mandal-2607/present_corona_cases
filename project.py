import folium
import pandas as pd

def y(point,i,color):
    str1="""{}
    Cases: {}
    Deaths: {}
    Recovered: {}""".format(dataset['location'][i],dataset['confirmed'][i],dataset['dead'][i],dataset['recovered'][i])
    folium.Marker(location=point,
                  popup=str1,
                  icon=folium.Icon(color=color, icon='tint', icon_color='purple')
    ).add_to(test)

dataset=pd.read_csv('countries.csv')
test=folium.Map(location=[0.00,0.00], zoom_start=1)
coor=dataset[['latitude','longitude']]
place=coor.values.tolist()
i=0
for point in place:
    if dataset['confirmed'][i]>50000:
        y(point,i,'darkred')
    elif dataset['confirmed'][i]>25000:
        y(point,i,'red')
    elif dataset['confirmed'][i]>10000:
        y(point,i,'orange')
    else:
        y(point,i,'green')
        
    i+=1
	
test.save('index.html')
