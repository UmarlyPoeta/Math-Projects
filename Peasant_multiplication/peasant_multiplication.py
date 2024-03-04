import math

def peasant_multiplication(num1, num2, s=0):
    if num1 % 2 != 0:
        s += num2
    if num1 == 1:
        return s
    return peasant_multiplication(num1 // 2, num2 * 2, s)

def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid number")
        return
    
    result = peasant_multiplication(num1, num2)
    print(f"{num1} x {num2} = {result}")

if __name__ == "__main__":
    main()
    exit()
