
nums = [3, 40, 54, 62, 93, 98]
#sortedList = sorted(newList, reverse = True)
#print(sortedList)
tempNums = []

# Convert the number to a string to access each digit
number_str = str(tempNums)
  
for i in nums: # i takes the current value in the list
    digits = len(str(i))
    if digits == 1:
        x = i*1
        tempNums.append(x)
    else:
        tempNums.append(i)

tempNums = sorted(tempNums, reverse=True)


sortedNumber = int("".join(map(str, tempNums)))
# print(big_number)

print(sortedNumber)
