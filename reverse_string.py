# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str

# string = "How are you today?"
# reversed_string = reverse_string(string)
# print(reversed_string)  


# s = "Hussain"
# print(s[::-1]) # start,stop and step

def rev(word):
    x = ""
    for i in range(len(word)-1,-1,-1):
        x += word[i]
    return x

if __name__ == "__main__":
    print(rev("somestring"))
    


