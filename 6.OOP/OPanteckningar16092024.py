
# 1 = [1, 2, 3]

# print(type(1))

# print(type([])) # Är list klass

# print(type({})) # Är dictionary klass

#  #Nyckelordet för att skapa klasser är klass. Från klasserna kan man skapa objekt/instanser

#---------------------------------------------

# class Sample():
#     pass # Lite låt gå, det kommer sen dvs pass

# x = Sample() # Namge klasser med stor bokastav

# print(type(x))

#--------------------------

# class Dog():
#     # Class object atributes:
#     species = "Däggdjur"
#     def __init__(self, breed, name):  # En konstruktor skapas
#        self.breed = breed
#        self.name = name

# frank = Dog("Huskie", "Frank",) 

# print(frank.breed)
# print(frank.name)
# print(frank.species)

#----------------------------------------

# class Circle:
#     pi = 3.14

#     # Cirklen initieras med en radie (standrad 1)
#     def __init__(self, radius=1):  # Konstruktor
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
    

# cirkel = Circle()
# cirkel.setRadius(8)
# print("Radien är: ", cirkel.getRadius())
# print("Area är: ", cirkel.area())


#-----------------------------------------------------

# Fler exempel

# class Person:
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
        
#     def __str__(self):
#       return f'{self.name} är {self.age} år gammal och har e-post {self.email}'

# p1 = Person('Alice', 'Alice@hotmail.com', 34)
# p2 = Person('Bob', 'Bob@email.com', 37)

# print(p1)
# print(p2)

# p1.phone = '072959596'

# print(p1.phone)
# # print(p2.phone) # kommer inte fungera

#----------------------------------------------------

# class Person:
#     def __init__(self, **kwargs):
#         self.__dict__=kwargs

#     def __str__(self):
#       return f"{self.name} är {self.age} år gammal"

# p1 = Person(name = 'ALice', age = 23)
# p2 = Person(name = 'Bob' , age = 75)

# print(p1)
# print(p2)

#------------------------------------------

# class Something:
#     def __init__(self, data:dict):  #Type hint, vill att du skrive en dictionary
#         self.__dict__ = data

#     def __str__(self):
#         str_rep = ' '
#         for key, value in self.__dict__.items():
#             str_rep += f'{key} = {value}'
#         return str_rep

# bla1 = {
#     'a' : 10,
#     'b' : 20,
#     'name' : 'One'
# }

# bla2 = {
#     'c' : 15,
#     'd' : 20,
#     'name' : 'two'

# }

# # s1 = Something(data_dict1)
# # s2 = Something(data_dict2)      

# print(bla1)
# print(bla2)


    
    


