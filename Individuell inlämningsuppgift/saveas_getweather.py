
# Först definera get weather funktionen för att få väderprognosen
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

        #8________Skapar dataframen som ska exporteras sen 
  
           
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

             # Sedan definera provide_Weather så att jag kan ladda upp väderprognosen

        return excel_path

def provide_weather(excel_path):

    #1_______Importerar fil och gör dataframen till olika listor

        import pandas as pd
        from datetime import datetime

        df = pd.read_excel(excel_path)

        provide_provider = df["Provider"].tolist() 
        provide_datum = df["DATUM"].tolist()
        provide_nedladdat = df["Nedladdat"].tolist() 
        provide_longitud = df["Koordinat Longitud"].tolist() 
        provide_latitud = df["Koordinat Latitud"].tolist() 
        provide_hour = df["Hour"].tolist() 
        provide_temperatur = df["Temperature"].tolist() 
        provide_rainorsnow= df["Rainorsnow"].tolist()  

        #1__________Gör om provide_hour så det går att bruka i outputen. 

        #---------, gör om int listan till stringlista

        list_string = map(str, provide_hour)
        list_string = list(list_string)

        #------------ Därefter åter till integers för att kunna lägga till 0a till siffror som är nedom 


        lista2 = []
        for hour in list_string:
            formatted_hour = f"{int(hour):02}"  
            lista2.append(formatted_hour)

        #------------- Lägger till minutformat via fstring

        tid_stor = []
        for hour in lista2:
            timme = f"{hour}:00"
            tid_stor.append(timme)



        #2____________Outputen
        print(f"Prognos från {provide_provider[0]} Datum:{provide_datum[0]}")
        print("Med koordinater Latitud/Longitud:")
        print(f"{provide_latitud[0]} {provide_longitud[0]}, Väderlek:\n")
        for delprognos in range(4):
            tid = tid_stor[delprognos]
            temperatur = provide_temperatur[delprognos]
            nederbord = provide_rainorsnow[delprognos]


            if nederbord == False:
                print(f"{tid} {temperatur} Grader, ingen nederbörd")
            
            else:
                print(f"{tid} {temperatur} Grader, nederbörd")
                

# Sist Definera mainfunktionen efter get and provide_weather för att kunna köra valmenyn
   
def main():

    excel_path = None

    while True:
        print("\n Välkommen till Eriks weather forecast")
        print("1. Ladda ned väderprognos")
        print("2. Visa väderprognos")
        print("3. Avsluta")
        

        choice = input("Välj ett alternativ (1-3):")

        print("\n")
        
        if choice == '1':
            excel_path = get_weather()
            
        elif choice == '2':
            provide_weather(excel_path)
            
        elif choice == '3':
            
            print("Avslutar...")
            break
        else:
            print("Ogiltigt val, försök igen.")
  

if __name__ == '__main__':
    main()


