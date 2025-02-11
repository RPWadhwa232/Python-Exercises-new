#names = ["Jack", "Hussain", "Rash"]
#print = names[0] 


# fruits = ["kiwi", "dragonfruit", "durian", "starfruit"]
# for fruit in fruits: # after the colon we use indentation compared to c#, whereas we use {}
#     if fruit == "durian":
#         print("Ew that stinks, its tasty tho")
#     else:
#         print("Nice")
#     # print(fruit) # it starts new process by printing every element.



#a=[[1,2,3],[4,5,6],[7,8,9]]
#print(a[0], a[1])


twodarray = [[1,2,3],[4,5,6],[7,8,9]]
#print(twodarray[2][0]) # another example to retrieve 7 using nested loops
for i in twodarray:
    # print(i) # This will print every list
    for j in i:
        if j == 7:
            print("7 has been found")
        else:
            print(j, " is not 7")
        # print(j) # print every value individually, we create another loop