import math


def egyptian_multiplication(number1,startB):
    startA=1
    listofA=[]
    listofB=[]
    while startA<number1:
        listofA.append(startA)
        listofB.append(startB)
        startA*=2
        startB*=2
    
    result=0
    for z,i in enumerate(listofA[::-1]):
        if number1-i>=0:
            number1-=i
            result+=listofB[len(listofB)-(z+1)]
            
    return result
        



def main():
    try:
        number1=int(input("Enter first number: "))
        number2=int(input("Enter second number: "))
        if number1<=0 or number2<=0:
            raise ValueError
    except:
        print("invalid number")
        exit()
    result=egyptian_multiplication(number1,number2)
    print(f"{number1} x {number2} = {result}")
    
    
if __name__=="__main__":
    main()
    exit()