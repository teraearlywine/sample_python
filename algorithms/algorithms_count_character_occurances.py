
sample_string = "Counting the character occurances in this particular string"
count_dict = {}

# Iterate over each indexed character
# First check to see if the character is in the count_dict already, and if it is add one
# Otherwise, assume it's not in the count dict and add char with initial value.
for char in sample_string: 

    if char in count_dict: 
        count_dict[char] += 1
    else:
        count_dict[char] = 1

print(count_dict)