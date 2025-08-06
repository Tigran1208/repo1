
class Calculator:
    def __init__(self,number):
        if not isinstance(number,int|float):
            raise TypeError("Enter the number correctly")
        self.__number=number

    @property
    def number(self):
        return self.__number

    def __add__(self,other):
        if isinstance(other,Calculator):
            other=other.__number
        return Calculator(self.__number+other)

    def __radd__(self,other):
        return self+other

    def __iadd__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number+=other
        return self
    
    def __sub__(self,other):
        return Calculator(self.__number-other)

    def __rsub__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(other-self.number)

    def __isub__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number-=other
        return self

    def __mul__(self,other):
        if isinstance(other,Calculator):
            other=other.__number
        return Calculator(self.number*other)

    def __rmul__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        return self *other

    def __imul__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number*=other
        return self

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number/other)

    def __rtruediv__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(other/self.__number)

    def __itruediv__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number/=other
        return self

    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number//other)

    def __rfloordiv__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(other//self.__number)

    def __ifloordiv__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number//=other
        return self

    def __mod__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number%other)

    def __rmod__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(other%self.__number)

    def __imod__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number%=other
        return self

    def __pow__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.number**other)

    def __rpow__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(other**self.__number)

    def __ipow__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number**=other
        return self

    def __eq__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number=other

    def __lt__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number<other

    def __le__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number<=other

    def __ge__(self,other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__other>=other

    def __str__(self):
        return f"{self.__number}"

    def __repr__(self):
        return f"{type(self.__number)}"

a=Calculator(4)
b=Calculator(3)
print(a+b)
print(a+4)
print(5+a)
print(a-5)
print(5-a)
a+=b
print(a)
print(a*b)
print(a**b)


