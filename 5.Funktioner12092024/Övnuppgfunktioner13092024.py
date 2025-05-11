
# 1

# list1 = (1, 1, 2, 3, 1)
# list2 = [1, 1, 2, 4, 1]
# list3 = [1, 1, 2, 1, 2, 3]


# len(list1)
# print(list1)


# def arrayCheck(nums):
#     for i in range(len(nums)-2):
#         if nums[i] == 1 and nums[i+1]== 2 and nums [i+2] == 3:
#             return True
        
#     return False
    

# print(arrayCheck([1, 1, 2, 3, 1]))
# print(arrayCheck([1, 1, 2, 4, 1]))
# print(arrayCheck([1, 1, 2, 1, 2, 3]))

# 2

# def everysecondchar(word):
#     print(word [::2]) # printa ut varannan bokstav, kan inte göra något annat


# everysecondchar("LarsGrisNästan")

# ----------- Aladins lösning

# def everysecondchar(word):
#     return word [::2] # Här har du varannan bokstav, gör vad du vill med den. Du kan typ stoppa in den i en lista, dictionary t.ex.

# everysecondchar("LarsGrisNästan")


# 3

# def doubleChar(word):
#     result = ""
#     for char in word:
#         result += char * 2  # Repeat each character twice and append to the result string
#     return result # Du måste returnera det i något, dvs result. 

# print(doubleChar("ÄpplE"))  # Output: 'AAPpaannaallrressggrriiss'

# 4

# def CountEvens(numbers):

#     count = 0
#     for numb in (numbers):
#         if numb % 2 == 0:
#          count += 1
#     return count


# print(CountEvens([2, 1, 2, 3, 4])) # 3

# print(CountEvens([2, 2, 1, 6, 8, 9])) # 4


# 5

# import random

# random_number_list = random.sample(range(10), 3)

# guess =  []

# while guess != random_number_list:

#  input = ("Vad är din gissning?")
#  guess.append(input)

#  if random_number_list[0] and guess [0] == True or random_number_list[1] and guess [1] == True or  random_number_list[2] and guess [2] == True:
#   print("Match, du har gissat ett rätt nummer på rätt position") 

#  elif random_number_list[0] and guess [0] == False or random_number_list[1] and guess [1] == False or  random_number_list[2] and guess [2] == False:
#   print("Match, du har gissat ett rätt nummer på rätt position") 
   
     

# import random

# random_number_list = random.sample(range(10), 3)
# # Uncomment below to see the generated number (for testing)
# # print(random_number_list)

# while True:
#     guess = list(map(int, input("Vad är din gissning? ")))  # Input as a list of integers

#     if guess == random_number_list:
#         print("Grattis! Du gissade rätt nummer!")
#         break
    
#     # Checking for matches and closeness
#     for i in range(3):
#         if guess[i] == random_number_list[i]:
#             print("Match, du har gissat ett rätt nummer på rätt position.")
#         elif guess[i] in random_number_list:
#             print("Close, du har gissat ett rätt nummer men i fel position.")
#         elif guess[i] != random_number_list[i]:
#             print("Nope, du har inte gissat någon av siffrorna rätt")


# import random

# # Generate the random number with unique digits
# random_number_list = random.sample(range(10), 3)
# # Uncomment below to see the generated number for debugging
# # print(random_number_list)

# while True:
#     # Get the user's guess and convert it to a list of integers
#     guess = list(map(int, input("Vad är din gissning? ")))
    
#     # Check if the guess is correct
#     if guess == random_number_list:
#         print("Grattis! Du gissade rätt nummer!")
#         break  # The game ends when the player guesses correctly

#     # Track if there are any common digits
#     has_common_digits = False

#     # Feedback for each digit in the guess
#     for i in range(3):
#         if guess[i] == random_number_list[i]:
#             print(f"Match: Du har gissat ett rätt nummer)")
#         elif guess[i] in random_number_list:
#             print(f"Close: Du har gissat rätt nummer men i fel position")
#             has_common_digits = True

#     # Check if no common digits were found
#     if not has_common_digits:
#         print("Nope: Ingen av dina gissningar stämmer överens med något nummer.")



# import random

# # Generate the random number with unique digits
# random_number_list = random.sample(range(10), 3)

# while True:

#     gissa = list(map(int, input("Gissa tre siffror:")))

#     if gissa == random_number_list:
#         print("Grattis, du gissade rätt")
#         break

#     for i in range(3):
#         if gissa [i] == random_number_list[i]:
#          print("Du gissade en siffra på rätt position rätt")

#         elif gissa [i] in random_number_list:
#           print("Du gissade en siffra rätt fast på fel position")

#         else:
#            print("Du gissade inte rätt på någon siffra")

import random

# Generate the random number with unique digits
random_number_list = random.sample(range(10), 3)

while True:
    gissa = list(map(int, input("Gissa tre siffror: ")))

    if gissa == random_number_list:
        print("Grattis, du gissade rätt")
        break

    # Counters for feedback
    correct_position = 0
    correct_number_wrong_position = 0

    # Step 1: Check for correct numbers in the correct positions
    for i in range(3):
        if gissa[i] == random_number_list[i]:
            correct_position += 1

    # Step 2: Check for correct numbers in the wrong positions
    # Use a list to keep track of which indices have been matched
    matched_indices = [False, False, False]
    for i in range(3):
        if gissa[i] != random_number_list[i]:  # Skip already matched
            if gissa[i] in random_number_list:
                # Find the index in random_number_list to avoid double-counting
                for j in range(3):
                    if gissa[i] == random_number_list[j] and not matched_indices[j] and gissa[j] != random_number_list[j]:
                        correct_number_wrong_position += 1
                        matched_indices[j] = True  # Mark this digit as matched
                        break

    # Step 3: Print results
    if correct_position > 0:
        print(f"Du gissade {correct_position} siffra/siffror på rätt position")
    if correct_number_wrong_position > 0:
        print(f"Du gissade {correct_number_wrong_position} siffra/siffror rätt fast på fel position")
    if correct_position == 0 and correct_number_wrong_position == 0:
        print("Du gissade inte rätt på någon siffra")
























# # Givet en lista av heltal, returnera True om sekvensen av siffrorna 1, 2, 3 förekommer någonstans i
# listan.
# Exempel:
# arrayCheck([1, 1, 2, 3, 1]) -> True
# arrayCheck([1, 1, 2, 4, 1]) -> False
# arrayCheck([1, 1, 2, 1, 2, 3]) -> True