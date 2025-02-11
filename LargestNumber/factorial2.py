# def factorial(n): # recursion example where function called itself, in recursion we need base case otherwise it will go for infinite.
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# number = 5

# print(f"Factorial of {number} is {factorial(number)}")  

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

number = 5
print(f"Factorial of {number} is {factorial(number)}")  

# if __name__ == "__main__":