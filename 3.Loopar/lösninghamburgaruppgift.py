totalpris = 0  # Tänk på utanför huvudloopen för att samla alla köp

while True: #Menyn körs om och om igen tills användaren säger annat
    print("Välkommen till Snabbmatskedjan!\n")
    print("Meny:")
    print("1. Hamburgare")
    print("2. Korv med bröd")
    print("3. Pizza")
    print("4. Kebab/falafel")
    print("5. Grill")
    print("6. Vegetariskt")

    # Användarens val
    val = int(input("\nVälj ett alternativ från menyn (1-6): "))

    if val == 1:
        while True:
            # Hamburgare
            print("\nHamburgare:")
            print("1. Vanlig burgare - 25 kr")
            print("2. Ostburgare - 39 kr")
            print("3. Dubbelburgare - 55 kr")

            burgarval = int(input("Välj hamburgare (1-3): "))
            if burgarval == 1:
                totalpris += 25
            elif burgarval == 2:
                totalpris += 39
            elif burgarval == 3:
                totalpris += 55

            vego_burgare = input("Vill du ha vegofärs? (ja/nej): ").lower()
            if vego_burgare == "ja":
                print("Vegoburgare vald.")

            gurka = input("Vill du ha gurka? (ja/nej): ").lower()
            if gurka == "ja":
                print("Gurka tillagd.")

            ketchup_senap = input("Vill du ha ketchup/senap? (ja/nej): ").lower()
            if ketchup_senap == "ja":
                print("Ketchup/senap tillagd.")
        
            # Fråga om användaren vill beställa fler burgare
            fler_burgare = input("Vill du lägga till fler burgare? (ja/nej): ").lower()
            if fler_burgare != "ja":
                break

    elif val == 2:
        # Korv med bröd
        print("\nKorv med bröd - 20 kr")
        totalpris += 20

        ketchup = input("Vill du ha ketchup? (ja/nej): ").lower()
        if ketchup == "ja":
            print("Ketchup tillagd.")

        senap = input("Vill du ha senap? (ja/nej): ").lower()
        if senap == "ja":
            print("Senap tillagd.")

        # Rostad lök med möjlighet att lägga till fler portioner
        rostad_lok = input("Vill du ha rostad lök (+5 kr)? (ja/nej): ").lower()
        while rostad_lok == "ja":
            totalpris += 5
            rostad_lok = input("Vill du ha mer rostad lök? (+5 kr) (ja/nej): ").lower()

        # Räksallad med möjlighet att lägga till fler portioner
        racksallad = input("Vill du ha räksallad (+15 kr)? (ja/nej): ").lower()
        while racksallad == "ja":
            totalpris += 15
            racksallad = input("Vill du ha mer räksallad? (+15 kr) (ja/nej): ").lower()

    elif val == 3:
        while True:  # Loopen för att hantera fler pizzabeställningar
            # Pizza
            print("\nPizza:")
            print("1. Margherita - 100 kr")
            print("2. Vesuvio - 110 kr")
            print("3. Funghi - 110 kr")
            print("4. Kebab pizza - 125 kr")
            print("5. Salami - 135 kr")

            pizzaval = int(input("Välj pizza (1-5): "))

            if pizzaval == 1:
                pizza_pris = 100
            elif pizzaval == 2:
                pizza_pris = 110
            elif pizzaval == 3:
                pizza_pris = 110
            elif pizzaval == 4:
                pizza_pris = 125
            elif pizzaval == 5:
                pizza_pris = 135

            lunchtid = input("Är det lunchtid? (ja/nej): ").lower()
            if lunchtid == "ja":
                if pizzaval == 1:
                    pizza_pris = 80
                elif pizzaval == 2:
                    pizza_pris = 90
                elif pizzaval == 3:
                    pizza_pris = 90
                elif pizzaval == 4:
                    pizza_pris = 110
                elif pizzaval == 5:
                    pizza_pris = 115

            totalpris += pizza_pris

            if pizzaval == 4:  # Kebab pizza
                vit_sas = input("Vill du ha vit sås? (ja/nej): ").lower()
                if vit_sas == "ja":
                    print("Vit sås tillagd.")
                rod_sas = input("Vill du ha röd sås? (ja/nej): ").lower()
                if rod_sas == "ja":
                    print("Röd sås tillagd.")

            # Lägg till extra ingredienser
            while True:
                print("\nExtra ingredienser (+10 kr per val):")
                print("1. Jalapeno")
                print("2. Extra ost")
                print("3. Bacon")
                print("4. Oliver")
                print("5. Kebab eller extra skinka (+25 kr)")

                extra_val = int(input("Välj en extra ingrediens (1-5), eller 0 för att avsluta: "))

                if extra_val == 1:
                    totalpris += 10
                    print("Jalapeno tillagd.")
                elif extra_val == 2:
                    totalpris += 10
                    print("Extra ost tillagd.")
                elif extra_val == 3:
                    totalpris += 10
                    print("Bacon tillagd.")
                elif extra_val == 4:
                    totalpris += 10
                    print("Oliver tillagd.")
                elif extra_val == 5:
                    totalpris += 25
                    print("Kebab eller extra skinka tillagd.")
                elif extra_val == 0:
                    break  # Avsluta loopen om användaren inte vill lägga till fler ingredienser
                else:
                    print("Ogiltigt val, vänligen försök igen.")

            # Visa totalpris för den specifika pizzabeställningen
            print(f"\nDin totala summa för pizzan är {totalpris} kr.\n")

            # Fråga om användaren vill beställa en till pizza
            fler_pizzor = input("Vill du beställa en till pizza? (ja/nej): ").lower()
            if fler_pizzor != "ja":
               break

    elif val == 4:
        while True:
            # Kebab/falafel
            print("\nKebab/falafel:")
            print("1. Falafel-tallrik - 95 kr")
            totalpris += 95

            ris = input("Vill du ha ris istället för pommes frites? (ja/nej): ").lower()
            if ris == "ja":
                print("Ris tillagd.")

            ta_bort_lok = input("Vill du ta bort löken? (ja/nej): ").lower()
            if ta_bort_lok == "ja":
                print("Lök borttagen.")

            rod_sas = input("Vill du ha röd sås? (ja/nej): ").lower()
            if rod_sas == "ja":
                print("Röd sås tillagd.")

            vit_sas = input("Vill du ha vit sås? (ja/nej): ").lower()
            if vit_sas == "ja":
                print("Vit sås tillagd.")

            # Fråga om användaren vill beställa en till kebab
            fler_kebab = input("Vill du beställa en till kebab? (ja/nej): ").lower()
            if fler_kebab != "ja":
                break

    elif val == 5:
        while True:
            # Grill
            print("\nGrill:")
            print("1. Lövbiff - 130 kr")
            print("2. Kycklingspett - 110 kr")
            print("3. Schnitzel - 120 kr")
            print("4. Chicken nuggets - 95 kr")
            print("5. Grillad kyckling - 115 kr")

            grillval = int(input("Välj grillalternativ (1-5): "))

            if grillval == 1:
                grill_pris = 130
            elif grillval == 2:
                grill_pris = 110
            elif grillval == 3:
                grill_pris = 120
            elif grillval == 4:
                grill_pris = 95
            elif grillval == 5:
                grill_pris = 115

            totalpris += grill_pris

            if grillval == 1:  # Lövbiff
                print("Välj sås:")
                print("1. Bearnaisesås")
                print("2. Vitlökssås")
                print("3. Vitlökssmör")
                sasval = int(input("Välj sås (1-3): "))
                print("Sås tillagd.")

                extra_lovbit = input("Vill du ha en extra lövbit (+50 kr)? (ja/nej): ").lower()
                if extra_lovbit == "ja":
                    totalpris += 50

            elif grillval == 3:  # Schnitzel
                print("Välj sås:")
                print("1. Remouladsås")
                print("2. Majonäs")
                sasval = int(input("Välj sås (1-2): "))
                print("Sås tillagd.")

            elif grillval == 4:  # Chicken nuggets
                print("Välj dipp:")
                print("1. Sweet and sour")
                print("2. BBQ")
                print("3. Taco")
                print("4. Vitlök")
                print("5. Szechuan")
                dippval = int(input("Välj dipp (1-5): "))
                print("Dipp tillagd.")

                extra_dipp = input("Vill du ha extra dipp (+5 kr)? (ja/nej): ").lower()
                if extra_dipp == "ja":
                    print("Välj dipp:")
                    print("1. Sweet and sour")
                    print("2. BBQ")
                    print("3. Taco")
                    print("4. Vitlök")
                    print("5. Szechuan")
                    dippval = int(input("Välj dipp (1-5): "))
                    print("Dipp tillagd.")
                    totalpris += 5

            elif grillval == 5:  # Grillad kyckling
                pommes_frites = input("Vill du ha pommes frites istället för ris? (ja/nej): ").lower()
                if pommes_frites == "ja":
                    print("Pommes frites tillagt.")

            # Fråga om användaren vill beställa en till grillrätt
            fler_grill = input("Vill du beställa en till grillrätt? (ja/nej): ").lower()
            if fler_grill != "ja":
                break

    elif val == 6:
        while True:
            # Vegetariskt
            print("\nVegetariskt:")
            print("1. Vegoburgare - 39 kr")
            print("2. Falafel - 45 kr")
            print("3. Vegansk pizza - 100 kr")

            vegoval = int(input("Välj vegetariskt alternativ (1-3): "))

            if vegoval == 1:
                vego_pris = 39
            elif vegoval == 2:
                vego_pris = 45
            elif vegoval == 3:
                vego_pris = 100

            totalpris += vego_pris
            
            # Fler vegorätt
            fler_vego = input("Vill du beställa en till vegorätt? (ja/nej): ").lower()
            if fler_vego != "ja":
                break

    else:
        print("Ogiltigt val, vänligen försök igen.")

    # Visa totalpris
    print(f"\nDin totala summa är {totalpris} kr.\n")

    # Fråga om användaren vill fortsätta
    fortsätta = input("Vill du beställa något annat? (ja/nej): ").lower()
    if fortsätta != "ja":
        print("Tack för ditt köp!")
        break