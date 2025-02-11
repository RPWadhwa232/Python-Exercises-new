def add(a, b):
    result = a
    if b >= 0:
        for _ in range(b):  # Increment `a` by 1, `b` times
            result += 1
    else:
        for _ in range(abs(b)):  # Decrement `a` by 1, |b| times
            result -= 1
    return result

def multiply(a, b):
    result = 0
    is_negative = b < 0  # Track if the result should be negative
    b = abs(b)  # Work with the absolute value of `b`
    for _ in range(b):  # Add `a`, `b` times
        result = add(result, a)
    return -result if is_negative else result

def exponent(a, b):
    if b == 0:
        return 1 
    result = a
    for _ in range(b - 1):  # Multiply `a` by itself, `b-1` times
        result = multiply(result, a)
    return result

x, y = 3, 4
print("Addition:", add(x, y))       # 3 + 4 = 7
print("Multiplication:", multiply(x, y))  # 3 * 4 = 12
print("Exponentiation:", exponent(x, y))  # 3^4 = 81

    
