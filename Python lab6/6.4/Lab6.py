class Shape:
   def area(self):
      pass
   def circumference(self):
      pass

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
 _width=0
 _height=0
 def __init__(self,width,height):
     self._width = width
     self._height = height

 def area(self):
  self.area = self._height * self._width
  print("area:",self.area)

 def circumference(self):
  self.circumference = 2*(self._height+self._width)
  print("circumference:",self.circumference)

class Square (Rectangle):
  side=0
  def __init__(self,side):
     self.side = side
  def Square(self):
    self.square=pow(self.side,2)
    print("Area of Square:",self.square)
    self.square=self.side*4
    print("Circumference of Square:",self.square)