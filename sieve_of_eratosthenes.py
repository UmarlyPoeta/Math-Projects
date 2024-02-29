import math


def sieve_of_era(n,numbers):
    for i in numbers[:int(math.sqrt(n))]:
        trial=i**2
        while trial<=n:
            if trial in numbers:
                numbers.remove(trial)
            trial +=i
    return numbers



def main():
    while True:
        try:
            n=int(input("enter how many numbers to check: "))
            break
        except:
            continue
    numbers=[i for i in range(2,n+1)]
    prime_numbers=sieve_of_era(n,numbers)
    print(f"Here is a list of prime numbers below a given number: \n {prime_numbers}")
    
            


if __name__=="__main__":
    main()
    exit()