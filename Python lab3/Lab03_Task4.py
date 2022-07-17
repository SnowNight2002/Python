def wordToChar(word):
 return list(word)

color = ['Red', 'Blue', 'Black'] 
print("Original list: ")
print(f"{color}") 
print("\nAfter listify the list of strings are:") 
result =list(map(wordToChar,color)) 
print(result)
