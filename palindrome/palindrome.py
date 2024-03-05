

def check_if_palindrome(word):
    while " " in word:
        word=word.replace(" ","")
    
    for i in word:
        if i in ",.!@#$%^&*":
            word=word.replace(i,"")
    
    
    modified_word=word.lower()
    if modified_word==modified_word[::-1]:
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