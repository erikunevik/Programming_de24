
# #1

# listaTal = []

# for siffror in range(4):
#     siffror= 1
#     tal = int(input(f"Mata in ett tal{siffror}:"))
#     listaTal.append(tal)

# # listaTal.sort()

# # print(listaTal[-1])

# maxlista= max(listaTal)

# print(maxlista)

# 2

# listaTal = []

# for talinlista in range(3):
#     tal = int(input (f"Mata in tal {talinlista + 1}:"))
#     listaTal.append(tal)

# maxLista = max(listaTal)
# minLista = min(listaTal)

# listaTal.sort()
# print(listaTal[1])

# 3

# listaTal = [5, 67, 33, 89, 53, 76, 13, 98, 23, 56]


# while True:
   

#    gissa = int(input("Gissa ett tal mellan 0 - 100:"))

#    if gissa in listaTal:
#       print("Bra gissat!")
#       print()
#       break
   

#    elif gissa not in listaTal:
#       print("Äsch, fel gissning det är en på 10 att du gissar rätt\n")

# 4

# favoritDjur = ["gris", "häst", "hund", "apa", "noshörning", "lemur"]

# användarDjur = []

# for gissningar in range (3):
#     antal = input(f"Skriv in djur {gissningar + 1}:").lower()
#     användarDjur.append(antal)

# gemensamma_djur = []


# for gemensamt in (favoritDjur):
#     if gemensamt in användarDjur:
#      gemensamma_djur.append(gemensamt) 
    
# print(f"Ni hade {gemensamma_djur} gemensamt")

# Detta var lösning men gemensamma djur, nu med siffror...

# favoritDjur = ["gris", "häst", "hund", "apa", "noshörning", "lemur"]

# användarDjur = []

# for gissningar in range (3):
#     antal = input(f"Skriv in djur {gissningar + 1}:").lower()
#     användarDjur.append(antal)


# gemensamma_djur = 0

# for gemensamt in (favoritDjur):
#     if gemensamt in användarDjur:
#      gemensamma_djur = gemensamma_djur + 1
    
# print(f"Ni hade {gemensamma_djur} gemensama djur")

# 6

# kontolista = {}

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

#         konto_till = (input("Skriv ett kontonummer:\n"))
#         saldo = float(input("Fyll i ditt saldo:\n"))
#         kontolista[konto_till] = saldo
#         (print)

#     elif val == "2":
#         konto_tabort = (input("Skriv vilket kontonummer som ska bort:\n"))
#         if konto_tabort in kontolista:
#             del kontolista[konto_tabort]
#             print(f"Konto {konto_tabort} har tagits bort.")
#         else:
#             print("Du har skrivit in fel värde")
        
#         enter = input("Press enter to return to the main menu\n").lower()

#     elif val == "3":
#         print (kontolista)
        
#         enter = input("Press enter to return to the main menu\n").lower()

#     elif val == "4":
#             print (sum(kontolista.values()))

#             enter = input("Press enter to return to the main menu\n").lower()

#     elif val == "5":
#             for keys, values in kontolista.items():
#                  print(f" Konto: {keys}, saldo: {values}")

#             enter = input("Press enter to return to the main menu\n").lower()

#     elif val == "6":
         
#            print("Programmet avslutas")
#            break

  

            

    
                                

            














    