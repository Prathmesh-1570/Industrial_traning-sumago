str = "pawar is a good boy"
# in string slicing index starting at 0 and end with (n-1)


print(str[4])                   #print the "r"

print(str[0:5])                 #print the "pawar"

print(len(str))                 #this line print the length of string

print (str[0:19:2])             #this line print the string with ignoring 2 index
                                #but considering privious index.

print(str[-4:-2])               #minus(-) slicing started from last index of string
                                #the line was printed space and b ( b)

print(str[::-2])                #this line print all string reverse and ignore 2 index.

#string slicing functions.
print(str.isalnum())              #it is check the string is an alpha numeric string,
                                #he is return false because given string is not alpha numeric
                                #spaces are include ("return false boolean value")

print(str.endswith("boy"))      #this return true because string ends with "boy"

print(str.count("o"))           #this return 3 because o in string three times.

print(str.capitalize())         #this function make first letter capital.

print(str.find("is"))           #this function finds the idex of "is"

print(str.upper())              #this function convert string into uppercase

print(str.replace("is","are"))  #this function replace given word