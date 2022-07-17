
def num(num):
 return num>=75

scores = [47, 30, 68, 74, 75, 68, 86, 73, 82, 100]
newlist = list(filter(num,scores))
print(newlist)