import math

def main():
    try:
        numb=float(input("Number to check: "))
    except ValueError or numb<0:
        print("Thats not a number")
        exit()
    new_number=round(math.sqrt(numb))
    if check_perfect_square(numb,new_number):
        print(f"{numb} is a perfect square")
    else:
        print(f"{numb} is not a perfect square")


def check_perfect_square(n,nn):
    if nn**2==n:
        return True
    else:
        return False

def round(numb):
    if numb-math.trunc(numb)>=0.5:
        return math.ceil(numb)
    else:
        return math.floor(numb)

if __name__=="__main__":
    main()
    exit()