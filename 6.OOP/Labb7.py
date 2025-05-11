# class Matratt:
#     def __init__(self, namn, pris, typ, kalorier):
#         self.namn = namn
#         self.pris = pris
#         self.typ = typ
#         self.kalorier = kalorier
    
#     def __str__(self):
#         return f"{self.namn} ({self.typ}) - {self.kalorier} kcal: {self.pris} kr"

# ratt1 = Matratt("Vegetarisk Lasagne", 85, "Vegetarisk", 600)
# ratt2 = Matratt("Köttbullar med Potatismos", 95, "Kött", 800)

# lista = [ratt1, ratt2]

# print("Dagens Lunchmeny:")
# for i in lista:
#     print(i)

#----------------------------------

# Definiera klassen Person
class Person:
    def __init__(self, fodelsedatum):
        # Födelsedatum är obligatoriskt
        self.fodelsedatum = fodelsedatum
        # Övriga attribut kan sättas senare
        self.namn = None
        self.gatuadress = None
        self.postnummer = None
        self.postort = None

    # Property för namn (Get)
    @property
    def namn(self):
        return self._namn
    
    # Setter för namn
    @namn.setter
    def namn(self, namn):
        self._namn = namn
    
    # Property för gatuadress
    @property
    def gatuadress(self):
        return self._gatuadress
    
    # Setter för gatuadress
    @gatuadress.setter
    def gatuadress(self, gatuadress):
        self._gatuadress = gatuadress

    # Property för postnummer
    @property
    def postnummer(self):
        return self._postnummer
    
    # Setter för postnummer
    @postnummer.setter
    def postnummer(self, postnummer):
        self._postnummer = postnummer
    
    # Property för postort (Get)
    @property
    def postort(self):
        return self._postort
    
    # Setter för postort
    @postort.setter
    def postort(self, postort):
        self._postort = postort
    
    # Metod för att byta namn
    def namnge(self, nytt_namn):
        self.namn = nytt_namn

    # Metod för att byta adress
    def byt_adress(self, ny_gatuadress, nytt_postnummer, ny_postort):
        self.gatuadress = ny_gatuadress
        self.postnummer = nytt_postnummer
        self.postort = ny_postort

    # Metod för att skriva ut information om personen
    def visa_info(self):
        return f"Person: {self.namn}, Födelsedatum: {self.fodelsedatum}, Adress: {self.gatuadress}, {self.postnummer}, {self.postort}"

# Skapa två personer
person1 = Person("1990-05-12")
person2 = Person("1988-08-23")

# Namnge personerna
person1.namnge("Anna Andersson")
person2.namnge("Erik Svensson")

# Sätt adresser för båda
person1.byt_adress("Storgatan 12", "12345", "Stockholm")
person2.byt_adress("Lillgatan 5", "54321", "Göteborg")

# Skriv ut information om båda personerna
print(person1.visa_info())
print(person2.visa_info())

# Låt Erik flytta in hos Anna
person2.byt_adress(person1.gatuadress, person1.postnummer, person1.postort)

# Skriv ut information efter flytten
print("\nEfter flytten:")
print(person1.visa_info())
print(person2.visa_info())
