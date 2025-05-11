
import os 
import requests
import json
import pandas as pd
import pprint

url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
response = requests.get(url)

if response.status_code == 200:
        vader_prognos = response.json()

vader_data = vader_prognos["timeSeries"] # Ger ut tiden från vad klockan är nu tills 24 fram + 1 H

df_vader = pd.DataFrame(vader_data)


nederbord = []
for parameters in df_vader["parameters"]: 
        for parameter in parameters:
                if parameter["name"] == "pcat": # Ifall pcat är korrekt parameter
                #    print(parameter) För att jämföra att parametern stämmer med excelfilen sen
                   for value in parameter["values"]: 
                       if value == 0:
                        value = True # Ingen nederbörd
                       else:
                        value = False # Nederbörd, har testat att det är en bool 

                       nederbord.append((value)) 











                    


vader_prognos = pd.DataFrame(nederbord, columns=["Nederbörd"])

excel_path = os.path.join(r"C:\Users\eriku\Desktop\DataenginerSTI2024-2026\Programmering\Programmering I\Individuell inlämningsuppgift", "nederbord.xlsx") 
vader_prognos.to_excel(excel_path)