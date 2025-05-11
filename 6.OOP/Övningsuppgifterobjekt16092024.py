

# 1

# class Maträtt:

#     def __init__(self, namn, pris, typ, kalorier):
#         self.namn = namn
#         self.pris = pris
#         self.typ = typ
#         self.kalorier = kalorier
#     def __str__(self):
#       return f'{self.namn} kostar {self.pris} är {self.typ} innehåller {self.kalorier} kalorier'

# rätt1 = Maträtt('Korv Stroganoff', '135 SEK', "Kötträtt", "1000")
# rätt2 = Maträtt('Falafel', '120 SEK', 'Vegansk', "900")
# rätt3 = Maträtt('Fiskgryta', '145 SEK', 'Fisk', "900")

# matlista = [rätt1, rätt2, rätt3]

# for rätter in (matlista):
#    print(f"Dagens lunch är: {rätter}")

# 2

# class Personuppgifter:
#     def __init__(self, personnummer, namn, gatuadress, postnummer, postort):
#         self.personnummer = personnummer
#         self.namn = namn
#         self.gatuadress = gatuadress
#         self.postnummer = postnummer
#         self.postort = postort

#     def __str__(self):
#         return (f"Personnummer: {self.personnummer}, "
#                 f"Namn: {self.namn}, "
#                 f"Gatuadress: {self.gatuadress}, "
#                 f"Postnummer: {self.postnummer}, "
#                 f"Postort: {self.postort}")

#     def set_flytt(self, gatuadress, postnummer, postort):
#          self.gatuadress = gatuadress
#          self.postnummer = postnummer
#          self.postort = postort

#     def get_flytt(self):
#         return self.gatuadress, self.postnummer, self.postort


# p1 = Personuppgifter(9033445567, "Luca", "Plommonvägen 7", 16345, "Rågsved")
# p2 = Personuppgifter(8007246678, "Aleandro", "Malteholsmvägen 10", 98756, "Tranås")

# p2.set_flytt("Plommonvägen 7", 16345, "Rågsved")
# (p2.get_flytt())
# print(p2)

# --------------------------- Aladins lösning som var lite fel då jag ej hann med, chatgpts kommer efter. 

# class Person:
#     def __init__(self, fodelsedatum):
#         self.fodelsedatum = fodelsedatum
#         self.name = None
#         self.adress = None
#         self.postnummer = None
#         self.city = None

#     @property
#     def name(self):
#         return self.name

#     @name.setter # Behöve ej göra för fodelsedatum för den finns i konstruktorn
#     def postnummer(self, postnummer):
#         self.postnummer = postnummer

#     @property
#     def adress(self):
#         return self.adress
        

#     @name.setter # Behöve ej göra för fodelsedatum för den finns i konstruktorn
#     def city(self, city):
#         self.city = city
    
#     def namer(self, changeName):
#         self.name = changeName

#     def changeAdress(self, newAdress, newPostnummer, newCity):
#         self.adress = newAdress
#         self.postnummer = newPostnummer
#         self.city = newCity

#     def showInfo(self):
#         return f"Person {self.name}, Födelsedatum {self.fodelsedatum}, Adress: {self.adress}, Postnummer: {self.city}"
    
# person1 = Person("1990-05-12")
# person2 = Person("1988-08-23")

# #Namnge personen

# person1.namer("Anna Andersson")
# person2.namer("Erik Eriksson")

# # Sätt adress

# person1.changeAdress("Storgatan 12", "12345", "Stockholm")
# person2.changeAdress("Lillgatan 14", "6789", "Alingsås")

# # Print info

# print(person1.showInfo())
# print(person2.showInfo())

# # Erik flyttar in till Anna

# person2.changeAdress(person1.adress, person1.postnummer, person1.city)

# # Skriv ut info

# print("\nEfter flytten:")
# print(person1.showInfo())
# print(person2.showInfo())

#----------------------------------------------------------- Chatgpt

# class Person:
#     def __init__(self, fodelsedatum):
#         self._fodelsedatum = fodelsedatum
#         self._name = None
#         self._adress = None
#         self._postnummer = None
#         self._city = None

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value

#     @property
#     def adress(self):
#         return self._adress

#     @adress.setter
#     def adress(self, value):
#         self._adress = value

#     @property
#     def postnummer(self):
#         return self._postnummer

#     @postnummer.setter
#     def postnummer(self, value):
#         self._postnummer = value

#     @property
#     def city(self):
#         return self._city

#     @city.setter
#     def city(self, value):
#         self._city = value
    
#     def change_name(self, new_name):
#         self.name = new_name

#     def change_adress(self, new_adress, new_postnummer, new_city):
#         self.adress = new_adress
#         self.postnummer = new_postnummer
#         self.city = new_city

#     def show_info(self):
#         return f"Person: {self.name}, Födelsedatum: {self._fodelsedatum}, Adress: {self.adress}, Postnummer: {self.postnummer}, Stad: {self.city}"
    
# # Create instances of Person
# person1 = Person("1990-05-12")
# person2 = Person("1988-08-23")

# # Set names
# person1.change_name("Anna Andersson")
# person2.change_name("Erik Eriksson")

# # Set addresses
# person1.change_adress("Storgatan 12", "12345", "Stockholm")
# person2.change_adress("Lillgatan 14", "6789", "Alingsås")

# # Print info
# print(person1.show_info())
# print(person2.show_info())

# # Erik moves in with Anna
# person2.change_adress(person1.adress, person1.postnummer, person1.city)

# # Print info after the move
# print("\nEfter flytten:")
# print(person1.show_info())
# print(person2.show_info())



#------Polymorphism handlar om metodöverskuggning

# class Animal:
#     def speak(self):
#         return "ett ljud"
    
# class Dog(Animal): 
#     def speak(self):
#         return "voff"
    
# class Cat(Animal): 
#     def speak(self):
#         return "mjau"

    
# dog = Dog()
# cat = Cat()

# animals = [dog, cat]

# for animal in animals:
#     print(animal.speak())

# Outputen överskuggar något som är definerat i basklassen

#Ducktyping, klassen defineras utefter dess beteende, walks and talks like a duck then its a duck

# class Bird ():
#     def make_sound(self):
#         return "Ett ljud"
    
# class Duck(Bird):
#      def make_sound(self):
#         return "kvack"
    
# class Crow(Bird):
#      def make_sound(self):
#         return "kra"
     
# def let_bird_make_sound(bird):
#     return bird.make_sound()

# duck = Duck()
# crow = Crow()

# print(let_bird_make_sound(duck))
# print(let_bird_make_sound(crow))

              






# 2

# Aladins lösning -----------------------------------------------

# class Person:
#     def __init__(self, fodelsedatum):
#         self.fodelsedaturm = fodelsedatum
#         self.namn = ??? # Ska stå en typ som vi inte gått igenom
#         self.adress = ???





# Person1 = Personuppgifter(19561212)
# Person2 = Personuppgifter(19780618)

# Lista = [person1, person2]





# ## creating an object
# obj = SampleClass(10)

# ## getting the value of 'a' using get_a() method
# print(obj.get_a())

# ## setting a new value to the 'a' using set_a() method
# obj.set_a(45)






# print(Person1)


# class Circle:
#     pi = 3.14

#     # Cirklen initieras med en radie (standrad 1)
#     def _init_(self, radius=1):  # Konstruktor
#         self.radius = radius


#      # Metod för att räkna ut arean (tänk på self)
#     def area(self):
#         return self.radius * self.radius * Circle.pi # För att pi är lokal bunden till funktionen

#     # 2 to get

#     # Behöver en metod för att sätta radien

#     def setRadius(self, radius):
#         self.radius = radius

#         # Metod för att hämta radien

#     def getRadius(self):
#         return self.radius
    



#-----------------------

 # Eriks lösning på att räkna ut hypotenusan

# import math 

# class Hypotenusan:

#     def __init__(self, radius1 = 0, radius2 = 0):
#         self.radius1 = radius1
#         self.radius2 = radius2

#     def hypo(self):
#         return math.sqrt(self.radius1**2 + self.radius2**2)

#     def setradius1(self, radius1):
#         self.radius1 = radius1

#     def setradius2(self, radius2):
#         self.radius2 = radius2

#     def getradius1(self):
#         return self.radius1
    
#     def getradius2(self):
#         return self.radius2   

# kateter = Hypotenusan()    
# kateter.setradius1(9)
# kateter.setradius2(9)

# print(f"kateter 1 är", kateter.getradius1(), "och 2", kateter.getradius2())
# print(f"Hypotenusan är", kateter.hypo())


#-----------------------------------------------------------------------------

# import math 

# class Hypotenusan:
#     def __init__(self, radius1=0, radius2=0):
#         self.radius1 = radius1
#         self.radius2 = radius2

#     def hypo(self):
#         return math.sqrt(self.radius1**2 + self.radius2**2)

#     def setradius1(self, radius1):
#         self.radius1 = radius1

#     def setradius2(self, radius2):
#         self.radius2 = radius2

#     def getradius1(self):
#         return self.radius1
    
#     def getradius2(self):
#         return self.radius2

# # Use a single instance and set both radii
# kateter = Hypotenusan()
# kateter.setradius1(8)
# kateter.setradius2(8)

# print(f"kateter 1 är", kateter.getradius1(), "och 2", kateter.getradius2())
# print(f"Hypotenusan är", kateter.hypo())

# import math

# class Hypotenusan:
#     def __init__(self, radius1=0, radius2=0):
#         self.radius1 = radius1
#         self.radius2 = radius2

#     def hypo(self):
#         return math.sqrt(self.radius1**2 + self.radius2**2)  # Compute the actual hypotenuse

#     def setradius1(self, radius1):
#         self.radius1 = radius1

#     def setradius2(self, radius2):
#         self.radius2 = radius2

#     def getradius1(self):
#         return self.radius1
 
#     def getradius2(self):
#         return self.radius2

# kateter1 = Hypotenusan()
# kateter2 = Hypotenusan()
 
# kateter1.setradius1(2)
# kateter2.setradius2(11)

# print(f"kateter 1 är", kateter1.getradius1(), "och 2", kateter2.getradius2())
# print(f"Hypotenusan är", kateter2.hypo())  # Call the method on the instance







# #--------------------------------------

# #     def __init__(self, data:dict):  #Type hint, vill att du skrive en dictionary
# #         self.__dict__ = data

# #     def __str__(self):
# #         str_rep = ' '
# #         for key, value in self.__dict__.items():
# #             str_rep += f'{key} = {value}'
# #         return str_rep

# # data_dict1 = {
# #     'a' : 10,
# #     'b' : 20,
# #     'name' : 'One'
# # }

# # data_dict2 = {
# #     'c' : 15,
# #     'd' : 20,
# #     'name' : 'two'

# # }

# -----------------------







