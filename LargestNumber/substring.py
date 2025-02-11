def length_of_last_word(s):
   
    words = s.strip().split()
   
    return len(words[-1]) if words else 0


s = "Hello World"

print(f"The length of last word  is {length_of_last_word(s)}") 
