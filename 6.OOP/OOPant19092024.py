# class Point:
#     def __init__ (self, x, y):
#         self.x = x
#         self.y = y


# Låt oss kunna skriva ut abra poin1 med inbyggda metoder

    # def __repr__(self):
    #  return f"Point(X = {self.x} and y={self.y}"

    # def __str__(self):
    #   return f"Point object method (X = {self.x} and y={self.y}"


#     def __eq__(self, other):
#       return self.x == other.x and self.y == other.y

# point1 = Point(10, 20)
# point2 = Point(10, 20)

# print(point1 == point2) # Blir false pga att man bara jämför namnet och innehållet först, men efter def __ eq true

# -------------------

# Till exempel 

# class Point:
#     def __init__ (self, x, y):
#         self.x = x
#         self.y = y

#     def swap_xy(self):
#         self.x, self.y = self.y, self.x


# point1 = Point(10, 20)

# point1.swap_xy()
# print(point1.x, point1.y)

# Arv -------------------------------------------------------

# Likt fordon, allt som är gemensamt -> Tar en till en plats, rör sig), sedan mer specifikt om den har motor, antal hjul. 


# class A: #Klass fordon

#     def __init__(self, value):
#         print(f"A__init__ has value = {value}")
#         self.value = value
#         self.value += 30
        

# class B(A): #Klass motorfordon

#     def __init__(self, value):
#         print(f"B__init__ has value = {value}")
#         super().__init__(value)
#         self.value += 30

# # Klass cykel

# class C(A):
#        def __init__(self, value):
#         print(f"C__init__ has value = {value}")
#         super().__init__(value)
#         self.value *= 8 


# # Klass bil

# class D(C, B): # Multipelt arv
#        def __init__(self, value):
#         print(f"D__init__ has value = {value}")
#         super().__init__(value)
        

# d = D(30)
# print( d.value)
# print(D.mro()) # Hur det ärvs, vem är vems super, metoedlösningsordning mro, D går till A först, sen B och sist C

#---------------------------------------------------------------------------

# Bas-klass (parent)
# class Animal:
#     def __init__(self):
#         print("Djur")

#     def WhoAmI(self):
#         print("Djur")

#     def eat(self):
#         print("Äter .... nom nom....")


# # Avledd klass, derived class
# class Dog(Animal): # Dog ärver från Animal
#     def __init__(self):
#         print("Hund skapad")

#     def WhoAmI(self):
#         print("hund")

#     def bark(self):
#         print("voff")


# d = Dog()
# d.WhoAmI() #Den tar över den senare för det står något där
# d.eat() #Man behöver inte repetera kod
# d.bark()


#-----------------------------------------

# class Employee:
#     increase = 1.04
#     def __init__(self, first_name, last_name, salary):
#       self.first_name = first_name
#       self.last_name = last_name
#       self.salary = salary

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} tjänar {self.salary}"
   
#     def increase_salary(self):
#       self.salary = int(self.salary * self.increase)

# class Developer(Employee):
#     increase = 1.10 # Den tar över denna från tidigare klass, även fast uträkningen är där
#     def __init__(self, first_name, last_name, salary, prog_lang):
#       super(). __init__(first_name, last_name, salary)
#       self.prog_lang = prog_lang

#     def __str__(self):
#         return f"{super().__str__()} och favorit programeringsspråk är {self.prog_lang}"
      
   


# # emp1 = Employee("Alice", "Ason", 45000)
# emp1 = Employee("Alice","Ason", 45000)
# emp2 = Employee("Bob", "Bobson", 35000)
# developer1 = Developer("Karl", "Karlsson", 50000, "Python")

# print(emp1)
# print(emp2)
# print(developer1)

# # Alla får en löneökning

# emp1.increase_salary()
# emp2.increase_salary()
# developer1.increase_salary()

# print(emp1)
# print(emp2)
# print(developer1)
      
    






