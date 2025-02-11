# Factorial using recursion

def check_integer(n):
    
    # param n: A non-negative integer
    # return: The factorial of n
    
    if n <= 1:  # Base case
        return 1
    return n * check_integer(n - 1)  # Recursive call

number = int(input("Enter an integer: "))
result = check_integer(number)
print(result)


