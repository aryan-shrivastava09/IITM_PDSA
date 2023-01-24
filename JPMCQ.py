from math import sqrt, pi, asin
import scipy.integrate as sci

class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        

class Rectangle():
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def __str__(self) -> str:
        return f"({self.p1.x1},{self.p1.y1})  ({self.p2.x1},{self.p2.y1})  ({self.p3.x1},{self.p3.y1})  ({self.p4.x1},{self.p4.y1})"
     

def areaRatio(n, R=10):
    # We assume the centre of first circle to be at origin
    circle = lambda x: sqrt(R*R - x*x)
    ## Therefore, points of Rectangle :
    p1 = Point(-1*R, R)
    p2 = Point(-1*R, -1*R)
    p3 = Point((2*n-1)*R, -1*R)
    p4 = Point((2*n-1)*R, R)
    ## Making the rectangle object.
    r = Rectangle(p1, p2, p3, p4)
    # print("Rectangle: ", r)
    ## Diagonal line equation
    s = (p2.y1 - p4.y1) / (p2.x1 - p4.y1)
    eq = lambda x1: s*(x1- p2.x) + p2.y
    ## now point of intersection of circle and diagonal line
    x_intersect =( ((n-1)*2*R) - sqrt(4*R*R*((1-n)*(1-n) - (n*n+1)*(1-2*n))) ) / (2*n*n+2)
   
    int1 = lambda x: (x*sqrt(R*R - x*x)/2 + (R*R/2)*asin(x/R))
    int2 = lambda x: x*x/(2*n)
    int3 = lambda x: x*(R/n - R)

    double_integration = -1*(int1(x_intersect)-int1(-R) + int2(x_intersect)-int2(-R) + int3(x_intersect)-int3(-R))
    area_a_b = R*R - (pi*R*R)/4

    return double_integration/area_a_b

print(areaRatio(n=3))

def findLeast(p):

    c = 0
    n=1
    while c <= p:
        c = areaRatio(n)
        n+=1
    return n-1

print("50% :",findLeast(0.5))
print("70% :", findLeast(0.7))
print("90% :", findLeast(0.9))
print("99.9% :", findLeast(0.999))
print("99.99% :", findLeast(0.9999))
print("100% :", findLeast(0.999999))