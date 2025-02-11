# Factorial using recursion

# If n>0, it's positive.
# If n<0, it's negative.
# If n=0, it's zero.

# def check_integer(n):
    
#     if n > 0:
#         return f"The number {n} is positive."
#     elif n < 0:
#         return f"The number {n} is negative."
#     else:
#         return "The number is zero."

# # Example usage
# number = int(input("Enter an integer: "))
# result = check_integer(number)
# print(result)


def check_integer(n):
    
    # param n: A non-negative integer
    # return: The factorial of n
    
    if n <= 1:  # Base case
        return 1
    return n * check_integer(n - 1)  # Recursive call

number = int(input("Enter an integer: "))
result = check_integer(number)
print(result)


