#how many times in character in string
#check if it is a palindrome
#convert to same case 
#reverse string, check if the same


def count_letters (str1,char):
    counter = 0
    str1=str1.lower()
    char = char.lower()
    for c in str1:
       if char == c:
            counter += 1   
    return counter
    
str1 = input("Enter a word: ")
char = input ("Enter a letter: ")
print(count_letters(str1,char))


def palindrome(str1):
    str1 = str1.lower()
    revstr = ""
    for c in str1:
        revstr = c + revstr
    if str1 == revstr:
        return True
    else: return False

str1 = input("Enter a word to check if it is a palindrome: ")
print(palindrome(str1))







