from enum import unique
from numpy import intersect1d


tom={"Basketball", "Reading", "Hiking"}
peter={"Football", "Singing", "Reading", "Hiking"}
mary={"Reading", "Swimming", "Cooking"}

#(a)
print("This is part a")
unionResult = tom.union(peter).union(mary)
print(f"Total {len(unionResult)} different hobbies of these 3 people:")
print(unionResult)


#(b)
print("This is part b")
intersectResult = tom & peter & mary
print(f"Total {len(intersectResult)} common hobbies of these 3 people:")
print(intersectResult)


#(c)
print("This is part c")
uniqueHobbies = unionResult - (tom & peter) - (peter & mary) - (mary & tom)
print(f"Total {len(uniqueHobbies)} unique hobbies of these 3 people:")
print(uniqueHobbies)