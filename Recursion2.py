def reverse_list_recursive(list):
   
    
    if len(list) <= 1:
        return list
    else:
        # Recursive case: reverse the rest of the list and append the first element to the end
        return reverse_list_recursive(list[1:]) + [list[0]]
     

example_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list_recursive(example_list)
print("Original List:", example_list)
print("Reversed List:", reversed_list)
