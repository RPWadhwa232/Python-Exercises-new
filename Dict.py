# dict = {"name": "Tom", "occupation":"student"} # curly barckets to definde dict
# print(dict["name"])
# dict["name"] = "Tayyab"
# dict["occupation"] ="lecturer"
# print(dict)

def word_frequency(text):
   
    word_counts = {}
    words = text.split()
    
    for word in words:
        # text = text.replace("!", "").replace(",","")  
        
        word = word.strip("!?.").lower()  
        # Remove punctuation and make it lowercase
        if word in word_counts:
            word_counts[word] += 1  
        else:
            word_counts[word] = 1  
    
    return word_counts

text = "Hello world! Hello everyone."
result = word_frequency(text)
print(result)