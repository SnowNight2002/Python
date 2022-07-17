k = input("k=") #input 輸入
n = []
k = int(k) #str to int 
for num in range(1,k+1):
  n.append(pow(k,num)) #append() 末尾添加新 ,pow 次方
print (n)