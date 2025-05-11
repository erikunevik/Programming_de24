



# #___________ Kontrollerar att listorna ser ok ut för provide weather
# # print(provide_provider)
# # print(provide_datum)
# # print(provide_nedladdat)
# # print(provide_longitud)
# # print(provide_latitud)
# # print(provide_hour, provide_temperatur, provide_rainorsnow)


# import pandas as pd
# from datetime import datetime

# df = pd.read_excel(r"C:\Users\eriku\Desktop\DataenginerSTI2024-2026\Programmering\Programmering I\Individuell inlämningsuppgift\Inlämning_Erik_Unevik\vaderdata_ErikUnevik.xlsx")
        


# provide_hour = df["Hour"].tolist() 
     
# provide_hour.apply(pd.to_datetime)  

# print(provide_hour)    


import pandas as pd

from datetime import datetime

# Load the Excel file into a DataFrame
df = pd.read_excel(r"C:\Users\eriku\Desktop\DataenginerSTI2024-2026\Programmering\Programmering I\Individuell inlämningsuppgift\Inlämning_Erik_Unevik\vaderdata_ErikUnevik.xlsx")

# Convert the 'Hour' column to a list (optional, you can work directly with the DataFrame)
provide_hour = df["Hour"].tolist() 

# Use pd.to_datetime directly on the Series instead of the list
changed = pd.to_datetime(df['Hour'], format='%H').dt.strftime('%H:%M')





# Print the DataFrame or the formatted hour column
print(changed)


x = datetime(provide_hour)

print(x.strftime("%X"))

print(x)

a = provide_hour(11, 34, 56)

print("Hour =", a.hour)
print("Minute =", a.minute)
print("Second =", a.second)
print("Microsecond =", a.microsecond)


    #---------, gör om int listan till stringlista

       

        

        # intlist_tostring = []
        # for nummer in provide_hour:
        #     intlist_tostring.append(str(nummer))

        #     #------------ Därefter åter till integers för att kunna lägga till 0a till siffror som är nedom 

        # extra_nolla = []
        # for hour in intlist_tostring:
        #     formatted_hour = f"{int(hour):00}"  
        #     extra_nolla.append(formatted_hour)

        # p1c1 = extra_nolla.pop(3)
        # print(f"pc1 är: {p1c1}, type: {type(p1c1)}")

        # #------------- Lägger till minutformat via fstring

        # tid_0000 = []
        # for hour in extra_nolla:
        #     timme = f"{hour}:00"
        #     tid_0000.append(timme)