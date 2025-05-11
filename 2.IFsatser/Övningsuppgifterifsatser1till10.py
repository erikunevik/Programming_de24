# tal=int(input(" välj ett tal"))
# if tal > 10 :
#     print ("talet är större än 10")
# elif tal < 10:
#      print("talet är mindre 10 ")

# uppgift nr 2
# antal = int(input("hur många mjölk paket finns det kvar"))
# if antal < 10:
#  print("beställ 30 paket")
# elif antal>=10 and antal <=20:
#  print ("beställ 20 paket ")
# else:
#  print("du behöver inte beställa mer ")

# Uppgift 3

# tal1 = int(input("Number 1"))
# tal2 = int(input("Number 2"))

# if tal1 > tal2:
#     print("largest")
# elif tal2 > tal1:
#     print("laergest")
# print("Det största talet är largest")

#Uppgift 4

# tal1 = int(input("Number 1"))
# tal2 = int(input("Number 2"))
# tal3 = int(input("Number 3"))

# if  tal2 <tal1> tal3:
#     print("Tal 1 är largest")
# elif tal2 > tal1 and tal3:
#     print("Tal 2 är laergest")
# elif tal3 > tal1 and tal2:
#     print("Tal 3 är laergest")

# print("Det största talet är largest")

# kategori= input ("ange kategori ( vuxen, student, pensionär): ")
# if  kategori == "pensionär" or kategori == "student":
#     print("resan kostar 20kr")
# elif kategori== ("vuxen"):
#     print("resan kostar 30kr")

# else:
#     print ("du har valt en felaktig kategori ")

#uppgift nr 6

# ålder = int(input("vilket år föddes du "))
# if ålder >= 1980 and ålder < 1990:
#     print( "du är född under 80 talet ")
# elif ålder >= 1990 and ålder < 2000:
#     print( "du är född under 90 talet ")
# else:
#     print("du är inte född på 1990 eller 1980")

#7

# land= input("Vilket land kommer du ifrån?")
# sverige = "sverige"
# norge = "norge"
# danmark = "danmark"
# if land == sverige:
#     print("Du bor i skandinavien")
# elif land == norge:
#     print("Du bor i skandinavien")
# elif land == danmark:
#     print("Du bor i skandinavien")
# else:
#     print("Du bor i ett annat land utanför skandivaien")

#8
# pengar = int(input("Skriv i hur mycket pengar du har"))
# rabatt = (input("Om du har du rabatt, skriv ja. Om du inte har rabatt, skriv nej"))
# nej = "nej"
# ja = "ja"
# if rabatt == nej and 25 >= pengar > 15 and pengar:
#     print("Du kan köpa en liten hamburgare")
# elif rabatt == ja and 25 >= pengar > 15:
#     print("Du kan köpa en liten hamburgare och en pommes frites")
# elif rabatt == nej and 50 >= pengar >  25:
#     print("Du kan köpa en stor hamburgare")
# elif rabatt == ja and 50 >= pengar >  25:
#     print("Du kan köpa en stor hamburgare och pommes frites")
# elif pengar > 60 or pengar == 50 or 60 and rabatt==ja:
#     print("Du kan köpa ett meal med dryck")

# else:
#     print("Du har matat in fel")

9

# from statistics import fmean


# svedala = float(input("Skriv in hur varmt det är i svedala"))
# jukka = float(input("Skriv in hur varmt det är i jukkasjärvi"))
# visby = float(input("Skriv in hur varmt det är i visby"))
# mean = fmean((svedala, jukka, visby))

# if  svedala >= visby and jukka >= visby:
#     print(f"Det är kallast i visby, {visby} grader, medeltemperaturen är {mean}")
# elif visby >= svedala and jukka >= svedala:
#     print(f"Det är kallast i svedala, {svedala} grader, medeltemperaturen är {mean}")
# elif visby >= jukka and svedala >= jukka:
#     print(f"Det är kallast i jukkasjärvi, {jukka}  grader, medeltemperaturen är {mean}")

    
# if  visby > svedala and visby > jukka:
#     print(f"Och det är varmast i visby, {visby} grader, medeltemperaturen är {mean}")
# elif svedala > visby and svedala > jukka:
#     print(f"Det är varmast i svedala, {svedala} grader, medeltemperaturen är {mean}")
# elif jukka > visby and jukka > svedala:
#     print(f"Det är varmast i jukkasjärvi, {jukka}  grader, medeltemperaturen är {mean}")

# 10

# lösen = (input("Mata in ett lösenord som är minst 8 tecken långt"))

# if len(lösen) >= 8:
#     print("Lösenordet är skapat")
# else:
#     print("Lösenordet uppfyller inte kraven")




