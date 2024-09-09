#input a word
text = str(input("enter a string = "))
#write reverse string
#using step value as - 1 to iterate in reverse
#the colun sign in py means slicing
reversetext = text[::-1]
text = reversetext
print("reverse of given string is = ", text ) 