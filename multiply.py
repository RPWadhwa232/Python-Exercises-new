

def multiply_all(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = [8, 2, 3, -1, 7]
print(multiply_all(numbers))  
