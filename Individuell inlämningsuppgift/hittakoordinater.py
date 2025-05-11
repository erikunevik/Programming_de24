
import os 
import requests
import json
import pandas as pd
import pprint

url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
response = requests.get(url)

if response.status_code == 200:
        vader_prognos = response.json()





# df_vader = pd.DataFrame(vader_prognos)

# print(vader_prognos["geometry"].values())
# print(vader_prognos["geometry"].items())
# print(vader_prognos["geometry"].keys())

koordinater = []
for inner_dict in vader_prognos["geometry"].values():
    if inner_dict != "Point": # Så att vi får ut koordinates
         for value in inner_dict: #  ]]
              for real in value: # Ingen []
               koordinater.append(real) # Jag har även testat tidigare att dessa är floats


#, skapar 26 dupliceringar av positioner för att kunna få in i min gemensamma dataframe
long_value = (koordinater[0]) 
lat_value = (koordinater[1]) # Har testat att de är floats

lat = [lat_value] * 26
long = [long_value] * 26

# print(lat, long)
          

# vader_prognos = pd.DataFrame(lat, long,  columns=["Koordinat Latitud"])

# excel_path = os.path.join(r"C:\Users\eriku\Desktop\DataenginerSTI2024-2026\Programmering\Programmering I\Individuell inlämningsuppgift", "koordianter.xlsx") 
# vader_prognos.to_excel(excel_path)

     
     
# import os
# import requests
# import pandas as pd

# url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
# response = requests.get(url)

# if response.status_code == 200:
#     vader_prognos = response.json()

# Extracting the coordinates
# koordinater = vader_prognos["geometry"]["coordinates"]
# print(koordinater)  # Inspecting the structure

# If it's a list of lists
# df_vader = pd.DataFrame(koordinater, columns=["Longitude", "Latitude"])

# Saving to Excel
# excel_path = os.path.join(r"C:\Users\eriku\Desktop\DataenginerSTI2024-2026\Programmering\Programmering I\Individuell inlämningsuppgift", "koordianter.xlsx")
# df_vader.to_excel(excel_path, index=False)

# print(df_vader)








# import numpy as np
# np.array(koordinater,dtype=float)

# print(type(koordinater))


# for koordinater in (vader_prognos["geometry"].values()):
#         if koordinater in (vader_prognos["geometry"].values())  == [16.017767, 57.999628]:
#                 print(koordinater.values())


# Om dom finns = ta dom


# koordinater = []
# for coordinates in vader_prognos["geometry"]:
#         if coordinates == "coordinates":
#               print(coordinates)
              
        # for liljeholmen in coordinates:
        #         for liljeholmen in ["coordinates"]:    
        #          koordinater.append(liljeholmen)



# print(koordinater)         

                


# print(koordinater)





# import datetime


# Now = datetime.datetime.now() 
# print(Now)



