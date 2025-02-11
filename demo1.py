def add(num1, num2):
 return num1 + num2

def multiply(num1, num2):
    num3 = 0
    for i in range(0,num2):
        num3 = add(num3, num1)
    return num3


def power(num1, num2):
    num3 = 1
    for i in range(0,num2):
        print(num3)
        num3 = multiply(num3, num1)
    return num3

# if __name__ == "__main__":

num1 = int(input("Enter first num "))
num2 = int(input("Enter second num "))
output = multiply(num1,num2)
print(output)


