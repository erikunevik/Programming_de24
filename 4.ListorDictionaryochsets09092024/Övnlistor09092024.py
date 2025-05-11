
1

# lista=[]

# for i in range (4):
#     tal = input("Mata in ett tal")
#     lista.append(tal)


# maxtal = max(lista)

# print(f"maxtalet är {maxtal}")



# lista = []

# for i in range (4):
#     tal = input(f"Mata in tal: {i+1}")
#     lista.append(tal)

# maxlista = max(lista)
# print(f"Maxvärdet var {maxlista}")

#-------------------- Aladins lösning




# # 2

# lista = []

# for i in range (3):
#     i = 1

#     tal = int(input("Mata in tre tal"))
#     lista.append(tal)

# max = max(lista)
# min = min(lista)

# # median = sorted(lista)


# # print(f" Medianvärdet är {median[1]}")

# sorted_lista = sorted(lista)
# median = sorted_lista[1]


# print(f" Medianvärdet är {median}")



# 3

# lista = [45, 78, 96, 90, 100, 5, 12, 57, 23, 90]
# while True:
#  gissa = int(input("Gissa ett valfritt tal mellan 0-100"))

#  if gissa in lista:
#   print("Wow, du lyckades, det är en på 10!")
#   break
#  else:
#   print("Synd, bättre lycka nästa gång")

# 4

# list_djur= ["apa", "noshörning", "murmis", "bäver", "lama", "gris", "häst", "ponny", "katt", "tulip", "lina",]

# gissa_djur_lista = []

# for i in range (3):

#  skriv_in = input("Skriv in ditt favoritdjur tre gånger så ska vi se om du har något gemensamt med mig:").lower().split(" , ")
#  gissa_djur_lista.append(skriv_in)

# gemensam = []

# for i in list_djur:

#    if i in gissa_djur_lista:

#           gemensam.append(i)

# samma =len(gemensam)

# print(f" Vi hade {samma} gemensamma djur")

#----------------------------------------

# Aladins lösning

# list_djur= ["apa", "noshörning", "murmis", "bäver", "lama", "gris", "häst", "ponny", "katt", "tulip", "lina",]

# gissa_djur_lista = []


# skriv_in = input("Skriv in ditt favoritdjur tre gånger så ska vi se om du har något gemensamt med mig:").lower().split(",")

# skriv_in = [djur.strip() for djur in skriv_in]
 

# gemensam = 0

# for i in skriv_in:

#    if i in list_djur:

#     gemensam += 1

# print(f" Vi hade {gemensam} gemensamma djur")

# 5

# seriea = [club.lower() for club in ["Atalanta", "Napoli", "Milan", "Inter", "Juventus", "Roma", "Fiorentina", "Parma", "Bologna", "Sampdoria", "Genoa", "Udinese"]]

# while True:
 
#   print("Välkommen till listan där du shoppar Serie A klubbar\n")
#   val = input("Press (1) for add, press (2) to remove, press (3) to edit, press (4) to print the list, Press (5) to insert a new club to the list, press (6) to reverse the list , press (7) to sort, press (8) to delete shopping list and (0) to exit\n")


#   if val == "1":
#      add = input ("Add a club to the list: \n")
#      seriea.append(add)
#      print(f"Your list looks like this: {seriea} \n")

#      enter = input("Press enter to return to the main menu\n").lower()
#   elif val == "2":
#       remove = input("Which club would you like to delete?: \n").lower()
#       seriea.remove(remove)

#       enter = input("Press enter to return to the main menu\n").lower()
      
#   elif val == "3":
#         vilken = input("Which club would you like to change the name for?\n").lower()
#         nytt = input("What new name would you like the club to have?\n").lower()
#         seriea = [nytt if x == vilken else x for x in seriea]
              
#         enter = input("Press enter to return to the main menu\n").lower()

#   elif val == "4":
#         print(f"Your list looks like this: {seriea} \n")

#         enter = input("Press enter to return to the main menu\n").lower()

#   elif val == "5":
#         nytt2 = input(" Enter a new club to the list\n").lower()
#         seriea.append(nytt2)

#         enter = input("Press enter to return to the main menu\n").lower()     
        
#   elif val == "6":
#         seriea.reverse()
#         print(f"The reversed list looks like this: {seriea}\n")

#         enter = input("Press enter to return to the main menu\n").lower()

#   elif val == "7":
#         seriea.sort()
#         print(f"Your sorted list lookes like this: {seriea}\n")

#         enter = input("Press enter to return to the main menu\n").lower()

#   elif val == "8":
#         seriea.clear()
        
#         enter = input("Press enter to return to the main menu\n").lower()
        

#   elif val == "0":
#        print("Tack för att du shoppade hos oss!\n")
#        break

# 6 Du behöver kontonummer, totalsaldo, 

# konto_lista = {}

# while True:
    
#     print("Välkommen till banken, tryck:\n")
#     print ("(1) för att skapa konto")
#     print("(2) för att ta bort konto")
#     print("(3) för att lista alla kontonummer")
#     print("(4) lista totalsaldo")
#     print("(5) Lista alla kontonummer och saldo")
#     print("(6) Avsluta\n")
    
#     val = input("Gör dit val:")
#     if val == "1":
#          kontonummer = int(input("Skriv in kontonummer\n"))
        
#          saldo =int(input("Skriv in ditt saldo\n"))
        
#          konto_lista[kontonummer]=saldo
        
#          print(konto_lista)

#          enter = input("Press enter to return to the main menu\n").lower()

#     elif val == "2":
#          delete = int(input("Vilket konto vill du ta bort?n"))
#          konto_lista.pop(delete)

#          enter = input("Press enter to return to the main menu\n").lower()

#     elif val == "3":
#    #   print(konto_lista.keys())

#        for i in (konto_lista):
#            print (i)

#        enter = input("Press enter to return to the main menu\n").lower()


#     elif val == "4":
#         print(sum(konto_lista.values()))

#         enter = input("Press enter to return to the main menu\n").lower()

#     elif val == "5":
        
#           for i, saldo in konto_lista.items():
#            print (f"kontonummer: {i} saldo: {saldo}")

#           enter = input("Press enter to return to the main menu\n").lower()

 
        

      
        
   

      






        
   #      enter = input("Press enter to return to the main menu\n").lower()

   #  elif val == "2":
   #       tabort =input("Skriv det konto du vill ta bort") .lower()
   #       del konto_lista{tabort}

   #       enter = input("Press enter to return to the main menu\n").lower()







  
# nested_dictionary = {
#     "person 1": {
#         "name": "Alice",
#         "age": 30
#     },
#     "person 2": {
#         "name": "Bob",
#         "age": 25
#     }
# }


  

#   names = ["A", "B", "C"]
# b = names.index("B")
# print(b)

# names[b] = "Z"
# print(names)

  




  
  
 
  


    
    
















