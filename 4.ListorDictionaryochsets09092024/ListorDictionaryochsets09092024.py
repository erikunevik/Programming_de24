# my_list = [1, 2, 3, "0", "text", True]
# print(my_list[1:]) # Skippar den första
# print(my_list[:3]) #slicing, skriver de 3 förtsa
# print(my_list[-1]) # Skriver bara den sista
# print(my_list[:-1]) # Skriver alla utom den sista
# print(my_list[:-2]) # Skriver ut alla förutom de två sista
# print(my_list[::2]) # every second element
# print(my_list),

#---------------------------------------

# sammanfoga

# my_list = [1, 2, 3, "0", "text", True]
# print(my_list + ["new item"])
# # print(my_list)

# # my_list = my_list + ["new item"] # Man lägger till något
# print(my_list)

#------------------------------

# Metoder

# list = [1, 2, 3]

# # list.append("append me")
# # list.pop(0) # Bara intgers?

# # print(list)

# popped_item = list.pop(0)
# print(popped_item)


#---------------------

# Ta bort, remove på specifikt, pop enl index


list = [1, 2, 3]

list.append("append me")
print(list)

list.remove("append me")
print(list)


#-----------------------

# Reverserande funktion

# new_list = ["a", "e", "x", "b", "c"]
# new_list.reverse()
# print(new_list)

# new_list.sort() # Bokstavsordning
# print(new_list)

#------------------------------------------

# Tupels. Likt datum i kalender, personummer mm.


# Du kan också ändra items i en lista, fungerar bara med integers?

# list = [1, 2, 3]
# list[1] = (10)
# print(list)

#------------------------

# my_tuple = list(1, 2, 3)
# my_list = list[8, 9, 10]

# my_tuple = (1, 2, 3, 'four')
# my_tuple2 = (5,)
# my_tuple = my_tuple + my_tuple2
# print(my_tuple)

# list (1, 2) = tuple

#_------------------------- Aladins



# my_dictionary = {
#     1 : "value one",
#     2 : "value two",
#     3: "value three"
# }

# print(my_dictionary[1])


# my_dictionary = {
#     1 : "value one",
#     2 : "value two",
#     3: "value three",
#     4: ["name_one", "name_two"]
# }

# print(my_dictionary[4])
# print(my_dictionary[4][0]) # Bara den första på 4an
# print(my_dictionary[4][0].upper()) # Bara den första på 4an i stora bokstäver

#-----------------------------------

# my_dictionary = {
#     1 : "value one",
#     2 : "value two",
#     3: "value three",
#     4: ["name_one", "name_two"]
# }

# my_dictionary[1] = "updated value one"  # Byter ut

# print(my_dictionary)

# my_dictionary[4] += ['name_three']

# print(my_dictionary)


#-----------------------------------

#assignments

# new_dictionary = {}

# new_dictionary['animal'] = 'cat'
# new_dictionary['answer'] = 42

# print(new_dictionary["animal"])

#-----------------------------------

# nested_dictionary = {
#      "person 1": {
#         "name" : "Alice",
#         "age" : 30
#     },
#     "person 2": {
#         "name" : "Bob",
#         "age" : 25
#     }
# }

# print(nested_dictionary["person 1"]["age"])


# Hur man får ut bara namnet bara, om man ska ha ut ålder så får man lägga till stringcommand mm.

# nested_dictionary = {
#     "person 1": {
#         "name": "Alice",
#         "age": 30
#     },
#     "person 2": {
#         "name": "Bob",
#         "age": 25
#     }
# }

# # Collect all ages
# ages = [str(person_info["age"]) for person_info in nested_dictionary.values()]

# # Print all ages
# print(", ".join(ages))





#-------------------------------------------

# nested_dictionary = {
#     "person 1": {
#        "name": {
#            "first": "Alice",
#            "last" : "Alisson",
#            "third": "Toni"
#         },
#         "age" : 30,
#         "Eye color" : "Brown",
#     },
#     "person 2": {
#         "name" : {
#             "first": "Bob",
#             "last" : "Bobson",
#             "third": "Toni"
#         },
#         "age" : 25,
#         "eye color" : "blue"
#     }
# }

# # print(nested_dictionary)
# # print(nested_dictionary ["person 2"]["name"]["third"])
# # print(nested_dictionary ["person 1"]["Eye color"])

# print(nested_dictionary .keys())
# print(nested_dictionary .values())
# print(nested_dictionary.items ()) #key-value-pair






#-------------------------------------------

#Methods

# dictionary = {
#     "key 1": 1,
#     "key 2": 2,
#     "key 3": 3
# }

# # print(dictionary.keys())
# # print(dictionary.values())
# # print(dictionary.items()) #key-value-pair

# print(dictionary.keys())    # Returns the keys: dict_keys(['key 1', 'key 2', 'key 3'])
# print(dictionary.values())  # Returns the values: dict_values([1, 2, 3])
# print(dictionary.items())   # Returns key-value pairs: dict_items([('key 1', 1), ('key 2', 2), ('key 3', 3)])

#---------------------------------------------------

# # Set

# x = set()

# x.add(1)

# print(x)

#-----------------------------------

# y = {1, 2, 3}

# y.add(4)

# print(y)

# y.add(3) # Får bara finnas en varje därför ingen 3a

# print(y)

#-----------------------------------

# my_list = [1, 2, 3, 1, 2, 3, 4, 5, 4, 6]

# print(set(my_list)) # Gör om den till ett set?

# # -----------------------------------

# my_set = {"äpple", "banan", "melon", "kiwi", "citron"}

# my_set.update(["kiwi", "citron"])

# print(my_set)

# my_set.remove("banan")
# # my_set.remove("äpple")

# my_set.discard("äpple")


# print(my_set)


# for frukt in my_set:
#     print(frukt)

# print("äpple" in my_set)
# print("melon" in my_set)


# my_set.clear()
# print(my_set)

#-------------------------------------------

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# print(A.union(B))
# print(A | B) # " Slår ihop alla siffror"

# #-------------------------------------------


# Snitt "Intersection"  A∩B # Vilka siffror som finns i bägge seten

# print(A.intersection(B))
# print(A & B)

#-------------------------------------------

# Differens "Mängddifferens"  A − B eller A \ B, skillnaden mellan två set

# print(A.difference(B))
# print(A - B)


# Aladins listor-------------------------------------



# my_list = [0, 1, 2, "0", "Text", True]

#-------------------------------------------------

# name = ["Kalle", "Pelle"]
# my_list = [1,2,3, name]

# print(my_list)


#-------------------------------------------------

# my_list = [1, 2, 3, "0", "Text", True]
# print(my_list[2])

#-------------------------------------

# my_list = [1, 2, 3, "0", "Text", True]
# # print(my_list[1:])
# # print(my_list[:3])  # Slicing
# print(my_list[:])
# print(my_list[-1])
# print(my_list[:-1])
# print(my_list[::2])
# print(my_list)

#-------------------------------------

# Concatinate (Sammanfoga)

# my_list = [1, 2, 3, "0", "Text", True]
# print(my_list + ['new item'])
# print(my_list)

# my_list = my_list + ['new item']
# print(my_list)
# print(my_list * 2)

#---------------------------------------------

# Metoder

# list = [1, 2, 3]

# list.append('append me')
# list.pop(0)
# print(list)

# popped_item = list.pop(0)
# print(popped_item)

# list = [1, 2, 3]
# print(list[10])



# list = [1, 2, 3]
# list.append("append me")
# print(list)

# list.remove("append me")
# print(list)


# new_list = ['a', 'e', 'x', 'b', 'c']
# # new_list.reverse()
# # print(new_list)

# new_list.sort()
# print(new_list)



#---------------------------------------------------------------

# Tuples

# my_tuple = (1, 2, 3)

# print(len(my_tuple))

#----------------------------

# my_tuple = (1, 2, 3, 'four')

# print(my_tuple)

# indx

# print(my_tuple[-1])

#-----------------------

# my_tuple = (1, 2, 3, 'four', 3)

# print(my_tuple.index('four'))

# print(my_tuple.count(3))


#---------------------------------

# my_tuple = (1,2,3,'four')
# my_tuple[0] = 5

# print(my_tuple)

# my_tuple = (1,2,3,'four')
# my_tuple.append(4)

# print(my_tuple)

# my_tuple = (1, 2, 3, 'four', [])
# my_tuple[-1].append("Kommer funka!")

# print(my_tuple)

# my_tuple = (1, 2, 3, 'four')
# my_tuple2 = (5,)
# my_tuple3 = my_tuple + my_tuple2
# print(my_tuple3)






