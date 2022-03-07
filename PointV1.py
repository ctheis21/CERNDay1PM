# attribute: a method or a instance variable

class Point: # class Point(object):
    # Inherited methods: __new__() __init__() __repr__() __eq__()
    def __init__(self, x, y):
        
        self.x=x # self.x is a "data attribute" or "instance variable" or "a field"
        self.y=y
    def __repr__(self): # __str__()
        #return "<"+str(self.x)+","+str(self.y)+">"
        #return "<{},{}>".format(self.x, self.y)
        #return "<%d,%d>" % (self.x, self.y)
        return f"<{self.x},{self.y}>" # >= 3.6
    def __eq__(self, other): # __ne__
        return self.x==other.x and self.y==other.y
    def __add__(self, other): # + operator
        return Point(self.x+other.x, self.y+other.y)
    
    def __setattr__(self, name, value):
        if name not in ["x", "y"]:
            raise Exception("Wrong attribute name")
        if not isinstance(value, (int, float)):
            raise Exception("Wrong attribute value")
        self.__dict__[name]=value
    def __delattr__(self, name):
        raise Exception("You cannot delete an attribute")
              
    def distance(self, other):
        import math
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    def clear(self):
        self.x=self.y=0

if __name__ == "__main__":
    p1=Point("abc",3)
    # 1) p1=Point.__new__()
    # 2) p1.__init__(2,3)
    # 3) __init__(p1,2,3)
    p2=Point(5,7)
    l1=[p1,p2]
    print(p1.__dict__)
    print(f"l1: {l1}")
    p1.x=5
    # 1) p1.__setattr__("x", "abc")
    p1.x=23
    
    # 1) p1.__setattr__("hkjkjh", 89)
    
    del p1.y
    # 1) p1.__delattr__("y")
    
    print(p1) # <5,7>
    print(p1.x)
    p1.y=7
    print(p1.y)
    print(p1) # <5,7>
    # 1) print(str(p1))
    # 2) print(p1.__repr__())
    
    p2=Point(5,7)
    
    print(p1==p2) # True
    print(p1.__eq__(p2)) # True
    
    p3=p1+p2 # p3=p1.__add__(p2)
    print(p3) # <10,14>
    
    result=p1.distance(p3)
    print(result)
    
    p1.clear()
    print(p1) # <0,0>
    
    len(l1) # <=> l1.__len__()
    print(p3 in l1) # <=> l1.__contains__(p1)


