

def check_if_palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False


def main():
    word=input("Enter the word: ")
    if check_if_palindrome(word):
        print("it is a palindrome")
    else:
        print("It is not a palindrome")

if __name__=="__main__":
    main()
    exit()