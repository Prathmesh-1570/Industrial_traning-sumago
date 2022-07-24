# Write a python program to multiplies all the items in the list.

def multiplying_List(user_List) :
     
    # Multiply elements one by one
    result = 1
    for x in user_List:
         result = result * x
    return result
     
# importing list 
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# return the multiplied result
print(multiplying_List(list2))