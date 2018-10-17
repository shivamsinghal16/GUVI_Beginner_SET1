x = input("Enter a character : ")

vowels = ['a','e','i','o','u','A','E','I','O','U']

if((x >= 'A' and x<= 'Z') or (x >= 'a' and x<= 'z')):
    if x in vowels:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
