# # remove a given word from list
# words = [" apple ", "banana", " orange ", "grape ", "apple"]
# word_to_remove = "apple"
# clean_list = [word.strip() for word in words if word.strip() != word_to_remove]

# print(clean_list) 
def greet(name = "stranger"): 
    return name
something=greet() # name will be "stranger" in function body (default) 
print(something)
something=print(greet("harry")) 
