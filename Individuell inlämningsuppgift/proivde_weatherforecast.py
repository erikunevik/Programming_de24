def provide_weather():

 #1_______Importerar fil och gör dataframen till olika listor

  import pandas as pd
  from datetime import datetime

  df = pd.read_excel(r"C:\Users\eriku\Desktop\DataenginerSTI2024-2026\Programmering\Programmering I\Individuell inlämningsuppgift\vaderdata.xlsx")

  provide_provider = df["Provider"].tolist() 
  provide_datum = df["DATUM"].tolist()
  provide_nedladdat = df["Nedladdat"].tolist() 
  provide_longitud = df["Koordinat Longitud"].tolist() 
  provide_latitud = df["Koordinat Latitud"].tolist() 
  provide_hour = df["Hour"].tolist() 
  provide_temperatur = df["Temperature"].tolist() 
  provide_rainorsnow= df["Rainorsnow"].tolist()  

  # 1__________Gör om provide_hour så det går att bruka i outputen. 

  #  ---------, gör om int listan till stringlista

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

  
  # tid_stor= pd.to_datetime(df['Hour'], format='%H:M').dt.strftime('%H:%M')


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

provide_weather()

      
     





  











































