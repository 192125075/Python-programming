def findReverse(string):  
   reverse = string[::-1]
   return reverse
string = input('Enter the string: ')
reverse = findReverse(string)
print('The reverse string is', reverse)
