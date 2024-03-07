from unittest.mock import patch
from io import StringIO
import sys

def main():
    try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        if number1 <= 0 or number2 <= 0 or number2 > number1:
            raise ValueError
    except:
        print("invalid number")
        exit()
    a = number1
    b = number2
    startA = 1
    listofA = []
    listofB = []
    while b < a:
        listofA.append(startA)
        listofB.append(b)
        startA *= 2
        b *= 2

    tmp_a = a
    sum_ = 0
    quotient = 0
    for z, i in enumerate(listofB[::-1]):
        if tmp_a - i >= 0:
            tmp_a -= i
            sum_ += listofB[len(listofB) - (z + 1)]
            quotient += listofA[len(listofA) - (z + 1)]

    remainder = a - sum_
    print(f"{number1} / {number2} = {quotient} r. {remainder}")

def run_test(input_values):
    with patch("builtins.input", side_effect=input_values.split()):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

# Test with valid input
result_valid_input = run_test("12\n4\n")
print(result_valid_input)  # Should print "12 / 4 = 3 r. 0"

result_valid_input = run_test("36\n2\n")
print(result_valid_input)  # Should print "36 / 2 = 18 r. 0"

result_valid_input = run_test("12\n7\n")
print(result_valid_input)  # Should print "12 / 7 = 1 r. 5"


