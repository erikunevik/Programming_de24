# Skapar en tom dictionary för att lagra konton och saldon
bank = {}

while True:

    # Visa menyn
    print("\nVälj ett alternativ:")
    print("1. Skapa konto")
    print("2. Ta bort konto")
    print("3. Lista alla kontonummer")
    print("4. Lista totalsaldo")
    print("5. Lista alla kontonummer och saldo")
    print("6. Avsluta")
    # print(bank)
    
    val = input("Ange ditt val: ")
    
    if val == "1":  # Skapa konto
        kontonummer = input("Ange kontonummer: ")
        if kontonummer in bank:
            print("Kontot finns redan.")
        else:
            saldo = float(input("Ange startsaldo: "))
            bank[kontonummer] = saldo  # Lägg till kontonummer och saldo i dictionaryn
            #Dict[key] = value
            print(f"Konto {kontonummer} har skapats med saldo {saldo}.")
    
    elif val == "2":  # Ta bort konto
        kontonummer = input("Ange kontonummer att ta bort: ")
        if kontonummer in bank:
            del bank[kontonummer]  # Ta bort kontot från dictionaryn
            print(f"Konto {kontonummer} har tagits bort.")
        else:
            print("Kontot finns inte.")
    
    elif val == "3":  # Lista alla kontonummer
        if bank:
            print("Alla kontonummer:")
            for kontonummer in bank:
                print(kontonummer)  # Skriv ut alla kontonummer (nycklarna i dictionaryn)
        else:
            print("Inga konton finns.")
    
    elif val == "4":  # Lista totalsaldo
        totalsaldo = sum(bank.values())  # Summera alla värden i dictionaryn
        print(f"Totalt saldo för alla konton: {totalsaldo} SEK")
    
    elif val == "5":  # Lista alla kontonummer och saldo
        if bank:
            print("Kontonummer och saldo:")
            for kontonummer, saldo in bank.items():  # Iterera över nycklar och värden i dictionaryn
                print(f"Konto {kontonummer}: {saldo} SEK")
        else:
            print("Inga konton finns.")
    
    elif val == "6":  # Avsluta programmet
        print("Avslutar programmet...")
        break
    
    else:
        print("Ogiltigt val, försök igen.")