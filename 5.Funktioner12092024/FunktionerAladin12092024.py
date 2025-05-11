


# def any_name(parameter, parameter2):
#     """
#     Docstring, förklarar vad denna funktion gör
#     """
#     print(parameter)



#------------------------------

# Hello-funktion

# def hello():
#     print("hello")


# hello()
# hello()

#------------------------------


# def giveMeHello():
#     return "Hello you!"

# res = giveMeHello()
# print(res)



#------------------------------


# def giveMeHello():
#     return "Hello you!"

# print(giveMeHello())


#------------------------------


# number1 = 3

# if number1 % 2 == 0:
#     print("even")
# else:
#     print("odd")

# number2 = 5
# if number2 % 2 == 0:
#     print("even")
# else:
#     print("odd")

# number3 = 20
# if number3 % 2 == 0:
#     print("even")
# else:
#     print("odd")


# def evenCheck(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    

# print(evenCheck(10))
# print(evenCheck(5))
# print(evenCheck(7))


# def evenCheck(number):
#     print(number%2 == 0)
    

# evenCheck(10)
# evenCheck(5)
# evenCheck(7)


#------------------------------

# def helloYou(name="John"):
#     return("hello " + name)

# res = helloYou()
# print(res)

# print(helloYou("lars"))
#------------------------------


# def addEvenOnly(num1, num2):
#     if (num1 % 2 != 0) or (num2 % 2 != 0):
#         return False
#     else:
#         return num1 + num2
   


# print(addEvenOnly(3, 6))


#------------------------------

# def func(a, b, c=10, d=11):
#     print(a,b,c,d)

# func(1, 2) # Skriver ut även c och d per automatik
# func(1, 2, 3) # 3an ersätter 10an
# func(1, 2, 3, 4) # 4an Ersätter 11an

# func(c="c", a="a", d="d", b="b") # Konverterar dom till strings och skriver dom per automatik i ordning

# func(1, 2, d=4) # 3an kommer med som den är



#------------------------------

# x = 10 # Global variabel

# def myFunc():
#     x = 5   # Lokal variabel
#     print(x)


# myFunc() # Knuten till den lokala variablen
# print(x) # Knuten till den ovanstående globala variablen

# # func(1,2)
#------------------------------


# def func(*args):
#     print(args)

# func()
# func(1)
# func(1,2)
# func(1,2,3)


# Chatgpt: Positional vs. Keyword Arguments:

# *args is used for positional arguments (arguments passed without keywords).
# **kwargs is used for keyword arguments (arguments passed with keys).
# Data Type:

# *args collects arguments as a tuple.
# **kwargs collects arguments as a dictionary.


#------------------------------


# def func2(a, b, **kwargs):
#     print(a,b)
#     print(kwargs)

# func2(1, 2, c=14, d=19)

# # Chatgpt Positional arguments:

# a = 1
# b = 2  #These are captured by a and b respectively, since they are positional arguments.
#  #Keyword arguments:

# c = 14
# d = 19 # These are captured by **kwargs, which collects all additional keyword arguments into a dictionary. In this case, kwargs will be {'c': 14, 'd': 19}.

#-------------------------

# def func2(a, b, **kwargs):
#     print(a,b, kwargs)

# func2(1, 2, c=14, d, e="Lisa") # Behöver finnas ett värde för att printas

# -------------------------

# Detta löses med en if sats t.ex.


# def func2(a, b, **kwargs):
#     print(a,b)
#     if "c" in kwargs:
#         print(kwargs["c"])
#     if "d" in kwargs:
#         print(kwargs["d"])

# func2(1, 2, c=14)

#-------------------------


# def func3(a, b, *args, name="John", **kwargs):
#     print(f'a = {a}')
#     print(f'b = {b}')  
#     print(f'args = {args}')
#     print(f'name = {name}')
#     print(f'kwargs = {kwargs}')

# func3(1, 2)

# func3(1, 2, 3, name="Anna", age=34, email="anna@email.com") # Argsen suger upp den positionella 3an, kwargsen age 
# # och email då dessa är en del av func3, där man justkommer printa det som står som är inyggt