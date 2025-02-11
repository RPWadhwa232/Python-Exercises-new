# def greeting(counter): #function can take parameters
#     if counter < 10:
#         print("Hello World")
#         greeting(counter+1) # function calling itself indefinetely
#     else:
#         return # end the code

# greeting(0)

# recursion starts backwards

def greeting(counter): #function can take parameters
    if counter > 10: # it goes until it hit the base case
        return
    else:
        print("Hello World")
        greeting(counter+1) # function calling itself indefinetely
    

greeting(0)
