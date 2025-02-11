grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


sum = 0
for i in grid: # Sum each row and then sum the results
    for j in i:
        sum = sum+j
print(sum)



# def sum_2d_array(grid):
#     for row in grid: # Sum each row and then sum the results
#         # for j in row:
#         output = sum(sum(row) for row in grid)  
#         return output    
        
# result = sum_2d_array(grid)
# print(result)



# def sum2darray(twodarray):
# sum = 0
# for i in grid: # Sum each row and then sum the results
#     for j in i:
#         sum = sum+j
# return sum

# print(sum2darray)