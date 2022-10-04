# Python program to count uppercase and lowercase characters

# take input
string = input('Enter any string: ')

upper, lower = 0, 0
for i in string:
    #count lowercase characters
    if(i.islower()):
        lower = lower + 1
    #count uppercase characters
    elif(i.isupper()):
        upper = upper + 1

# print number of lowercase characters
print('Lowercase characters:',lower)
# print number of uppercase characters
print('Uppercase characters:',upper)
