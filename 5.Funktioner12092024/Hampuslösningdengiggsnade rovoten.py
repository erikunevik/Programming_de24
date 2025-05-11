import random

def gameGuess():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

def tryAgain():
    for i in range(3):
        guess = int(input("Vad är din gissning? "))
        player.append(guess)

lista1 = gameGuess()
print(lista1)

player = []


def playGame():

    ratt_position = 0
    fel_position = 0
    attempts = 0


    for i in range(3):
        guess = int(input("Vad är din gissning? "))
        player.append(guess)

    while True:
        for i in range(len(lista1)):
            if lista1[i] == player[i]:
                ratt_position += 1
            elif lista1[i] in player:
                fel_position += 1

        if ratt_position == len(lista1):
            print(f"Alla tal är rätt och på rätt position! Det tog {attempts} försök!")
            break
        elif fel_position > 0 and ratt_position > 0:
            print(f"{fel_position} tal är rätt men på fel position, {ratt_position} tal är på rätt position")
            attempts += 1
            player.clear()
            ratt_position = 0
            fel_position = 0
            tryAgain()
        elif ratt_position > 0:
            print(f"{ratt_position} tal är på rätt position.")
            attempts += 1
            player.clear()
            ratt_position = 0
            fel_position = 0
            tryAgain()
        elif fel_position > 0:
            print(f"{fel_position} tal är rätt men på fel position.")
            attempts += 1
            player.clear()
            ratt_position = 0
            fel_position = 0
            tryAgain()
        elif ratt_position == 0 and fel_position == 0:
            print("Inga tal är rätt.")
            attempts += 1
            player.clear()
            ratt_position = 0
            fel_position = 0
            tryAgain()

playGame()

# ------------------------------ min


# import random

# def game_guess():

#     digits = list(range(10))
#     random.shuffle(digits)
#     return digits[:3]

# def try_again():

#     for i in range(3):
#        gissningar = int(input("Gissa ett tal"))
#        spelarens_gissningar.append(gissningar)

# def end_game():
#     exit()
   

# spelarens_gissningar = []
# spelets_gissningar = game_guess()


# def play_game():

#     global spelets_gissningar
#     print(spelets_gissningar)

#     rätt_position = 0
#     fel_position = 0
#     försök = 0
    
    

#     while True:

#         spelarens_gissningar.clear()
#         rätt_position = 0
#         fel_position = 0
#         försök = 1

       

#         for i in range(3):
#           gissningar = int(input("Gissa ett tal"))
#           spelarens_gissningar.append(gissningar)


#         for nummer in range(len(spelets_gissningar)):
#             if spelarens_gissningar[nummer] == spelets_gissningar[nummer]:
#                 rätt_position += 1
                
#             elif spelarens_gissningar[nummer] in spelets_gissningar:
#                 fel_position  += 1
                


#         if rätt_position == 3:
#              if försök == 1:
#                 print(f"Grattis, du klarade spelet, på {försök} försök")
#                 spelarens_gissningar.clear()
#                 rätt_position = 0
#                 fel_position = 0
#                 break
             

#              elif försök > 0:
#                 print(f"Grattis, du klarade spelet, på {försök} försök")
#                 spelarens_gissningar.clear()
#                 rätt_position = 0
#                 fel_position = 0
#                 försök = 0
#                 break
            
     
#         elif fel_position > 0 and rätt_position >0:
#            print(f" Du gissade {fel_position} siffror rätt, men på fel position och {rätt_position} siffror på rätt position ")
#            spelarens_gissningar.clear()
#            rätt_position = 0
#            fel_position = 0
#            försök += 1
#            play_game()


#         elif rätt_position > 0:
#            print(f" Du gissade {rätt_position} siffror på rätt position")
#            spelarens_gissningar.clear()
#            rätt_position = 0
#            fel_position = 0
#            försök += 1
#            play_game()

#         elif fel_position > 0:
#            print(f" Du gissade {fel_position} siffror rätt, men på fel position")
#            spelarens_gissningar.clear()
#            rätt_position = 0
#            fel_position = 0
#            försök += 1
#            play_game()

#         elif fel_position and rätt_position == 0:
#            print(f" Du gissade inga siffror rätt")
#            spelarens_gissningar.clear()
#            rätt_position = 0
#            fel_position = 0
#            försök += 1
#            play_game()


#     svar = input("Vill du spela igen, (ja), (nej)").lower()
    

#     if svar == "ja":
#      spelets_gissningar = game_guess()  
#      spelarens_gissningar.clear()
#      play_game()
        
#     if svar == "nej":  
#      print("Programmet avslutas") 
#      exit()
        

# play_game()






# ------------------------------ chatgpt


# import random

# def game_guess():
#     digits = list(range(10))
#     random.shuffle(digits)
#     return digits[:3]

# spelarens_gissningar = []
# spelets_gissningar = game_guess()

# def play_game():
#     global spelets_gissningar
#     print(spelets_gissningar)  # You can remove this line if you want to hide the answer

#     rätt_position = 0
#     fel_position = 0
#     försök = 0

#     while True:
#         spelarens_gissningar.clear()  # Clear guesses before a new attempt
#         while len(spelarens_gissningar) < 3:
#             try:
#                 gissningar = int(input("Gissa ett tal: "))
#                 if gissningar in range(10) and gissningar not in spelarens_gissningar:
#                     spelarens_gissningar.append(gissningar)
#                 else:
#                     print("Ogiltigt tal. Vänligen gissa ett unikt tal:")
#             except ValueError:
#                 print("Var god och ange ett giltigt heltal.")

#         for nummer in range(len(spelets_gissningar)):
#             if spelarens_gissningar[nummer] == spelets_gissningar[nummer]:
#                 rätt_position += 1
#             elif spelarens_gissningar[nummer] in spelets_gissningar:
#                 fel_position += 1

#         if rätt_position == 3:
#             print(f"Grattis, du klarade spelet, på {försök + 1} försök!")
#             break

#         elif fel_position > 0 and rätt_position > 0:
#             print(f"Du gissade {fel_position} siffror rätt, men på fel position och {rätt_position} siffror på rätt position.")
        
#         elif rätt_position > 0:
#             print(f"Du gissade {rätt_position} siffror på rätt position.")

#         elif fel_position > 0:
#             print(f"Du gissade {fel_position} siffror rätt, men på fel position.")

#         elif fel_position == 0 and rätt_position == 0:
#             print("Du gissade inga siffror rätt.")

#         försök += 1  # Increment the attempt count after each round

#     svar = input("Vill du spela igen? (ja/nej): ").lower()
    
#     if svar == "ja":
#         spelets_gissningar = game_guess()  
#         play_game()
#     elif svar == "nej":  
#         print("Programmet avslutas.") 
#         exit()

# play_game()

#------------------------------- Mitt försök på chatgpts, blev fel


# import random

# def game_guess():

#     digits = list(range(10))
#     random.shuffle(digits)
#     return digits[:3]

# def try_again():

#     for i in range(3):
#        gissningar = int(input("Gissa ett tal"))
#        spelarens_gissningar.append(gissningar)

# def end_game():
#     exit()
   

# spelarens_gissningar = []
# spelets_gissningar = game_guess()


# def play_game():

#     global spelets_gissningar
#     print(spelets_gissningar)

#     rätt_position = 0
#     fel_position = 0
#     försök = 0
    
    

#     while True:

#         spelarens_gissningar.clear()
#         rätt_position = 0
#         fel_position = 0
#         försök = 1

       

#         for i in range(3):
#           gissningar = int(input("Gissa ett tal"))
#           spelarens_gissningar.append(gissningar)


#         for nummer in range(len(spelets_gissningar)):
#             if spelarens_gissningar[nummer] == spelets_gissningar[nummer]:
#                 rätt_position += 1
                
#             elif spelarens_gissningar[nummer] in spelets_gissningar:
#                 fel_position  += 1
                


#         if rätt_position == 3:
#              if försök == 1:
#                 print(f"Grattis, du klarade spelet, på {försök + 1} försök")
               
#                 break
             

#              elif försök > 0:
#                 print(f"Grattis, du klarade spelet, på {försök} försök")
#                 spelarens_gissningar.clear()
#                 rätt_position = 0
#                 fel_position = 0
#                 försök = 0
#                 break
            
     
#         elif fel_position > 0 and rätt_position >0:
#            print(f" Du gissade {fel_position} siffror rätt, men på fel position och {rätt_position} siffror på rätt position ")
          

#         elif rätt_position > 0:
#            print(f" Du gissade {rätt_position} siffror på rätt position")
          

#         elif fel_position > 0:
#            print(f" Du gissade {fel_position} siffror rätt, men på fel position")
          

#         elif fel_position and rätt_position == 0:
#            print(f" Du gissade inga siffror rätt")

#         försök += 1
       


#     svar = input("Vill du spela igen, (ja), (nej)").lower()
    

#     if svar == "ja":
#      spelets_gissningar = game_guess()  
#      spelarens_gissningar.clear()
#      play_game()
        
#     if svar == "nej":  
#      print("Programmet avslutas") 
#      exit()
        

# play_game()