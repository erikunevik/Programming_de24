
# # import os 
# # import requests
# # import json
# # import pandas as pd

# # def get_weather():
# #     url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
# #     response = requests.get(url)
 

# #     if response.status_code == 200:
# #         vader_prognos = response.json()

# #         # Timeseries innebär data för prognosen
# #         vader_data = vader_prognos["timeSeries"] 

# #         df_vader = pd.DataFrame(vader_data)

# #         for index, row in df_vader.iterrows():
# #             for paramteter in row["parameter"]:
# #                 if parameter["name"] == "t":
# #                      print(row)

# # get_weather()

# # # for index, row in df_vader.iterrows():
# # #             for parameter in row["parameters"]:
# # #                 if parameter["name"] == "t":  # Check the parameter name
# # #                     print(row) 


# import os 
# import requests
# import json
# import pandas as pd

# def get_weather():
#     url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.02152/lat/59.30997/data.json"
#     response = requests.get(url)

#     if response.status_code == 200:
#         vader_prognos = response.json()
        
#         # Timeseries innebär data för prognosen
#         vader_data = vader_prognos["timeSeries"] 
#         df_vader = pd.DataFrame(vader_data)

#         # Gå igenom df_vader för att få fram temperatur
#         # temperatur = []
#         # for index, row in df_vader.iterrows():
#         #     for parameter in row["parameters"]:
#         #         if parameter["name"] == "t": # Check for temperature
#         #             temperatur.append(parameter["values"])

#         temperatur = []
#         for parameters in df_vader["parameters"]: 
#             for parameter in parameters:
#                 if parameters["name"] == "t": 
#                     temperatur.append(float(parameter["values"][0]))
        

       
#     df_temperatur = pd.DataFrame(temperatur, columns=["Temperature"])

#     excel_path = os.path.join(r"C:\Users\eriku\Desktop\DataenginerSTI2024-2026\Programmering\Programmering I\Individuell inlämningsuppgift", "testtemperatur.xlsx") 
#     df_temperatur.to_excel(excel_path)
 
#     print(f"Data har laddats ned\n")


# get_weather()




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

        # Gå igenom df_vader för att få fram temperatur
        temperatur = []
        for parameters in df_vader["parameters"]: 
            for parameter in parameters:  # parameters is a list, so we loop over each dict inside it
                if parameter["name"] == "t":  # Check for temperature
                    temperatur.append(float(parameter["values"][0]))  # Get the first value from the list

        print(temperatur)  # Just to check the output

# Call the function to test
get_weather()



    







