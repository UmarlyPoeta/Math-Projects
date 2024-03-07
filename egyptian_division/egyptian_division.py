

def main():
    try:
        number1=int(input("Enter first number: "))
        number2=int(input("Enter second number: "))
        if number1<=0 or number2<=0 or number2>number1:
            raise ValueError
    except:
        print("invalid number")
        exit()
    a=number1
    b=number2
    startA=1
    listofA=[]
    listofB=[]
    while b<a:
        listofA.append(startA)
        listofB.append(b)
        startA*=2
        b*=2
    
    tmp_a=a
    sum=0
    quotient=0
    for z,i in enumerate(listofB[::-1]):
        if tmp_a-i>=0:
            tmp_a-=i
            sum+=listofB[len(listofB)-(z+1)]
            quotient+=listofA[len(listofA)-(z+1)]
    
    remainder=a-sum
    print(f"{number1} / {number2} = {quotient} r. {remainder}")
    
    
if __name__=="__main__":
    main()
    exit()