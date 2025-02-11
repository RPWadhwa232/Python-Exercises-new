def single_number(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Find the number with count 1
    for num, freq in count.items():
        if freq == 1:
            return num

nums = [4, 2, 2, 1, 1]
print(single_number(nums))  



# def single_number(nums):
#     result = 0
#     for num in nums:
#         result ^= num  # XOR each number with result
#     return result

# nums = [4, 2, 2, 1, 1]
# print(single_number(nums)) 
