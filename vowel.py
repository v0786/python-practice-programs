letter = input("input a letter of the alphabet: ")

if letter in ('a','e','i','o','u'):
    print("%s is a vowel." % letter)
elif (letter == 'y'):
    print("sometimes letter y stand for vowel, sometimes stand for consotant.")
else:
    print("%s is a consonant." % letter)