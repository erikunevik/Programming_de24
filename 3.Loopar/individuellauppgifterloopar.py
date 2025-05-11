# for i in range(1, 11):
#     print('Current value:', i)

# counter = 11111111111
# while counter <= 10:
#     print('Current value:', counter)
#     counter = counter + 1

# line_to_print = ''
# for i in range (1, 10):
#     for j in range (0, 9):
#         line_to_print += str(i)
#     print(line_to_print)
#     line_to_print = ''

# for i in range(1, 100, 4):
#     print(i)

# Individuella uppgifter

# 1 A

# for i in range(0, 11):
#     print("Värde", i)

# 1 B

# i = 0
# while (i < 11):
#     print( "Värde", i)
#     i = i + 1

# 2A

# tal1 = int(input(" Mata in ett tal"))
# tal2 = int(input(" Mata in ett tal"))

# for i in range(tal1 + 1, tal2):
#     print("Värde", i)

# 2B

# tal1 = int(input(" Mata in ett tal"))
# tal2 = int(input(" Mata in ett tal"))


# if tal2 > tal1:
#   tal1 = tal1 + 1

#   while (tal1  != tal2 ):
#      print( "Värde", tal1)
#      tal1 = tal1 + 1

# elif tal1 > tal2:
#     tal1 = tal1 - 1

#     while (tal1  != tal2 ):
#      print( "Värde", tal1)
#      tal1 = tal1 - 1

# 3

import time

ogiltigt_svar = True

while ogiltigt_svar == True:

  tal1 = int(input(" Mata in första talet"))
  tal2 = int(input(" Mata in andra talet"))

  print(f"Summan av det två talen är {tal1 + tal2}")
  time.sleep(2)
  svar = input("Vill du fortsätta (J) (N)?").lower()

  if svar == ("n"):
   print("Programmet avbryts")
   ogiltigt_svar == False
   break

#   elif svar == ("j"): # Behövs ej
#    ogiltigt_svar == True

# 4

# for i in range (1, 11):


#  print(("Mata in en valfri siffra", i))
#  summa = i

# print(summa)

# fel

# summa = 0  # Initialize summa to store the sum of inputs

# for i in range(1, 11):
#     Prompt the user for input
#     num = int(input(f"Mata in en valfri siffra ({i}/10): "))
#     summa += num  # Add the input to the sum

# print("Summan av alla siffror är:", summa)

# 5

# tal = int(input("Mata in ett tal:"))

# for i in range (1, tal):
#     print(i)

# 6

# gånger = int(input("Mata in ett tal"))

# for i in range (1, 11):
#     print(i * gånger)

# 7

# gånger = int(input("Mata in ett tal"))

# for i in range (1, 11):
#     print(f"{i} * {gånger} = {i*gånger}")


# Jävligt krångligt

# gånger = int(input("Mata in ett tal"))

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# primes = []
# for num in range(1, gånger):
#     if is_prime(num):
#         primes.append(num)
# print(primes)

# 8

# Python3 program to implement 
# run length encoding
# def printRLE(st):
 
#     n = len(st)
#     i = 0
#     while i < n- 1:
 
#         # Count occurrences of 
#         # current character
#         count = 1
#         while (i < n - 1 and st[i] == st[i + 1]):
#             count += 1
#             i += 1
#         i += 1
 
#         # Print character and its count
#         print(st[i - 1] + str(count),  end = "")
 
# # Driver code 
# if __name__ == "__main__":
 
#     st = "eeeeeeeeyyyyyyyyyyhhhhhhhhhhhhhhhh"
#     printRLE(st)
 

























































