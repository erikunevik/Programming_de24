

# # Övning 1

# numbers = []


# for i in range(4):
#     num = int(input(f"Ange tal {i+1}"))
#     numbers.append(num)

# max_number = max(numbers)

# print(f"Det största talet är: {max_number}")

# #--------------------------------------------

# # Övning 2

# numbers = []
# for i in range(3):
#     num = int(input(f"Ange tal {i+1}: "))
#     numbers.append(num)


# max_value = max(numbers)
# min_value = min(numbers)


# sorted_numbers = sorted(numbers)
# median = sorted_numbers[1]

# #--------------------------------------------

# # Övning 3

# numbers = [12, 25, 37, 77, 89, 90, 91, 92, 93, 99]

# guess = int(input("Giss ett heltal mellan 1 till 100: "))

# if guess in numbers:
#     print("Ha, vilken tur du har, du gissade rätt! Är en på 10 att det sker!")
# else:
#     print("Aj då, bättre lycka nästa gång!")

# #--------------------------------------------

# # Övning 4

# favoritdjur = ["katt", "hund", "häst", "fågel", "ko"]

# användardjur = input("Ange dina tre favoritdjur, separerade med kommatecken: ").lower().split(',')

# användardjur = [djur.strip() for djur in användardjur]

# gemensamma = 0
# for djur in användardjur:
#     if djur in favoritdjur:
#         gemensamma += 1

# print(f"Ni har {gemensamma} gemansamma djur.")


#--------------------------------------------

# Uppgift 5

# shopping_list = []

# while True:
#     # Menyn
#     print("\nVälj ett alternativ:")
#     print("1. Add (Lägg till vara)")
#     print("2. Remove (Ta bort vara)")
#     print("3. Edit (Redigera vara)")
#     print("4. Print shopping list (Skriv ut shoppinglistan)")
#     print("5. Insert (Sätt in vara på viss plats)")
#     print("6. Reversed (Skriv ut listan baklänges)")
#     print("7. Sorted (Skriv ut listan sorterad)")
#     print("8. Delete shopping list (Radera hela listan)")
#     print("0. Exit (Avsluta)")
    
#     # Val från användaren
#     choice = input("\nAnge ditt val: ")
    
#     if choice == "1":
#         # Add: Lägg till vara
#         item = input("Ange vara att lägga till: ")
#         shopping_list.append(item)
#         print(f"{item} har lagts till i listan.")
    
#     elif choice == "2":
#         # Remove: Ta bort vara
#         item = input("Ange vara att ta bort: ")
#         if item in shopping_list:
#             shopping_list.remove(item)
#             print(f"{item} har tagits bort från listan.")
#         else:
#             print(f"{item} finns inte i listan.")
    
#     elif choice == "3":
#         # Edit: Redigera vara
#         item = input("Ange vara att redigera: ")
#         if item in shopping_list:
#             new_item = input(f"Ange nytt namn för {item}: ")
#             index = shopping_list.index(item)
#             shopping_list[index] = new_item
#             print(f"{item} har ändrats till {new_item}.")
#         else:
#             print(f"{item} finns inte i listan.")
    
#     elif choice == "4":
#         # Print shopping list: Skriv ut listan
#         if shopping_list:
#             print("\nShoppinglista:")
#             for idx, item in enumerate(shopping_list, start=1):
#                 print(f"{idx}. {item}")
#         else:
#             print("Shoppinglistan är tom.")
    
#     elif choice == "5":
#         # Insert: Sätt in vara på viss plats
#         item = input("Ange vara att sätta in: ")
#         position = int(input("Ange position (1 för att sätta in i början): ")) - 1
#         if 0 <= position <= len(shopping_list):
#             shopping_list.insert(position, item)
#             print(f"{item} har lagts till på position {position + 1}.")
#         else:
#             print("Ogiltig position.")
    
#     elif choice == "6":
#         # Reversed: Skriv ut listan baklänges
#         if shopping_list:
#             print("\nShoppinglista (baklänges):")
#             for item in reversed(shopping_list):
#                 print(item)
#         else:
#             print("Shoppinglistan är tom.")
    
#     elif choice == "7":
#         # Sorted: Skriv ut listan sorterad
#         if shopping_list:
#             print("\nShoppinglista (sorterad):")
#             for item in sorted(shopping_list):
#                 print(item)
#         else:
#             print("Shoppinglistan är tom.")
    
#     elif choice == "8":
#         # Delete shopping list: Radera hela listan
#         confirm = input("Är du säker på att du vill radera hela listan? (ja/nej): ")
#         if confirm.lower() == "ja":
#             shopping_list.clear()
#             print("Shoppinglistan har raderats.")
#         else:
#             print("Shoppinglistan raderades inte.")
    
#     elif choice == "0":
#         # Exit: Avsluta programmet
#         print("Avslutar programmet...")
#         break
    
#     else:
#         print("Ogiltigt val, försök igen.")