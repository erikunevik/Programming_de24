
# marp = 100
# vesp = 110
# funp = 125
# kebp = 135

# marpl =80
# vespl = 90
# funpl = 110
# kebpl = 115

# jalp = 10
# ostp = 10
# bacp = 10
# olip = 10

# ekebp = 25
# eskip = 25



# tid = input("Vilken tid på dagen kommer du vilja äta pizza, lunch (L) eller annan tid på dagen (A)?")

# if tid == "L":
#     vilken_pizzal = (input("vilken pizza vill du ha? Margherita (marpl), Vesuvio (vespl), Funghi (funpl) eller Kebabpizza(kebpl)?"))
    
#     if vilken_pizzal == "kebpl":
#        ejviktig=input("Vill du ha röd eller vit sås till?")
       
#        tillbehörp = input("Välj ett tillbehör, när du är klar tryck klar (K), Jalapenos (jalp), Extra ost (eost), bacon (bac), oliver (oli)")
#        while tillbehörp != "K":
#         tillbehörp = input("Välj ett tillbehör, när du är klar tryck klar (K), Jalapenos (jalp), Extra ost (eost), bacon (bac), oliver (oli)")

#         vilkenpizzal = 


#        print(f"Det kommer kosta dig {vilken_pizzal + tillbehörp}")

# Feeeeeel jag är ingen haxxxxorrrr

# Nytt försök, allt bra frutom fel intendentation

# while True:

#     val_rätt = input("Vilken rätt skulle du vilja äta: pizza, korv, hamburgare, kebab/falafel, grill eller vegetariskt?, tryck (Q) för att avsluta")

 
#      if val_rätt == "korv":
   
#            korv = 20
#             korv_tillbehör = 0

#             while True:

#               topping = input("Vad vill du ha extra på din korv, rostad lök (rl) eller räksallad (rs)? Om du inte vill ha något mer på, tryck (K)")

#               if topping== "K":
#                break
#                elif topping == "rl":
#               korv_tillbehör += 5
#               elif topping == "rs":
#                 korv_tillbehör += 15

#               slutpris_korv = korv + korv_tillbehör
#                print(f"Priset blir {slutpris_korv} kronor")
   
#      elif val_rätt == "pizza":

#       pizzaprisl = 0
#       pizzapris = 0
#       tillbehörpris = 0
#       tillbehör2pris = 0

#       tid = input("Vilken tid på dagen kommer du vilja äta pizza, lunch (L) eller annan tid på dagen (A)?")

#       if tid == "L": 
#        vilken_pizzal = (input("vilken pizza vill du ha? Margherita (marpl), Vesuvio (vespl), Funghi (funpl) eller Kebabpizza(kebpl)?"))

#        if vilken_pizzal == "marpl":
#          pizzaprisl = +- 80
#        elif vilken_pizzal == "vespl":
#          pizzaprisl = +- 90
#        elif vilken_pizzal == "funpl":
#          pizzaprisl = +- 110 
#        elif vilken_pizzal == "kebpl":
#          pizzaprisl = +- 115

#          if vilken_pizzal == "kebpl":
#              ejviktig=input("Vill du ha röd eller vit sås till?")


#      elif tid == "A":

#       vilken_pizza = (input("vilken pizza vill du ha? Margherita (marp), Vesuvio (vesp), Funghi (funp) eller Kebabpizza(kebp)?"))

#       if vilken_pizza == "marp":
#          pizzapris = +- 100
#       elif vilken_pizza == "vesp":
#          pizzapris = +- 110
#       elif vilken_pizza == "funp":
#          pizzapris = +- 115 
#       elif vilken_pizzal == "kebp":
#          pizzapris = +- 125

#          if vilken_pizzal == "kebp":
#              ejviktig=input("Vill du ha röd eller vit sås till?")

#      while True: 

#       tillbehörp = input("Välj ett tillbehör, när du är klar tryck klar (K), Jalapenos (jalp), Extra ost (eostp), bacon (bacp), oliver (olip)")
#       if tillbehörp == "K":
#        break
#       elif tillbehörp == "jalp":
#        tillbehörpris = +- 10
#       elif tillbehörp == "eostp":
#        tillbehörpris = +- 10
#       elif tillbehörp == "bacp":
#        tillbehörpris = +- 10
#       elif tillbehörp == "olip":
#        tillbehörpris = +- 10

#      while True:
 
#        tillbehörp2 = input ("Vill du extra skinka eller kebab på? när du är klar tryck klar (K), skinka (ski), Extra kebab (ekebp)")
#        if tillbehörp2 == "K": 
#         break
#        elif tillbehörp2 == "ski":
#         tillbehör2pris = +- 25
#        elif tillbehörp == "ekebp":
#         tillbehör2pris = +- 25
 
#      if tid == "L":
#       total_pris = pizzaprisl + tillbehörpris + tillbehör2pris
#       print (f"Det kommer kosta dig {total_pris} kronor")

#      elif tid == "A":
#       total_pris = pizzapris + tillbehörpris + tillbehör2pris
#       print (f"Det kommer kosta dig {total_pris} kronor")

#  elif val_rätt == "Q":
#     break
#     ("Print nu avslutas programmet")


# Här kommer min från chatgpt med rätt intendentation:

while True:
    val_rätt = input("Vilken rätt skulle du vilja äta: pizza, korv, hamburgare, kebab/falafel, grill eller vegetariskt? (tryck Q för att avsluta): ")

    if val_rätt == "korv":
        korv = 20
        korv_tillbehör = 0

        while True:
            topping = input("Vad vill du ha extra på din korv, rostad lök (rl) eller räksallad (rs)? Om du inte vill ha något mer på, tryck (K): ")

            if topping == "K":
                break
            elif topping == "rl":
                korv_tillbehör += 5
            elif topping == "rs":
                korv_tillbehör += 15

        slutpris_korv = korv + korv_tillbehör
        print(f"Priset blir {slutpris_korv} kronor")
    
    elif val_rätt == "pizza":
        pizzaprisl = 0
        pizzapris = 0
        tillbehörpris = 0
        tillbehör2pris = 0

        tid = input("Vilken tid på dagen kommer du vilja äta pizza, lunch (L) eller annan tid på dagen (A)? ")

        if tid == "L":
            vilken_pizzal = input("Vilken pizza vill du ha? Margherita (marpl), Vesuvio (vespl), Funghi (funpl) eller Kebabpizza (kebpl)? ")

            if vilken_pizzal == "marpl":
                pizzaprisl = 80
            elif vilken_pizzal == "vespl":
                pizzaprisl = 90
            elif vilken_pizzal == "funpl":
                pizzaprisl = 110
            elif vilken_pizzal == "kebpl":
                pizzaprisl = 115

                if vilken_pizzal == "kebpl":
                    ejviktig = input("Vill du ha röd eller vit sås till? ")

        elif tid == "A":
            vilken_pizza = input("Vilken pizza vill du ha? Margherita (marp), Vesuvio (vesp), Funghi (funp) eller Kebabpizza (kebp)? ")

            if vilken_pizza == "marp":
                pizzapris = 100
            elif vilken_pizza == "vesp":
                pizzapris = 110
            elif vilken_pizza == "funp":
                pizzapris = 115
            elif vilken_pizza == "kebp":
                pizzapris = 125

                if vilken_pizza == "kebp":
                    ejviktig = input("Vill du ha röd eller vit sås till? ")

        while True:
            tillbehörp = input("Välj ett tillbehör, när du är klar tryck klar (K), Jalapenos (jalp), Extra ost (eostp), bacon (bacp), oliver (olip): ")
            if tillbehörp == "K":
                break
            elif tillbehörp == "jalp":
                tillbehörpris += 10
            elif tillbehörp == "eostp":
                tillbehörpris += 10
            elif tillbehörp == "bacp":
                tillbehörpris += 10
            elif tillbehörp == "olip":
                tillbehörpris += 10

        while True:
            tillbehörp2 = input("Vill du extra skinka eller kebab på? När du är klar tryck klar (K), skinka (ski), Extra kebab (ekebp): ")
            if tillbehörp2 == "K":
                break
            elif tillbehörp2 == "ski":
                tillbehör2pris += 25
            elif tillbehörp2 == "ekebp":
                tillbehör2pris += 25

        if tid == "L":
            total_pris = pizzaprisl + tillbehörpris + tillbehör2pris
            print(f"Det kommer kosta dig {total_pris} kronor")
        elif tid == "A":
            total_pris = pizzapris + tillbehörpris + tillbehör2pris
            print(f"Det kommer kosta dig {total_pris} kronor")

    elif val_rätt == "Q":
        print("Programmet avslutas")
        break

# while True:  # Infinite loop to keep asking for a dish
#     val_rätt = input("Vilken rätt skulle du vilja äta: pizza, korv, hamburgare, kebab/falafel, grill eller vegetariskt? (tryck Q för att avsluta): ")

#     if val_rätt == "korv":
#         korv = 20
#         korv_tillbehör = 0

#         while True:
#             topping = input("Vad vill du ha extra på din korv, rostad lök (rl) eller räksallad (rs)? Om du inte vill ha något mer på, tryck (K): ")

#             if topping == "K":
#                 break
#             elif topping == "rl":
#                 korv_tillbehör += 5
#             elif topping == "rs":
#                 korv_tillbehör += 15
#             else:
#                 print("Ogiltigt val, försök igen.")

#         slutpris_korv = korv + korv_tillbehör
#         print(f"Priset blir {slutpris_korv} kronor")

#     elif val_rätt == "pizza":
#         pizzaprisl = 0
#         pizzapris = 0
#         tillbehörpris = 0
#         tillbehör2pris = 0

#         tid = input("Vilken tid på dagen kommer du vilja äta pizza, lunch (L) eller annan tid på dagen (A)? ")

#         if tid == "L":
#             vilken_pizza = input("Vilken pizza vill du ha? Margherita (marpl), Vesuvio (vespl), Funghi (funpl) eller Kebabpizza (kebpl)?")

#             if vilken_pizza == "marpl":
#                 pizzaprisl = 80
#             elif vilken_pizza == "vespl":
#                 pizzaprisl = 90
#             elif vilken_pizza == "funpl":
#                 pizzaprisl = 110
#             elif vilken_pizza == "kebpl":
#                 pizzaprisl = 115
#                 ejviktig = input("Vill du ha röd eller vit sås till?")

#         elif tid == "A":
#             vilken_pizza = input("Vilken pizza vill du ha? Margherita (marp), Vesuvio (vesp), Funghi (funp) eller Kebabpizza (kebp)?")

#             if vilken_pizza == "marp":
#                 pizzapris = 100
#             elif vilken_pizza == "vesp":
#                 pizzapris = 110
#             elif vilken_pizza == "funp":
#                 pizzapris = 115
#             elif vilken_pizza == "kebp":
#                 pizzapris = 125
#                 ejviktig = input("Vill du ha röd eller vit sås till?")

#         while True:
#             tillbehörp = input("Välj ett tillbehör, när du är klar tryck klar (K), Jalapenos (jalp), Extra ost (eostp), bacon (bacp), oliver (olip): ")
#             if tillbehörp == "K":
#                 break
#             elif tillbehörp == "jalp":
#                 tillbehörpris += 10
#             elif tillbehörp == "eostp":
#                 tillbehörpris += 10
#             elif tillbehörp == "bacp":
#                 tillbehörpris += 10
#             elif tillbehörp == "olip":
#                 tillbehörpris += 10
#             else:
#                 print("Ogiltigt val, försök igen.")

#         while True:
#             tillbehörp2 = input("Vill du extra skinka eller kebab på? När du är klar tryck klar (K), skinka (ski), Extra kebab (ekebp): ")
#             if tillbehörp2 == "K":
#                 break
#             elif tillbehörp2 == "ski":
#                 tillbehör2pris += 25
#             elif tillbehörp2 == "ekebp":
#                 tillbehör2pris += 25
#             else:
#                 print("Ogiltigt val, försök igen.")

#         if tid == "L":
#             total_pris = pizzaprisl + tillbehörpris + tillbehör2pris
#             print(f"Det kommer kosta dig {total_pris} kronor")
#         elif tid == "A":
#             total_pris = pizzapris + tillbehörpris + tillbehör2pris
#             print(f"Det kommer kosta dig {total_pris} kronor")

#     elif val_rätt == "Q":
#         print("Tack för din beställning! Programmet avslutas.")
#         break  # Exit the infinite loop and end the program

#     else:
#         print("Ogiltigt val, försök igen.")

