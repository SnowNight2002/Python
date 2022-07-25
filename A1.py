phoneBook = {"Peter": "24368567", "Amy": "28813991", "Ellen": "95668766"}

# Search tel no. by name
searchName = "Ellen"
if searchName in    phoneBook.keys():  #(a)       # if searchName is found in the phone book
    print( f"Tel no. is {phoneBook [searchName]}" )    # (b) show the telephone no. of searchName
else:
    print("Names is not found")

# Search name by tel no.
searchTel = "28813991"
result = "Tel no. is not found"
for name, tel in    phoneBook.items()  : #(c)
    if    tel == searchTel   :    # (d)  if searchTel is found in the phone book
        result = f"Name is {name}"         #(e)  show the name of searchTel
        break
print(result)




#"Peter": "24368567" = .items()
# "Peter" = .keys()
