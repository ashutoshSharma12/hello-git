#Answer Number1:
class Circle():
  def __init__(self,radius):
    self.radius = radius
  def  getArea(self):
    return 3.14*self.radius*self.radius
  def getCircumference(self):
    return self.radius*2*3.14

#Answer Number2:
class Student():
  def __init__(self,name,roll):
    self.name = name
    self.roll= roll
  def display(self):
    print self.name
    print self.roll
  def setAge(self,age):
    self.age=age
  def setMarks(self,marks):
    self.marks = marks

#Answer Number3:
class Temprature():
  def  convertFahrenhiet(self,celsius):
    return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
    return (farenhiet-32)*(5/9)

#Answer Number4:
class Moviedetails:
    def __init__(self, movie, artist, releaseyear, rating):

        self.movie = movie
        self.artist = artist
        self.releaseyear = releaseyear
        self.rating = rating

    def moviename(self):
        print("\n\n","Movie name is =>", name)

    def artistname(self):
        print("artist name is=>", artist)

    def release(self):
        print("year of release is=>", release)

    def ratingg(self):
        print("your rating for movie is =>", rating)

    def update(self, movie, artist, releaseyear, rating):

        self.movie = movie
        self.artist = artist
        self.releaseyear = releaseyear
        self.rating = rating

name=input("enter movie name=>")
artist=input("enter artist name=>")
release=input("enter year of release  of movie=>")
rating=(input("enter rating between 1 to 5"))

a=Moviedetails(name,artist,release,rating)
a.moviename()
a.artistname()
a.release()
a.ratingg()


name=input("enter movie name=>")
artist=input("enter artist name=>")
release=input("enter year of release  of movie=>")
rating=(input("enter rating between 1 to 5"))

a.update(name,artist,release,rating)
a.moviename()
a.artistname()
a.release()
a.ratingg()

#Answer Number5:
class Animal:
   def animal_attribute(self,name,atri):
       print(name," has attribute to ",atri)

class Tiger(Animal):
   def show_attribute(self,name,atri):
       self.animal_attribute(name,atri)

T = Tiger()
T.show_attribute("Tiger","roar")

#Answer Number6:
class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'
a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()
###OUTPUT
A B
A B###

#Answer Number 7:
class Shape:
   length=int()
   breadth=int()
   def area(self,l,b):
       self.length=l
       self.breadth=b
       return self.length*self.breadth

class Rectangle(Shape):
   def display_area(self):
      l=int(input("Enter length of rectangle: "))
      b=int(input("Enter breadth of rectangle: "))
      print("Area of Rectangle: ",self.area(l,b))

r= Rectangle()
r.display_area()

class Square(Shape):
   def display_area(self):
      a=int(input("Enter side length of square: "))
      print("Area of Rectangle: ",self.area(a,a))

s= Square()
s.display_area()
