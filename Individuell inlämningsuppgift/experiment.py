
# Först definera get weather funktionen för att få väderprognosen
def get_weather():


        #1___________ Ladda ned väderdata och importera funnktioner

        import os # För att föra samman data
        import requests
        import json
        import pandas as pd
        import pprint # För att läsa dictionaries bättre
        from datetime import datetime
    
        url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json" # URL addressen 
        response = requests.get(url)

        if response.status_code == 200:
            vader_prognos = response.json() # Gör om svaret till json format för hantering
            df_hela = vader_prognos["geometry"]
            coordinates = df_hela["coordinates"]
            koord = pd.DataFrame(coordinates, columns=["Longitude", "Latitude"])
            lat = koord["Latitude"].iloc[0]
            long = koord["Longitude"].iloc[0]
            print(lat, long)


        

       


            #2______, Hämta ut koordianter från gemoetry då den finnas ovan timeseries i json.koden

            koordinater = []
            for ingeo in koord["coordinates"]:
                if ingeo != "Point": # Så att vi får ut koordinates
                    for value in ingeo: #  ]], utanför listan
                        for real in value: # Ingen [], inuti listan
                            koordinater.append(real) # Jag har även testat tidigare att dessa är floats

            print(koordinater)

            


            


            koordinater = []
            for ingeo in vader_prognos["geometry"].values():
                if ingeo != "Point": # Så att vi får ut koordinates
                    for value in ingeo: #  ]], utanför listan
                        for real in value: # Ingen [], inuti listan
                            koordinater.append(real) # Jag har även testat tidigare att dessa är floats


            #, skapar 26 dupliceringar av positioner för att kunna få in i min gemensamma dataframe sedermera
            long_value = (koordinater[0]) 
            lat_value = (koordinater[1]) # Har testat att de är floats

            lat = [lat_value] * 26
            long = [long_value] * 26
            
            #____3 Timeseries innebär data för prognosen
            vader_data = vader_prognos["timeSeries"][2:28] # Ger ut tiden från vad klockan är nu tills 24 fram + 1 H

            
            #4__________ Skapar variabel för Datetime när datan hämtades
            
            datetime_decimals = datetime.now()
            datetime_nodecimals = datetime_decimals.strftime("%Y-%m-%d %H:%M") # För att ta bort sekunder och decimaler
                       
            #5_______, Skapar tid och datum variabel

            validtime_lista = []
            datum = []
            hour = []
        
            # Tar ut valid time till att börja med

            
            for tid in vader_data:
                valid_time = tid["validTime"]
                validtime_lista.append(valid_time)

                # print(validtime_lista)
                            
                #Slicar ut dat och tid ur valid
                for rad in validtime_lista:

                    sliced_datum = rad[0:10]
                    sliced_hour = rad[11:13]

                datum.append(sliced_datum)
                hour.append(sliced_hour)
                
            # Gör hours till integers, har sen kontrollerat att de är int
            hour_int = []
            for timmar in hour:
                hour_int.append(int(timmar))
             
        
            #6_______ , Skapar temperatur variabel

            # Gå igenom df_vader för att få fram temperatur
            # temperatur = []
            # for parameters in vader_data:
            #     if parameters["parameters"] == "name":
            #         for parameter in parameters: # Går igenom listan av dictionaries
            #             if parameter["name"] == "t": # t är grader C
            #                 temperatur.append(float(parameter["values"][0])) # Det blir 0 för att det finns bara en siffra i t

            # print(f"aa{temperatur}")

            temperatur = []
        for parameters in vader_data:
            for parameter in parameters["parameters"]:  # Access the parameters list directly
                if parameter["name"] == "t":  # Check if the name is "t"
                    temperatur.append((parameter["values"]))  # Append the temperature value

            
        temperatur = [float(temp) for temp in temperatur]

        print(temperatur)
                            


           

           #7_______ , Skapar nederbörd variabel


        #     nederbord = []
        #     for parameters in vader_data["parameters"]: 
        #         for parameter in parameters: # Går igenom listan av dictionaries
        #             if parameter["name"] == "pcat": # Ifall pcat är korrekt parameter
        #                 for value in parameter["values"]: # Letar värden i pcat
        #                     if value == 0:
        #                      value = False # Ingen nederbörd
        #                     else:
        #                         value = True # Nederbörd, har testat att det är en bool 

        #                 nederbord.append((value)) 


        #         #8 _______ Ordna variabel provider

        #         SMHI = ["SMHI"] 

        #         provider = SMHI * 26
            

        #     # 9______Skapar en dict för att slå ihop filer 
        #         vader_dict = {

        #         "Nedladdat": datetime_nodecimals,
        #         "Koordinat Longitud": long,
        #         "Koordinat Latitud": lat,
        #         "DATUM": datum,
        #         "Hour": hour_int,
        #         "Temperature": temperatur,
        #         "Rainorsnow": nederbord,
        #         "Provider": provider

        #                   }

        #     #10________Skapar dataframen som ska exporteras sen 
    
        #     df_ihop_vader = pd.DataFrame(vader_dict) # Lägger till dictionarien            

        #     excel_path = os.path.join(r"C:\Users\eriku\Desktop\DataenginerSTI2024-2026\Programmering\Programmering I\Individuell inlämningsuppgift\Inlämning_Erik_Unevik", "vaderdata_ErikUnevik.xlsx")
        #     df_ihop_vader.to_excel(excel_path, sheet_name="Väderdata", index=False)       
            
        #     print(f"Data har laddats ned", datetime_nodecimals)
        #     print()

        # else: 
        #     print(f"Error vid hämtning av data status kod: {response.status_code}")  

# Sedan definera provide_Weather så att jag kan ladda upp väderprognosen

def provide_weather():

    #1_______Importerar fil och gör dataframen till olika listor

        import pandas as pd
        from datetime import datetime

        df = pd.read_excel(r"C:\Users\eriku\Desktop\DataenginerSTI2024-2026\Programmering\Programmering I\Individuell inlämningsuppgift\Inlämning_Erik_Unevik\vaderdata_ErikUnevik.xlsx")
        
        provide_provider = df["Provider"].tolist() 
        provide_datum = df["DATUM"].tolist()
        provide_longitud = df["Koordinat Longitud"].tolist() 
        provide_latitud = df["Koordinat Latitud"].tolist() 
        provide_temperatur = df["Temperature"].tolist() 
        provide_rainorsnow= df["Rainorsnow"].tolist()  

        #1__________ Gör om intlistan av tid så det passar in i outputen
    
        tid_0000 = pd.to_datetime(df['Hour'], format='%H').dt.strftime('%H:%M') 
  
        #2____________Outputen
        print(f"Prognos från {provide_provider[0]} Datum:{provide_datum[0]}")
        print("Med koordinater Latitud/Longitud:")
        print(f"{provide_latitud[0]} {provide_longitud[0]}, Väderlek:\n")
        for delprognos in range(4):
            tid = tid_0000[delprognos]
            temperatur = provide_temperatur[delprognos]
            nederbord = provide_rainorsnow[delprognos]


            if nederbord == False:
                print(f"{tid} {temperatur} Grader, ingen nederbörd \u2601\ufe0f \U0001f325\ufe0f  \u2600\ufe0f  ")
            
            else:
                print(f"{tid} {temperatur} Grader, nederbörd \U0001f327\ufe0f \U0001f328\ufe0f ")
                

# Sist Definera mainfunktionen efter get and provide_weather för att kunna köra valmenyn
   
def main():

    while True:
        print("\n")
        print("Välkommen till Eriks weather forecast \U0001f302  ")
        print("1. Ladda ned väderprognos")
        print("2. Visa väderprognos")
        print("3. Avsluta")
        print()
        

        choice = input("Välj ett alternativ (1-3):")

        print("\n")
        
        if choice == '1':
            get_weather()

            input("Tryck enter för att komma till huvudmenyn")
            
        elif choice == '2':
            provide_weather()
            print()
            input("Tryck enter för att komma till huvudmenyn")
            
        elif choice == '3':
            
            print("Programmet avslutas...")
            print("\n")
            break
        else:
            print("Ogiltigt val, försök igen.")
  

if __name__ == '__main__':
    main()


