# def adder(a,b):
#     return a + b
# result = adder(3, 5)
# print(result)



# def reverser(newList):
#     # Reverse the input list
#     reversedList = newList[::-1] 
#     return reversedList




def reverser(newList):
    
    reversedList = []
    for item in newList:
        reversedList.insert(0, item)
    return reversedList

# myList = [1, 2, 3, 4, 5]
print(reverser([1, 2, 3, 4, 5])) 