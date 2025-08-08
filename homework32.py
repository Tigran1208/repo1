class MyList:
    def __init__(self,argument=None):
        if argument is None:
            self.l=[]
        self.l=list(argument)

    def __getitem__(self, item):
        return self.l[item]

    def __setitem__(self, key, value):
        self.l[key]=value

    def __delitem__(self, item):
        del self.l[item]

    def len(self):
        return len(self.l)

    def append(self,item):
        self.l.append(item)

    def remove(self,item):
        if item not in self.l:
            raise TypeError("Item not in list")
        self.l.remove(item)

    def pop(self,item=-1):
        return self.l.pop(item)

    def reverse(self):
        self.l.reverse()

    def summa(self):
        return sum(self.l)

    def sort(self):
        self.l.sort()

    def clear(self):
        self.l.clear()

    def extend(self,argument):
        self.l.extend(argument)

    def insert(self,item1,item2):
        self.l.insert(item1,item2)

    def first_item(self):
        return self.l[0]

    def last_item(self):
        return self.l[-1]

    def __str__(self):
        return str(self.l)

    def __repr__(self):
        return f"List:{self.l}"


m=MyList([1,23,334])
m.append(5)
m.remove(1)
m.reverse()
m.sort()
m.extend("a")
m.insert(2,6)
print(m.first_item())
print(m.last_item())
print(m)