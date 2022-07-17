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

class Circle (Shape):
 __pi=3.1416
 __radius=0
 def __init__(self,__radius,):
  self.__radius=__radius
  
 def areaCircle(self):
    self.areaCircle = self.__pi*self.__radius*self.__radius
    print("Area of Circle:","{:.2f}".format(self.areaCircle))

 def circumferenceCircle(self):
    self.CircumferenceCircle = self.__pi*self.__radius*2
    print("Circumference of Circle:","{:.2f}".format(self.CircumferenceCircle))

class Rectangle (Shape):

  def Rectangle(self):
    print("area:",self.area)
    print("circumference:",self.circumference)