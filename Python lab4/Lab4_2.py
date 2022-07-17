from math import prod
#(a)
print("This is part A")
cart = {'P017': 3, 'P721': 1, 'P187': 4}
#print(cart.keys())
#print('P017' in cart.keys())
items = (('P017', 1), ('P359', 2))
for prodID, Qty in items:
 if prodID in cart.keys():
     cart[prodID] = cart[prodID] + Qty #cart and items number add together
 else:
     #print("Product ID is not found")
     cart[prodID] = Qty   #add items to cart
print("ID   | Qty" )
for prodID in sorted(cart.keys()): # sorted() 排序
    print("----------" ) 
    print(prodID," |",cart[prodID])

#(b)
print("This is part B")
prices = {'P005': 42.7, 'P017': 29.9, 'P187': 78.1,
          'P286': 95.3, 'P359': 72.4, 'P427': 21.7,
          'P721': 71.8}
sum = 0.00
for prodID in sorted(cart.keys()): 
 if prodID in prices.keys():
     a=(prices[prodID] * cart[prodID]) 
     sum += a
     print(f"Subtotal of ",prodID,":",prices[prodID],"*",cart[prodID],"=",a)
print("{:.2f}".format(sum))
#print(f"{sum:.2f}")