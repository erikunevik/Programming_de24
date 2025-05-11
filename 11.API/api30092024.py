
# import requests


# # Get (URL)

# # Status kod

# # Om ok -> konvertera till json
# # Om ej ok -> error

# # Get request för att hämta

# response = requests.get("")

# if response.status_code == 200:

#     products = response.json() # Konvertera till json
#     print(f"All products; {products}") # Visa alla produkter

# else:
#     print(f"Error fetching products. status code: {response.status_code}")


#-------------------------------------------------------------

# Uppgift 1

# # 1:1




# while True:

#     print("Meny\n")
#     print ("(1) Visa alla produkter")
#     print("(2) Visa produktdetaljer")
#     print("(3) Lägg till en ny produkt")
#     print("(4) Avsluta")


#     val = input("Gör dit val:")
#     if val == "1":

#         import requests


# # Get (URL)

# # Status kod

# # Om ok -> konvertera till json
# # Om ej ok -> error

# # Get request för att hämta

#     response = requests.get("https://fakestoreapi.com/products")

#     if response.status_code == 200:

#         products = response.json() # Konvertera till json
#         # print(f"All products; {products}") # Visa alla produkter

#         for product in products:
#             print(product["title"])






#     elif val == "2":

#         import requests

#         id = input("Ange id på produkten:")
#         response = requests.get(f"https://fakestoreapi.com/products/{id}")# Get request för att hämta data från en server
#         if response.status_code == 200:
#             product = response.json()
#             print(product)


   


# # #     elif val == "3":
# # #    #   print(konto_lista.keys())

# # #        for i in (konto_lista):
# # #            print (i)

# # #        enter = input("Press enter to return to the main menu\n").lower()


# # #     elif val == "4":
# # #         print(sum(konto_lista.values()))

# # #         enter = input("Press enter to return to the main menu\n").lower()

# # #     elif val == "5":

# # #           for i, saldo in konto_lista.items():
# # #            print (f"kontonummer: {i} saldo: {saldo}")

# # #           enter = input("Press enter to return to the main menu\n").lower()


#     else:
#         print(f"Error fetching products. status code: {response.status_code}")









#---------------------------------------

 

# import requests  # Import requests at the top

# while True:
#     # Display the menu
#     print("Meny\n")
#     print("(1) Visa alla produkter")
#     print("(2) Visa produktdetaljer")
#     print("(3) Lägg till en ny produkt")
#     print("(4) Avsluta")

#     val = input("Gör ditt val: ")

#     # Option 1: Show all products
#     if val == "1":
#         # Make a GET request to the Fakestore API
#         response = requests.get("https://fakestoreapi.com/products")

#         # Check if the request was successful
#         if response.status_code == 200:
#             products = response.json()  # Convert response to JSON

#             # Print the title of each product
#             print("Alla produkter:")
#             for product in products:
#                 print(product["title"])
#         else:
#             print(f"Error fetching products. Status code: {response.status_code}")

#     # Option 2: Show product details
#     elif val == "2":
#         id = input("Ange id på produkten: ")
#         response = requests.get(f"https://fakestoreapi.com/products/{id}")

#         # Check if the request was successful
#         if response.status_code == 200:
#             product = response.json()  # Convert response to JSON
#             print(f"Produktdetaljer: {product}")
#         else:
#             print(f"Error fetching product details. Status code: {response.status_code}")


#     elif val == "3":

#         url = "https://fakestoreapi.com/products"

#         id = input("Lägg till en ny produkt: ")
#         title = input("Lägg till en titel: ")
#         price = input("Lägg till pris: ")
#         description = input("Lägg till beskrivning: ")
#         category = input("Lägg till kategori: ")
#         image = input("Lägg till bild: ")

#         payload =  {
                
#                 "title": title,
#                 "price": price,
#                 "description": description,
#                 "category": category,
#                 "image": image
#             }
        

#         print(payload)
       

#         response = requests.post(url, json = payload)# Post request för att lägga till en ny produkt

      

#         if response.status_code == 201:# Om statuskoden är 200 så är det ok

            
#             print("Produkten har lagts till")

           
        
        
#         else:
#             print(f"Error fetching product details. Status code: {response.status_code}")





#     # Option 4: Exit the program
#     elif val == "4":
#         print("Avslutar programmet...")
#         break  # Exit the loop and end the program

#     # Invalid input handling
#     else:
#         print("Ogiltigt val, försök igen.")




# ------------------------------------------


import requests

while True:
    # Display the menu
    print("Meny\n")
    print("(1) Visa alla produkter")
    print("(2) Visa produktdetaljer")
    print("(3) Lägg till en ny produkt")
    print("(4) Avsluta")

    val = input("Gör ditt val: ")

    if val == "1":

        response = requests.get("https://fakestoreapi.com/products")

        response_json = response.json()

        for products in response_json:
            print(products["title"])


    elif val == "2":

        id = int(input("Mata in ett ID:"))

        response = requests.get(f"https://fakestoreapi.com/products/{id}")

        id = response.json()

       
        print(id)

    elif val == "3":

     new_item = {}
    
     new_item["title"] = input("Lägg till en titel: ")
     new_item["price"] = input("Lägg till pris: ")
     new_item["description"] = input("Lägg till beskrivning: ")
     new_item["category"] = input("Lägg till kategori: ")
     new_item["image"] = input("Lägg till bild: ")
    
     
     response = requests.post("https://fakestoreapi.com/products", json=new_item)
    
     
     if response.status_code == 200 or response.status_code == 201:
        print("New item added successfully!")
     else:
        print(f"Failed to add item. Status code: {response.status_code}")

     print(new_item)
     print(response.status_code)
     print(response.json())  


    elif val == "4":
        print("Avslutar programmet...")
        break 

    
    else:
        print("Ogiltigt val, försök igen.")





      

       
   







    






    # elif val == "4":
    # print("Avslutar programmet...")
    # break  # Exit the loop and end the program

    # # Invalid input handling
    # else:
    # print("Ogiltigt val, försök igen.")
