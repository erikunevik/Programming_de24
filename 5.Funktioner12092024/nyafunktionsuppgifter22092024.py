
# 1


def array_check(s):


    
    for number in range(len(s) - 2):
        if s[number] == 1 and s[number + 1] == 2 and s[number + 2] == 3:  

         return True
        
    return False
         
print(array_check([4, 5, 6, 9, 1, 2, 4, 1, 2, 3]))
    


# 2


# def stringbits(s):

#     everySecondChar = " "
#     for words in range(0, len(s), 2):
#      everySecondChar += s[words]
     
#     return everySecondChar

# print(stringbits("mojitoärgott"))


# ------------------------------------------


# def stringbits(s):

#     return(s[::2])


# print(stringbits("larslarslars"))

# 3

# def doublestring(s):

#  doubleword = ""      
    
#  for i in s:
#       doubleword += i * 2
  
#       return doubleword

    
# print(doublestring("apaaaaaaaannnnnss"))

# 4

# def count_evens(s):

#     numbers = 0
    
#     for i in s:
#         if i % 2 == 0:
#             numbers += 1  

#     return numbers  

# print(count_evens([1, 2, 3, 4, 5, 6]))

# 5
        









