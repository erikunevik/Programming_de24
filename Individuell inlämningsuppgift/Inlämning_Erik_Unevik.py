def get_weather():

    #1___________ Ladda ned väderdata och importera funnktioner

    import os # För att föra samman data
    import requests
    import json
    import pandas as pd
    import pprint # För att läsa dictionaries bättre
    from datetime import datetime
   
    url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
    response = requests.get(url)

    if response.status_code == 200:
        vader_prognos = response.json()


         #2______, Hämta ut koordianter från gemoetry då den finnas ovan timeseries i json.koden

        koordinater = []
        for inner_dict in vader_prognos["geometry"].values():
            if inner_dict != "Point": # Så att vi får ut koordinates
                for value in inner_dict: #  ]]
                    for real in value: # Ingen []
                        koordinater.append(real) # Jag har även testat tidigare att dessa är floats


        #, skapar 26 dupliceringar av positioner för att kunna få in i min gemensamma dataframe sedermera
        long_value = (koordinater[0]) 
        lat_value = (koordinater[1]) # Har testat att de är floats

        lat = [lat_value] * 26
        long = [long_value] * 26
        
        # Timeseries innebär data för prognosen
        vader_data = vader_prognos["timeSeries"][2:28] # Ger ut tiden från vad klockan är nu tills 24 fram + 1 H

        df_vader = pd.DataFrame(vader_data)

       #3__________ Skapar variabel för Datetime när datan hämtades
        
        datetime_decimals = datetime.now()
        datetime_nodecimals = datetime_decimals.strftime("%Y-%m-%d %H:%M") # För att ta bort sekunder och decimaler
        
        #4_______, Skapar tid och datum variabel

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
        hour_int = []
        for timmar in hour:
            hour_int.append(int(timmar))

       

        
        #5_______ , Skapar temperatur variabel

        # Gå igenom df_vader för att få fram temperatur
        temperatur = []
        for parameters in df_vader["parameters"]: 
            for parameter in parameters:
                if parameter["name"] == "t": # Ifall t är korrekt parameter
                   for value in parameter["values"]: 
                       temperatur.append(float(value)) # För att temperatur ska vara en float 

           #6_______ , Skapar nederbörd variabel


        nederbord = []
        for parameters in df_vader["parameters"]: 
            for parameter in parameters:
                if parameter["name"] == "pcat": # Ifall pcat är korrekt parameter
                #    print(parameter) För att jämföra att parametern stämmer med excelfilen sen
                   for value in parameter["values"]: 
                       if value == 0:
                        value = False # Ingen nederbörd
                       else:
                        value = True # Nederbörd, har testat att det är en bool 

                       nederbord.append((value)) 


            #6 _______ Ordna variabel provider

        SMHI = ["SMHI"] 

        provider = SMHI * 26
           

    # 7______Skapar en dict för att slå ihop filer 
    vader_dict = {

        "Nedladdat": datetime_nodecimals,
        "Koordinat Longitud": long,
        "Koordinat Latitud": lat,
        "DATUM": datum,
        "Hour": hour_int,
        "Temperature": temperatur,
        "Rainorsnow": nederbord,
        "Provider": provider

    }

    #8________Skapar dataframen som ska exporteras sen och ger alternativ för att spara
     
    df_ihop_vader = pd.DataFrame(vader_dict)

    vill_du = input("Vill du döpa filen och spara den på egen vald plats? Ja/Nej")

    if vill_du.lower() == "ja":

        file_name = input("Ange ett filnamn, avsluta med .xlsx:")

        directory = input("Ange en plats att spara på: ")

        excel_path = os.path.join(directory, file_name)
        df_ihop_vader.to_excel(excel_path, sheet_name="Väderdata", index=False)       
    
        print(f"Data har laddats ned")
        print(datetime_nodecimals)    


    else:            

        excel_path = os.path.join(r"D:\Inlämning_Erik_Unevik", "vaderdata_Erik_Unevik.xlsx")
        df_ihop_vader.to_excel(excel_path, sheet_name="Väderdata", index=False)       
    
        print(f"Data har laddats ned till D:\Inlämning_Erik_Unevik och heter vaderdata_Erik_Unevik.xlsx ")
        print(datetime_nodecimals)    

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

    


# def provide_weatherforecast():

# while True:
     
#  print(f"Prognos levereras från  " vad)
        

    









    
    
    
    



# pass

# provide_weatherforecast()    

