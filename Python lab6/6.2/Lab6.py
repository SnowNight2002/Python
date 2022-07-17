class Shape:
 __width=0
 __height=0
 def __init__(self,__width,__height):
     self.__width = __width
     self.__height = __height

 def area(self):
  self.area = self.__height * self.__width
  print("area:",self.area)

 def circumference(self):
  self.circumference = 2*(self.__height+self.__width)
  print("circumference:",self.circumference)

class Rectangle (Shape):

  def Rectangle(self):
    print("area:",self.area)
    print("circumference:",self.circumference)