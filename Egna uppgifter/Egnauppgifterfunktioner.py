
# Here's a different challenge for you:

#Challenge: Sum of Positive Integers
#Create a function sum_positive(numbers) that takes a list of integers and returns the sum of all the positive integers in the list. You should ignore any negative numbers or zeros.


def sum_positive_integers(s):

    positive_numbers = []   

    for numbers in s:

              
        if numbers > 0:
           positive_numbers.append(numbers)

    return sum(positive_numbers)
    


print(sum_positive_integers([1, -4, 7, 0, -3, 5]))    



                         
                        