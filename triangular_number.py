import math


def perfect_square(num):
    new_num=math.sqrt(num)
    if new_num-math.trunc(new_num)>=0.5:
        new_num=math.ceil(new_num)
    else:
        new_num=math.floor(new_num)
    if new_num**2==num:
        return True
    else:
        return False

def main():
    while True:
        try:
            num=int(input("Enter a num: "))
            break
        except:
            print("Unvalid number")
            pass
    if perfect_square(1+8*num):
        print(f"{num} is a triangular number")
    else:
        print(f"{num} is not a triangular number")



if __name__=="__main__":
    main()
    exit()