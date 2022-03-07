# attribute: a method or a instance variable

class Point: # class Point(object):
    # Inherited methods: __new__() __init__() __repr__() __eq__()
    def __init__(self, x, y):
        
        self.x=x # self.x is a "data attribute" or "instance variable" or "a field"
        self.y=y
        self.__secret =100
    def __repr__(self): # __str__()
        #return "<"+str(self.x)+","+str(self.y)+">"
        #return "<{},{}>".format(self.x, self.y)
        #return "<%d,%d>" % (self.x, self.y)
        return f"<{self.x},{self.y}>" # >= 3.6
    def __eq__(self, other): # __ne__
        return self.x==other.x and self.y==other.y and self.__secret==other.__secret
    def __add__(self, other): # + operator
        return Point(self.x+other.x, self.y+other.y)
    
    def distance(self, other):
        import math
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    def clear(self):
        self.x=self.y=0

if __name__ == "__main__":
    p1=Point(2,3)
    print(p1._Point__secret)
    p2=Point(5,7)
    l1=[p1,p2]
    print(p1.__dict__)
    print(p1)
    print(l1)
    