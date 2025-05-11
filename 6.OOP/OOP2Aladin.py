

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f'Point(x = {self.x} and y ={self.y})'

# point1 = Point(10, 20)

# # print(point1.x, point1.y)

# print(point1)

#--------------------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f'Point(x = {self.x} and y ={self.y})'
    
#     def __str__(self):
#         return f'Point-object med (x = {self.x} and y ={self.y})'

# point1 = Point(10, 20)

# print(point1)

#--------------------------------------------


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


#     def swap_xy(self):
#         self.x, self.y = self.y, self.x
    



# point1 = Point(10, 20)

# point1.swap_xy()
# print(point1.x, point1.y)

#--------------------------------------------


# class A:
#     def __init__(self,value):
#         print(f'A.__init__ has value = {value}')
#         self.value = value

# class B(A):
#     def __init__(self,value):
#         print(f'B.__init__ has value = {value}')
#         super().__init__(value)
#         self.value += 10

# class C(A): 
#     def __init__(self,value):
#         print(f'C.__init__ has value = {value}')
#         super().__init__(value)
#         self.value *= 4   

# class D(C, B):
#     def __init__(self, value):
#         print(f'D.__init__ has value = {value}')
#         super().__init__(value)

# d = D(10)
# print(d.value)
# print(D.mro()) #metodlösningsordning



#--------------------------------------------

# # Bas-klass (parent)
# class Animal:
#     def __init__(self):
#         print('Djur skapat')

#     def WhoAmI(self):
#         print('Djur')
    
#     def eat(self):
#         print('Äter ....nom nom...')

# # Avledd klass (Derived class)
# class Dog(Animal): # Dog ärver från Animal
#     def __init__(self):
#         print('Hund skapad')

#     def WhoAmI(self):
#         print('Hund')
    
#     def bark(self):
#         print('Voff')

# d = Dog()
# d.WhoAmI()
# d.eat()
# d.bark()


#--------------------------------------------


# class Employee:
#     increase = 1.04
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
    
#     def __str__(self):
#         return f'{self.first_name} {self.last_name} tjänar {self.salary}'
    
#     def increase_salary(self):
#         self.salary = int(self.salary * self.increase)

# class Developer(Employee):
#     increase = 1.10
#     def __init__(self, first_name, last_name, salary, prog_lang):
#         super().__init__(first_name, last_name, salary)
#         self.prog_lang = prog_lang
    
#     def __str__(self):
#         return f'{super().__str__()} och favorit programmeringsspråk är {self.prog_lang}'

# emp1 = Employee("Alice", "Ason", 45000)
# emp2 = Employee("Bob", "Bson", 42000)
# dev1 = Developer("Carl", "Cson", 50000, 'Python')

# print(emp1)
# print(emp2)
# print(dev1)

# # Alla får löneökning
# emp1.increase_salary()
# emp2.increase_salary()
# dev1.increase_salary()

# print(emp1)
# print(emp2)
# print(dev1)

#--------------------------------------------
# Polymorfism

# class Animal:
#     def speak(self):
#         return "Ett ljud"
    
# class Dog(Animal):
#     def speak(self):
#         return "Voff"

# class Cat(Animal):
#     def speak(self):
#         return "Mjau"
    
# dog = Dog()
# cat = Cat()

# animals = [dog, cat]

# for animal in animals:
#     print(animal.speak())



#--------------------------------------------

# Duck-typing

class Bird:
    def make_sound(self):
        return 'Ett ljud'

class Duck(Bird):
    def make_sound(self):
        return 'Kvack'
    
class Crow(Bird):
    def make_sound(self):
        return 'Kra'
    
def let_bird_make_sound(bird):
    return bird.make_sound()

duck = Duck()
crow = Crow()

print(let_bird_make_sound(duck))
print(let_bird_make_sound(crow))
