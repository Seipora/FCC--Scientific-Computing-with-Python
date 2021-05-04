# Creating a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side.
# The function should optionally take a second argument.
# When the second argument is set to True, the answers should be displayed.
# The function will return the correct conversion if the supplied problems are properly formatted,
# otherwise, it will return a string that describes an error that is meaningful to the user.

def arithmetic_arranger(problems, i=False):
    denominator = list()
    numerator = list()
    operator = list()

    # Defining a function which checks whether elements are integer (Error #1)
    def int_check(integer):
        try:
            i = int(integer)
            return True
        except:
            return False

    # Checking if there are more than 5 problems in list (Error #2)
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        a = problem.split(" ")  # Splitting denominator, numerator and operator
        if len(a[0]) > 4 or len(a[2]) > 4:  # Checking if length of denominator or numerator is >4 (Error #3)
            return "Error: Numbers cannot be more than four digits."
        if a[1] != "+" and a[1] != "-":  # Checking if there is a proper operator -> + or - (Error #4)
            return "Error: Operator must be '+' or '-'."
        # Using function for checking if elements were integers
        if int_check(a[0]) is False:
            return "Error: Numbers must only contain digits."
        if int_check(a[2]) is False:
            return "Error: Numbers must only contain digits."

        # Slicing each section into separate list for arranging
        numerator.append(a[0])
        denominator.append(a[2])
        operator.append(a[1])

    # Converting list into a string for formatting
    first_operand = ""  # numerator
    second_operand = ""  # denominator
    lines = ""  # Will be used for end lines
    result = ""
    final = ""  # for showing result
    count = 0

    # Looping through both lists to get each problem separately, both numerator and denominator have same length
    for part in range(len(numerator)):
        # Converting operator into a working operator and doing math
        if operator[part] == "+":
            result = str(int(numerator[part]) + int(denominator[part]))
        elif operator[part] == "-":
            result = str(int(numerator[part]) - int(denominator[part]))

        count += 1  # Keeping count to make sure 4 spaces don't get after the last problem

        if count < len(numerator):
            if len(numerator[part]) > len(denominator[part]):  # Getting bigger number for formatting operator
                first_operand += numerator[part].rjust(len(numerator[part]) + 2) + "    "  # Justifying to fit second
                second_operand += operator[part] + " " + denominator[part].rjust(len(numerator[part])) + "    "
                lines += "-" * (len(numerator[part]) + 2) + "    "  # End lines
                final += result.rjust(len(numerator[part]) + 2) + "    "

            else:  # in case second is bigger
                first_operand += numerator[part].rjust(len(denominator[part]) + 2) + "    "
                second_operand += operator[part] + " " + denominator[part].rjust(len(denominator[part])) + "    "
                lines += "-" * (len(denominator[part]) + 2) + "    "
                final += result.rjust(len(denominator[part]) + 2) + "    "

        elif count == len(numerator):  # For last item in list (same as before just without space after)

            if len(numerator[part]) > len(denominator[part]):
                first_operand += numerator[part].rjust(len(numerator[part]) + 2)
                second_operand += operator[part] + " " + denominator[part].rjust(len(numerator[part]))
                lines += "-" * (len(numerator[part]) + 2)
                final += result.rjust(len(numerator[part]) + 2)
            else:
                first_operand += numerator[part].rjust(len(denominator[part]) + 2)
                second_operand += operator[part] + " " + denominator[part].rjust(len(denominator[part]))
                lines += "-" * (len(denominator[part]) + 2)
                final += result.rjust(len(denominator[part]) + 2)

    if i:
        return first_operand + "\n" + second_operand + "\n" + lines + "\n" + final
    else:
        return first_operand + "\n" + second_operand + "\n" + lines

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

import unittest

# the test case
class UnitTests(unittest.TestCase):
    def test_arrangement(self):
        actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]')

        actual = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
        expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
        self.assertEqual(actual, expected,
                         'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]')

    def test_too_many_problems(self):
        actual = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
        expected = "Error: Too many problems."
        self.assertEqual(actual, expected,
                         'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."')

    def test_incorrect_operator(self):
        actual = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(actual, expected,
                         '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."''')

    def test_too_many_digits(self):
        actual = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers cannot be more than four digits."
        self.assertEqual(actual, expected,
                         'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."')

    def test_only_digits(self):
        actual = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(actual, expected,
                         'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."')

    def test_solutions(self):
        actual = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
        expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
        self.assertEqual(actual, expected,
                         'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with arithemetic problems and a second argument of `True`.')


if __name__ == "__main__":
    unittest.main()
