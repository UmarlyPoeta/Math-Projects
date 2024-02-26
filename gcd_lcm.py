
def gcd(x,y):
    if x==y:
        return x
    elif x>y:
        return gcd(abs(x-y),y)
    else:
        return gcd(x,abs(y-x))
        
def main():
    while True:
        try:
            number1=int(input("Enter the first number: "))
            number2=int(input("Enter the second number: "))
            break
        except:
            print("unvalid number")
            pass
    div=gcd(number1,number2)
    print(f"Greatest common divisor of {number1} and {number2} is {div}")
    print(f"Least common multiple of {number1} and {number2} is a {number2*number1//div}")
    

if __name__=="__main__":
    main()