import math
class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        if a+b<c or c+a<b or c+b<a:
            raise ValueError("Triangle does not excist")
    def sides(self):
        return self.a,self.b,self.c
    def perimeter(self):
        return self.a+self.b+self.c
    def area(self):
        return ((self.perimeter()/2)*(self.perimeter()/2-self.a)*(self.perimeter()/2-self.b)*(self.perimeter()/2-self.c))**0.5
    def type(self):
        if self.a==self.b!=self.c or self.c==self.b!=self.a or self.c==self.a!=self.b:
            return "Isosceles triangle"
        elif self.a==self.b==self.c:
            return "Equilateral triangle"
        else:
            return "Iregular triangle"
    def right_triangle(self):
        if self.a**2+self.b**2==self.c**2 or self.c**2+self.b**2==self.a**2 or self.c**2+self.a**2==self.b**2:
            return "Yes"
        else:
            return "No"
    def angles(self):
        angle_a=math.degrees(math.acos((self.b**2+self.c**2-self.a**2)/(2*self.b*self.c)))
        angle_b = math.degrees(math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c)))
        angle_c = math.degrees(math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b)))
        return angle_a,angle_b,angle_c
    def inscribed_circle(self):
        r=2*self.area()/self.perimeter()
        return r
    def circumscribed_circle(self):
        R=(self.a*self.b*self.c)/(4*self.area())
        return R
    def all(self):
        print(f"Sides: {self.sides()}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")
        print(f"Type: {self.type()}")
        print(f"Is a right Triangle?: {self.right_triangle()}")
        print(f"Angles: {self.angles()}")
        print(f"Inscribed circle: {self.inscribed_circle()}")
        print(f"Circumscribed circle: {self.circumscribed_circle()}")
e=Triangle(5,12,13)
print(e.all())

