

# class Fordon:
#     def __init__(self, märke, år, färg):
#         self.märke = märke
#         self.år = år
#         self.färg = färg

#     def __str__(self):     
#      return f"{self.märke} är från {self.år} och är {self.färg}"

#     def start(self):
#         print(f"{self.märke} från {self.år} som är {self.färg} har startat")
              
#     def stop(self):
#         print(f"{self.märke} från {self.år} som är {self.färg} har stannat")

#     def tanka(self):
#      pass # Passas för man vet ju inte om alla fordon kan tankas, smart!
        

    
# class Cykel(Fordon):
#     def __init__(self, märke, år, färg, växlar):
#         super(). __init__(märke, år, färg)
#         self.växlar = växlar

#     def __str__(self): 
#         return f"{super().__str__()} och har {self.växlar} växlar"

#     def ringklocka(self):
#         return("och har ringt på ringklockan")


# class Bil(Fordon):

#     def __init__(self, märke, år, färg, dörrar):
#         super(). __init__(märke, år, färg)
#         self.dörrar = dörrar


#     def __str__(self): 
#         return f"{super().__str__()} och har {self.dörrar} dörrar"
        

#     def öppna(self):
#         return(" och bilens dörrar öppnats")
    
#     def tanka(self):
#        print(f"{self.märke} från {self.år} som är {self.färg} och har tankats")
       


# class Motorcykel(Fordon):

#     def __init__(self, märke, år, färg):
#         super(). __init__(märke, år, färg)

#     def etthjul(self):
#      return("och har kört på ett hjul")
    

# # Skapa instanser av fordon


# cykel = Cykel("Cressent", 1987, "vit", 18)
# bil = Bil("BMW", 2024, "Mörkblå", 4)
# motorcykel = Motorcykel("Honda", 2005, "röd")


# print(f" {cykel} {cykel.ringklocka()}")
# print(f" {bil} {bil.öppna()}")
# print(f" {motorcykel} {motorcykel.etthjul()}")
# bil.tanka()
# cykel.start()
# motorcykel.stop()
# print(motorcykel.etthjul())


# 2 ------------------------------------------------------------------------------------------

# Chatgpt:

# import math

# Base class Shape
# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclasses must implement this method")

#     def perimeter(self):
#         raise NotImplementedError("Subclasses must implement this method")

# Subclass Circle
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# Subclass Rectangle
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# Subclass Triangle (Assuming it is an equilateral triangle for simplicity)
# class Triangle(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return (math.sqrt(3) / 4) * self.side ** 2

#     def perimeter(self):
#         return 3 * self.side

# Create instances of each shape
# circle = Circle(9)
# rectangle = Rectangle(5, 7)
# triangle = Triangle(2)

# Demonstrate polymorphism
# shapes = [circle, rectangle, triangle]

# for shape in shapes:
#     print(f"{shape.__class__.__name__}:")
#     print(f" Area: {shape.area():.2f}")
#     print(f" Perimeter: {shape.perimeter():.2f}")
#     print()


        
   

