import math

factors=[]
primefactors=[]
def divison(number):
    for i in range(2,number):
        if number%i==0:
            factors.append(i)


def primes():
    for i in factors:
        if i==2:
            primefactors.append(i)
            continue
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            primefactors.append(i)

def main():
    while True:
        try:
            number=int(input("Enter the number: "))
            break
        except:
            pass
    divison(number)
    primes()
    print(factors)
    print(primefactors)
    print(f"Prime factors of number {number}: {primefactors}")
        



if __name__=="__main__":
    main()
    exit()