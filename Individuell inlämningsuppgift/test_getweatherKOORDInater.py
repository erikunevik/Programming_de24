
import os # För att föra samman data
import requests
import json
import pandas as pd
import pprint # För att läsa dictionaries bättre
from datetime import datetime


def get_weather():
    url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
    response = requests.get(url)

    if response.status_code == 200:
        vader_prognos = response.json()


         #____________, först hämta ut koordianter från gemoetry då den finnas ovan timeseries

        koordinater = []
        for inner_dict in vader_prognos["geometry"].values():
            if inner_dict != "Point": # Så att vi får ut koordinates
                for value in inner_dict: #  ]]
                    for real in value: # Ingen []
                        koordinater.append(real) # Jag har även testat tidigare att dessa är floats

       
        
        # Timeseries innebär data för prognosen
        vader_data = vader_prognos["timeSeries"][2:28] # Ger ut tiden från vad klockan är nu tills 24 fram + 1 H

        df_vader = pd.DataFrame(vader_data)


       #__________1 Skapar datetime

        
        datetime_decimals = datetime.now()
        datetime_nodecimals = datetime_decimals.strftime("%Y-%m-%d %H:%M") # För att ta bort sekunder och decimaler

        print(datetime_nodecimals)

        
        #_________2, Skapar tid och datum 

        validtime_lista = []
        datum = []
        hour = []
        

        

        # Tar ut valid time till att börja med
        for tid in df_vader["validTime"]:
            validtime_lista.append(tid)
                           
            #Slicar ut dat och tid ur valid
            for rad in validtime_lista:

                sliced_datum = rad[0:10]
                sliced_hour = rad[11:13]

            datum.append(sliced_datum)
            hour.append(sliced_hour)
            
        # Gör hours till integers, har kontrollerat att de är int
        hour_int  = [int(i) for i in hour]
        
        #_______ 3, Skapar temperatur

        # Gå igenom df_vader för att få fram temperatur
        temperatur = []
        for parameters in df_vader["parameters"]: 
            for parameter in parameters:
                if parameter["name"] == "t": # Ifall t är korrekt parameter
                   for value in parameter["values"]: 
                       temperatur.append(float(value)) # För att temperatur ska vara en float 

           #_______ 4, Skapar nederbörd  


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


      
           
   



        


    # Ordna så vi får data för de första 24 timmarna bara, kanske in range?

     
        
        


     

# Skapar en dict för att slå ihop filer 
    vader_dict = {

        "Nedladdat": datetime_nodecimals,

        "DATUM": datum,

        "Hour": hour_int,

        "Temperature": temperatur,

        "Nederbörd": nederbord

    }

    koordinater_dict = {

        "Koordinater Long/Lat": koordinater
    }

    
   

    df_ihop_vader = pd.DataFrame(vader_dict)
    df_koordinat = pd.DataFrame(koordinater_dict)
                
    excel_path = os.path.join(r"C:\Users\eriku\Desktop\DataenginerSTI2024-2026\Programmering\Programmering I\Individuell inlämningsuppgift", "vaderdata.xlsx") 

    # Mergar filerna så att man inte overwritar
    with pd.ExcelWriter(excel_path) as writer:
        df_ihop_vader.to_excel(writer, sheet_name = "Väderdata", index=False)
        df_koordinat.to_excel(writer, sheet_name = "Koordinater", index=False)
                 


    # with pd.ExcelWriter(excel_path) as writer:
    # df_temperatur.to_excel(writer, sheet_name='Temperature', index=False)
    # df_tid.to_excel(writer, sheet_name='DATETIME', index=False)

    
 
    print(f"Data har laddats ned\n")


get_weather()

#------------------------------ För att hitta keys

# import os 
# import requests
# import json
# import pandas as pd

# def get_weather():
#     url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
#     response = requests.get(url)

#     if response.status_code == 200:
#         vader_prognos = response.json()

#         vader_data = vader_prognos["timeSeries"] 
#         df_vader = pd.DataFrame(vader_data)

#         print (df_vader.keys())

# get_weather()


# Försök att loopa mig till resultat -----------------------

# for index, row in df_vader.iterrows():
#             for första11ord in row["validTime"]:
#              slice_datum = första11ord[0:11]
#              tid.append(slice_datum)
#             print(tid)

        

        
#         print(f"Här är dom {slice_datum}")

#---------------- Min tidigare lösning för tid

    # tid = []

        # for index, row in df_vader.iterrows():
        #     tid.append(row["validTime"])
        #     # print(tid)

        

        # slice_datum = tid[0:11]
        # print(f"Här är dom {slice_datum}")


        # Test
     


     #------------ för att testa att jag får ut float ur temperatur

        #   p1c1 = temperatur.pop(3)
        # print(f"pc1 är: {p1c1}, type: {type(p1c1)}")


        #------------ För att läsa datan bättre, pprint.pprint(vader_data)


    #-------------------- För att hitta keys till lokalisering
# print(vader_prognos["geometry"].values())
# print(vader_prognos["geometry"].items())
# print(vader_prognos["geometry"].keys())

    