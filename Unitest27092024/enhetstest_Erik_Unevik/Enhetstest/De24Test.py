import unittest

# SVAR FRÅGA 1: Multiplicera flyttalen
def multiply_floats(a, b):
    
    return a * b

# SVAR FRÅGA 2: Omvandla till sträng
def convert_to_string(x):
    
    return str(x)
        
        

# SVAR FRÅGA 3: Kontrollera om ett nummer är positivt, negativt eller noll
def check_number_type(x):


    if x > 0:
        return ("Positivt")

    elif x == 0:
        return("Noll")
    else:
        return("Negativt")

    


# SVAR FRÅGA 4: Beräkna längden av en listorna
def length_of_list(lst):
    
    return len(lst)

# SVAR FRÅGA 5: Returnera alla element i listan i omvänd ordning
# Klurig!
def reverse_list(lst):

    new_lst = lst[::-1]
    
    return new_lst


# SVAR FRÅGA 6: Iterera över en lista och returnera element STÖRRE än 5
def filter_greater_than_five(lst):
    
    over_5 = []
    for number in lst:
        if number > 5:
            over_5.append(number)
    return over_5


# SVAR FRÅGA 7: Lägg till en nyckel och ett värde i dictionary
def add_key_value_to_dict(d, key, value):



    d[key]=value
    return d

# SVAR FRÅGA 8: Använd for-loop för att summera (+) alla tal i en lista
def sum_with_loop(lst):

    sum = 0
    for numbers in lst:
        sum = sum + numbers

    return sum

# SVAR FRÅGA 9: Kontrollera om ett tal är jämnt eller udda
def is_even_or_odd(num):
    
    if num % 2 == 0:
        return ("Jämnt")
    else:
        return ("Udda")

# SVAR FRÅGA 10: Kombinera två listor
def combine_lists(lst1, lst2):
    
    return lst1 + lst2




# RÖR EJ
#------------------------------------------------------------------------------------


question_map = {
    "test_01_multiply_floats": "Fråga 1",
    "test_02_convert_to_string": "Fråga 2",
    "test_03_check_number_type": "Fråga 3",
    "test_04_length_of_list": "Fråga 4",
    "test_05_reverse_list": "Fråga 5",
    "test_06_filter_greater_than_five": "Fråga 6",
    "test_07_add_key_value_to_dict": "Fråga 7",
    "test_08_sum_with_loop": "Fråga 8",
    "test_09_is_even_or_odd": "Fråga 9",
    "test_10_combine_lists": "Fråga 10"
}

class CustomTestResult(unittest.TextTestResult):
    def addFailure(self, test, err):
        super().addFailure(test, err)
        test_name = test._testMethodName
        question = question_map.get(test_name, test_name)
        print(f"Fail: {question}")


class TestMathAndStringFunctions(unittest.TestCase):

    # Test Fråga 1
    def test_01_multiply_floats(self):
        try:
            self.assertAlmostEqual(multiply_floats(2.5, 4), 10.0, places=7)
        except TypeError:
            self.fail("TypeError: multiply_floats returnerade None istället för ett numeriskt värde")
        try:
            self.assertAlmostEqual(multiply_floats(-1.2, 3), -3.6, places=7)
        except TypeError:
            self.fail("TypeError: multiply_floats returnerade None istället för ett numeriskt värde")
        try:
            self.assertAlmostEqual(multiply_floats(0, 3), 0, places=7)
        except TypeError:
            self.fail("TypeError: multiply_floats returnerade None istället för ett numeriskt värde")
        

    # Test Fråga 2
    def test_02_convert_to_string(self):
        self.assertEqual(convert_to_string(100), "100")
        self.assertEqual(convert_to_string(3.14), "3.14")

    # Test Fråga 3
    def test_03_check_number_type(self):
        self.assertEqual(check_number_type(10), "Positivt")
        self.assertEqual(check_number_type(-5), "Negativt")
        self.assertEqual(check_number_type(0), "Noll")

    # Test Fråga 4
    def test_04_length_of_list(self):
        self.assertEqual(length_of_list([1, 2, 3]), 3)
        self.assertEqual(length_of_list([]), 0)

    # Test Fråga 5
    def test_05_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list([5, 6, 7]), [7, 6, 5])
        self.assertEqual(reverse_list([]), [])

    # Fråga 6
    def test_06_filter_greater_than_five(self):
        self.assertEqual(filter_greater_than_five([1, 6, 3, 7, 5]), [6, 7])
        self.assertEqual(filter_greater_than_five([1, 2, 3]), [])

    # Fråga 7
    def test_07_add_key_value_to_dict(self):
        self.assertEqual(add_key_value_to_dict({"a": 1}, "b", 2), {"a": 1, "b": 2})
        self.assertEqual(add_key_value_to_dict({}, "a", 1), {"a": 1})

    # Fråga 8
    def test_08_sum_with_loop(self):
        self.assertEqual(sum_with_loop([1, 2, 3]), 6)
        self.assertEqual(sum_with_loop([]), 0)

    # Fråga 9
    def test_09_is_even_or_odd(self):
        self.assertEqual(is_even_or_odd(2), "Jämnt")
        self.assertEqual(is_even_or_odd(3), "Udda")

    # Fråga 10
    def test_10_combine_lists(self):
        self.assertEqual(combine_lists([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(combine_lists([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(combine_lists([], [5]), [5])


# RÖR EJ
if __name__ == '__main__':
    runner = unittest.TextTestRunner(resultclass=CustomTestResult)
    runner.run(unittest.makeSuite(TestMathAndStringFunctions))
