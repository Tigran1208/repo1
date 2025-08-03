# from abc import ABC,abstractmethod
# import math
# class Shape(ABC):
#     @abstractmethod
#     def __init__(self):
#         ...
#     def perimetr(self):
#         ...
#     def area(self):
#         ...
# class Circle(Shape):
#     def __init__(self,radius):
#         if not isinstance(radius,int):
#             print("Raduis must be integer")
#         self.radius=radius
#     def perimetr(self):
#         p1=2*math.pi*self.radius
#         print(f"Perimetr of circle is {p1}")
#
#     def area(self):
#         a1=math.pi*(self.radius)**2
#         print(f"Area of circle is {a1}")
# class Rectangle(Shape):
#     def __init__(self,height,lenght):
#         if not isinstance(height,int) and isinstance(lenght,int):
#             print("Height and weight must be integers")
#         self.height=height
#         self.lenght=lenght
#     def perimetr(self):
#         p2=2*self.height+2*self.lenght
#         print(f"Perimetr of rectangle is {p2}")
#     def area(self):
#         a2=self.height*self.lenght
#         print(f"Area of rectange is {a2}")
# class Triangle(Shape):
#     def __init__(self,a=None,b=None,c=None,h=None,angle=None):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.h=h
#         self.angle=angle
#     def check(self):
#         if not isinstance(self.a, int) and isinstance(self.b, int) and isinstance(self.c, int) and isinstance(self.h, int) and isinstance(self.angle, int | float):
#             print("Print parameters right!")
#     def perimeter(self):
#         p3=self.a+self.b+self.c
#         print(f"Perimeter of triangle is {p3}")
#     def area(self):
#         if self.a!=None and self.b!=None and self.c!=None:
#              p3 = self.a + self.b + self.c
#              P = p3 / 2
#              a3=(P*(P-self.a)*(P-self.b)*(P-self.c))**0.5
#              print(f"Area of triangle is {a3}")
#         elif self.a!=None and self.h!=None or self.b!=None and self.h!=None or self.c!=None and self.h!=None:
#             a3=self.a*self.h/2 or self.b*self.h/2 or self.c*self.h/2
#             print(f"Area of triangle is {a3}")
#         elif self.a!=None and self.b!=None and self.angle!=None or  self.c!=None and self.b!=None and self.angle!=None or self.c!=None and self.a!=None and self.angle!=None:
#             a3=self.a*self.b*math.sin(self.angle)/2 or self.c*self.a*math.sin(self.angle)/2 or self.c*self.b*math.sin(self.angle)/2
#             print(f"Area of triangle is {a3}")
# c=Circle(5)
# c.area()
# c.perimetr()
# r=Rectangle(4,5)
# r.area()
# r.perimetr()
# t=Triangle(a=3,b=3,c=3)
# t.perimeter()
# t.area()

#
#
# class MyShows:
#     def __init__(self,name,platform,year,number_of_episode=1,rating=None,actors_list=[ ]):
#        if  not isinstance(name,str):
#            raise ValueError("Enter the name of series correctly(name must be a text)")
#        if not isinstance(platform,str):
#            raise ValueError("Enter the name of platform correctly(name must be a text)")
#        if not isinstance(year, int):
#               raise ValueError("Enter the year correctly(year must be a positive)")
#        if rating is not None:
#          if not isinstance(rating, int) and  1<=rating<=10:
#            raise ValueError("Enter the rating correctly( must be a text)")
#        if not isinstance(number_of_episode, int):
#            raise ValueError("Enter number of episode correctly(number of episode must be a positive)")
#        if not isinstance(actors_list, list):
#            raise ValueError("Enter actors names correctly( actors names must be in list)")
#        self.__name=name
#        self.__platform=platform
#        self.__year=year
#        self.__number_of_episode=number_of_episode
#        self.__rating=rating
#        self.__actors_list=actors_list
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def platform(self):
#         return self.__platform
#     @property
#     def year(self):
#         return self.__year
#     @property
#     def num_of_ep(self):
#         return self.__number_of_episode
#     @property
#     def rating(self):
#         return self.__rating
#     @property
#     def actors(self):
#         return self.__actors_list
#     @num_of_ep.setter
#     def num_of_ep(self,value):
#         self.__num_of_ep=value
#     @rating.setter
#     def rating(self,value):
#         self.__rating=value
#     @rating.deleter
#     def rating(self):
#         del self.__rating
#     def add_actor(self,actor_name):
#         if not isinstance(actor_name,str):
#             raise ValueError("Actor name must be text")
#         if actor_name not in self.__actors_list:
#             self.__actors_list.append(actor_name)
#     def remove_actor(self,actor_name):
#         if not isinstance(actor_name, str):
#             raise ValueError("Actor name must be text")
#         if actor_name  in self.__actors_list:
#             self.__actors_list.remove(actor_name)
#         else:
#             print("Actor name not in list")
#     def info(self):
#         print(f"Series: {self.__name}")
#         print(f"Platform: {self.__platform}")
#         print(f"Year: {self.__year}")
#         print(f"Number of episode: {self.__number_of_episode}")
#         print(f"Rating: {self.__rating}")
#         print(f"Actors: {self.__actors_list}")
# series=MyShows("The killer","Netflix",2023,1,5,["Charles Parnel","Gabriel Martineli"])
# series.remove_actor("Gabriel Martineli")
# series.add_actor("Leonardo Trossard")
# series.info()
