# import requests
# import json
 
# # API-anrop med avrundade longitud och latitud
# url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
# response = requests.get(url)
 
# # Kontrollera att svaret är OK
# if response.status_code == 200:
#     forecast_SMHI = response.json()
   
#     # Skriv ut hela API-svaret i ett indenterat format för att förstå strukturen
#     print(json.dumps(forecast_SMHI, indent=4))
# else:
#     print(f"Misslyckades med att hämta data från SMHI. Statuskod: {response.status_code}")

    #------------
import requests
import json
 
url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
response = requests.get(url)
 
if response.status_code == 200:
    forecast_SMHI = response.json()
   
    print("Översta lagret av nycklar i JSON-svaret:")
    print(forecast_SMHI.keys())
   
    # Om du redan vet att datan finns i en "timeseries"-sektion, kolla direkt på den.
    if 'timeSeries' in forecast_SMHI:
        print("Nycklar inom 'timeSeries':")
        print(forecast_SMHI['timeSeries'][0].keys())  # Skriv ut nycklarna i den första timeSeries-posten
                                        #0 syftar på närmsta timmen. t.ex 5 hade vart prognos om 5h
        # Visa parametrar som kan inkludera temperatur
        print("Parameter-data:")
        print(forecast_SMHI['timeSeries'][0]['parameters'])  # Skriv ut parameter-sektionen där temperatur borde finnas
        for i in forecast_SMHI['timeSeries'][0]['parameters']:
            if i['name'] == "t":
                print(i['values'])
       
else:
    print(f"Misslyckades med att hämta data från SMHI. Statuskod: {response.status_code}")

#----------------------------------------------------------------------------

import requests
import json
 
url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
response = requests.get(url)
 
if response.status_code == 200:
    forecast_SMHI = response.json()
   
    print("Översta lagret av nycklar i JSON-svaret:")
    print(forecast_SMHI.keys())
   
    # Om du redan vet att datan finns i en "timeseries"-sektion, kolla direkt på den.
    if 'timeSeries' in forecast_SMHI:
        print("Nycklar inom 'timeSeries':")
        print(forecast_SMHI['timeSeries'][0].keys())  # Skriv ut nycklarna i den första timeSeries-posten
                                        #0 syftar på närmsta timmen. t.ex 5 hade vart prognos om 5h
        # Visa parametrar som kan inkludera temperatur
        print("Parameter-data:")
        print(forecast_SMHI['timeSeries'][0]['parameters'])  # Skriv ut parameter-sektionen där temperatur borde finnas
        for i in forecast_SMHI['timeSeries'][0]['parameters']:
            if i['name'] == "t":
                print(i['values'])
       
else:
    print(f"Misslyckades med att hämta data från SMHI. Statuskod: {response.status_code}")