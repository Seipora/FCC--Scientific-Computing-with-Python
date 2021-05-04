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
