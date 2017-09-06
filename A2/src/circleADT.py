##Mohamed Bengezi
##400021279

## @file circleADT.py
#  @author Mohamed Bengezi
#  @brief ADT for a circle, for use in DequeCircleModule.
#  @date Feb 19, 2017
import pointADT as pADT
import lineADT as lADT
import math

## @brief Local function for determing whether a point is inside a circle
#  @param p the point 
#  @param c the Circle
#  @return true(if point is inside the circle) or false
def insideCircle(p,c):
    return (p.dist(c.cen()) <= c.rad())
## @brief CircleT class for the circle ADT
class CircleT:
    ## @brief Constructor for CircleT
    #  @details Creates a Circle object
    #  @param cin The centre point
    #  @param rin The radius of the circle
    def __init__(self,cin,rin):
        self.c = cin
        self.r = rin
    ## @brief Returns the centre point of the circle
    #  @return Centre point
    def cen(self):
        return self.c
    ## @brief Returns the radius of the circle
    #  @return Radius
    def rad(self):
        return self.r
    ## @brief Returns the area of the circle using Pi*radius**2
    #  @return Area of the circle
    def area(self):
        return math.pi*self.r**2
    ## @brief Checks whether two circles intersect
    #  @details creates a new point thats in between the two circles, then checks whether the point is inside both. If it is, return True
    #  @param ci The second circle to compare
    #  @return True or False
    def intersect(self, ci):
        px = lADT.avg(ci.cen().xcrd(),self.cen().xcrd())
        py = lADT.avg(ci.cen().ycrd(),self.cen().ycrd())
        p = pADT.PointT(px,py)
        if ((insideCircle(p,ci) == True) and (insideCircle(p,self) == True)):
            return True
        return False
    ## @brief Checks whether two circles intersect
    #  @details creates a new line that connects the centre's of each circle's
    #  @param ci The second circle to connect
    #  @return The line created 
    def connection(self,ci):
        return lADT.LineT(self.c,ci.cen())
    ## @brief Calculates the force between two circles
    #  @details Uses a lambda function to accomplish this
    #  @param f The gravitational law
    #  @return The line created
    def force(self, f):
        return lambda x: self.area()*x.area()*f(self.connection(x).len())
        
        
        


