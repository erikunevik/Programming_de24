
import os 
import requests
import json
import pandas as pd

def get_weather():
    url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
    response = requests.get(url)
 

    if response.status_code == 200:
        vader_prognos = response.json()

        # Timeseries innebär data för prognosen
        vader_data = vader_prognos["timeSeries"] 

        df_vader = pd.DataFrame(vader_data)

        # for i in df_vader["timeSeries"]:
        #     if i["parameter"] == "t":
        #         print(i) 
    
        # OS hjälper mig arbeta med det underliggande operativsystemet, path & join slår ihop sökvägen och väder
        excel_vader = os.path.join(r"C:\Users\eriku\Desktop\DataenginerSTI2024-2026\Programmering\Programmering I\Individuell inlämningsuppgift", "vader.xlsx") 
        
        # Tar bort index columnen som är onödig
        df_vader.to_excel(excel_vader, index=False) 

        print(f"Data har laddats ned till {excel_vader}\n")

        huvudmeny = input("Tryck på någon knapp för att komma till huvudmenyn")

        
   
    
    else:
        print(f"Misslyckades med att hämta data från SMHI. Statuskod: {response.status_code}")


    
def main():
    while True:
        print("\n Välkommen till Eriks weather forecast")
        print("1. Ladda ned väderprognos")
        print("2. Visa väderprognos")
        print("3. Avsluta")
        

        choice = input("Välj ett alternativ (1-3):")

        print("\n")
        
        if choice == '1':
            get_weather()
            
        elif choice == '2':
            pass
            
        elif choice == '3':
            
            print("Avslutar...")
            break
        else:
            print("Ogiltigt val, försök igen.")




if __name__ == '__main__':
    main()