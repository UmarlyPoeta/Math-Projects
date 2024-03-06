import math



def is_armstrong_number(number):
    if number<0:
        if (len(str(number))-1)%2!=0:
            number=abs(number)
        else:
            return False
    number=str(number)
    n_of_digits=len(number)
    sum=0
    for i in range(n_of_digits):
        sum=sum+int(math.pow(int(number[i]),n_of_digits))
    
    if sum==int(number):
        return True
    else:
        return False
    

def main():
    try:
        number=int(input("Enter the number: "))
    except:
        print("Invalid number")
        exit()
    if is_armstrong_number(number):
        print("It is an armstrong number")
    else:
        print("It is not an armstrong number")


if __name__=="__main__":
    main()
    exit()