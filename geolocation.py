import pandas as pd
import folium
import requests
import webbrowser
print("hello")
url="https://data.cityofchicago.org/resource/ijzp-q8t2.json?%24limit=50"
response = requests.get(url)
data=response.json()
df=pd.DataFrame(data)
print(df)
df.info()
df=df[['primary_type', 'latitude', 'longitude']].dropna()
df['latitude']=df['latitude'].astype(float)
df['longitude']=df['longitude'].astype(float)
crime_map=folium.Map(location=[41.871,-87.6298], zoom_start=11) 
for _, row in df.iterrows():
      folium.CircleMarker(
         location=[row['latitude'], row['longitude']],
         radius=3,
         popup=row['primary_type'],
         fill=True,
         color='red',
         fill_opacity=0.7
      ).add_to(crime_map)
crime_map.save("crime_map.html")
print("Map saved as crime_map.html")  
webbrowser.open('crime_map.html')
