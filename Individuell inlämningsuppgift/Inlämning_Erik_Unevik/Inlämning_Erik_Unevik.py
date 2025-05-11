import os
import requests
import json
import pandas as pd
import pprint
from datetime import datetime

# Först definera get weather funktionen för att få väderprognosen
def get_weather():
    # Använd den aktuella katalogen där filen ligger
    base_dir = os.path.dirname(os.path.abspath(__file__))

    url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
    response = requests.get(url)

    if response.status_code == 200:
        vader_prognos = response.json()

        # Hämta ut koordinater från geometry
        koordinater = []
        for ingeo in vader_prognos["geometry"].values():
            if ingeo != "Point":
                for value in ingeo:
                    for real in value:
                        koordinater.append(real)

        long_value = koordinater[0]
        lat_value = koordinater[1]

        lat = [lat_value] * 26
        long = [long_value] * 26

        # Hämta väderdata för 26 timmar framåt
        vader_data = vader_prognos["timeSeries"][2:28]
        df_vader = pd.DataFrame(vader_data)

        # Tidpunkt då datan hämtades
        datetime_decimals = datetime.now()
        datetime_nodecimals = datetime_decimals.strftime("%Y-%m-%d %H:%M")

        # Skapa datum- och tidsvariabler
        validtime_lista = []
        datum = []
        hour = []

        for tid in df_vader["validTime"]:
            validtime_lista.append(tid)
            for rad in validtime_lista:
                sliced_datum = rad[0:10]
                sliced_hour = rad[11:13]
            datum.append(sliced_datum)
            hour.append(sliced_hour)

        hour_int = [int(timmar) for timmar in hour]

        # Temperatur
        temperatur = []
        for parameters in df_vader["parameters"]:
            for parameter in parameters:
                if parameter["name"] == "t":
                    temperatur.append(float(parameter["values"][0]))

        # Nederbörd
        nederbord = []
        for parameters in df_vader["parameters"]:
            for parameter in parameters:
                if parameter["name"] == "pcat":
                    for value in parameter["values"]:
                        if value == 0:
                            value = False
                        else:
                            value = True
                    nederbord.append(value)

        # Leverantör
        SMHI = ["SMHI"]
        provider = SMHI * 26

        # Skapa dataframe
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

        df_ihop_vader = pd.DataFrame(vader_dict)

        # Spara som Excel i samma mapp som .py-filen
        excel_path = os.path.join(base_dir, "vaderdata_ErikUnevik.xlsx")
        df_ihop_vader.to_excel(excel_path, sheet_name="Väderdata", index=False)

        print(f"Data har laddats ned", datetime_nodecimals)
        print()

    else:
        print(f"Error vid hämtning av data status kod: {response.status_code}")



# Sedan definera provide_Weather så att jag kan ladda upp väderprognosen
def provide_weather():
    # Använd samma sökväg som get_weather
    base_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(base_dir, "vaderdata_ErikUnevik.xlsx")

    df = pd.read_excel(excel_path)

    provide_provider = df["Provider"].tolist()
    provide_datum = df["DATUM"].tolist()
    provide_longitud = df["Koordinat Longitud"].tolist()
    provide_latitud = df["Koordinat Latitud"].tolist()
    provide_temperatur = df["Temperature"].tolist()
    provide_rainorsnow = df["Rainorsnow"].tolist()

    tid_0000 = pd.to_datetime(df['Hour'], format='%H').dt.strftime('%H:%M')

    print(f"Prognos från {provide_provider[0]} Datum:{provide_datum[0]}")
    print("Med koordinater Latitud/Longitud [Liljeholmen]:")
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



