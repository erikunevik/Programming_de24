

# print(5+2)

# def adder(num1, num2): # num är parametrar

#     return num1 + num2 # I provet testas funktionen


# # Rör ej

# print(adder(2, 5))

#------------------------------------------

# x = "parallella "

# print(len(x))

# # func

# def length(x):

#     return len(x)

# # Rör ej

# print(length("mojitomojitomojito"))

# def length(x):

#  return len(x)

# print(x.upper())
# print(x.lower())
# print(x.split())
# print(x.split("l"))

#----------------------------------------------

# Variabler finns till för att lagra och manipulera information

# namn = "Alice"
# ålder = 30

# print("Namn:", namn)
# print("Ålder:", ålder)

# [] # För index och listor

# a = "Hello world"

# print(a[0]) # Skriver ut bara första het från den första eftersom 0
# print(a[1]) # Bara första e eftersom 1
# print(a[1:]) # Från e och sen resten
# print(a[:3]) # Första 3
# print(a[:]) # HEla
# print(a[-1]) # Den sista
# print(a[::2]) # Varannan

#-----------------------------------------------------------

# # String inmutable
# # lista mutable
# # Tuple inmutable

# a = "Hello world"

# a[0] = "x" # Går ej

# a = a + "concate me"

# print(a)

#----------------------------------------------------

# name = "alice"
# age = "30"

# print(f" ")

# Ska skrivas exakt så som han vill ha det

# def comparer(num1, num2):
#     if num1 < num2:
#         return "Yes!"
#     else:
#         return "No!"


#     # Rör ej


# print(comparer(3, 1))
# print(comparer(3, 4))


#------------------------------------------

# name = "Alice"
# age = 36

# if age == 35 and name == "alice":
#     print("Kom in")
# elif age == 35 or name == "Alice":
#     print("Något av kraven uppfylls ej")
# else:
#     print("Ingen av kraven uppfylls")

#------------------------------------------------------------


# for i in range(2, 10, 2): # Den stegar med 2
#     print(i)

# lista = [1, True, None, "String", 2.5]

# print(lista)

# for i in lista:
#     print(i)

#-----

# [1, True, None, "String", 2.5]

# def lister(lista):
#     myList = []
#     for i in lista:
#         myList.append(i)
#     return myList

# # Hade bara kunnat köra addera



# print(lister([1, True, None, "String", 2.5]))

#-----------

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Loopen är avslutad") # Om vi inte har itenderingen där så kommer det skrivas ut varje gång


#-----------------------------------------

# guess = input("Ange mest populära toppningen")

# while guess != "ost":
#     print("Fel")
#     guess = input("Ange mest populära toppningen")

# print("Rätt svar")

# -----------------------------------

# def gissa_topping(guess):
#     while guess != "ost":
#         return "fel"

#     return "Rätt svar!"


# # rör ej

# test1 = gissa_topping("skinka")
# print(test1)

# print(gissa_topping("skinka"))

# test2 = gissa_topping("ost")
# print(test2)

#--------------------------------------


# my_list = [1, True, None, "String", 2.5]

# print(my_list + ["new item"])

# print(my_list) # Inget har lagts till

# my_list += ["new item"]

# print(my_list) # För lister är mutable


#-------------------------

# new_dict = {}

# new_dict["animal"] = "cat"

# print(new_dict)

# func

# def createDict(new_dictionary, animal, typeanimal, color): # parametrar

#     new_dictionary[animal]=typeanimal, color
#     return new_dictionary


# # Rör ej
# print(createDict({}, "animal", "cat", "blue"))  #-> {"animal" : "cat"}

# dictionary = {
#     "key1" :1,
#     "key2" :2,
#     "key3" :3,
# }

# print(dictionary.items())

# for key, value in dictionary.items():

#     print(f" {key} :  {value} ")



#-----------------------------------

