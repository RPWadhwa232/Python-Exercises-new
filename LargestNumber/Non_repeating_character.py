# def non_repeating_char(list):

# # count occurrence
#     counts = [0] * 256
#     for char in s:
#         counts[ord(char)] +=1

# # find the non_repating
#     for index, char in enumerate(s):
#         if counts[ord(char)] == 1:
#             return index
    
# print(non_repeating_char("leetcode"))  
# print(non_repeating_char("loveleetcode"))  
# print(non_repeating_char("aaaccc")) 
def stringer(s):

    for char in s:
        if s.count(char) == 1:
            print(s.find(char))
            break
    else:
        pass
    return -1

def countCreator(s):
    letterCount = {}
    for i in range(len(s)):
        counter = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                counter+=1
        letterCount[s[i]] = counter
    return letterCount




s = "eetcode"
print(countCreator(s))
#stringer(s) # This works with the first function.
  




   