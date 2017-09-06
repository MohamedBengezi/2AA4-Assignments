##Mohamed Bengezi
##400021279

## @file lineADT.py
#  @author Mohamed Bengezi
#  @brief ADT for a line, for use in circleADT.
#  @date Feb 19, 2017
import pointADT as pADT
import math

## @brief Local function for calculating the average
#  @param x1 First number
#  @param x2 Second Number
#  @return the average of x1 and x2
def avg(x1,x2):
    return ((x1 + x2)/2.0)
## @brief LineT class for the line ADT
class LineT:
    ## @brief Constructor for LineT
    #  @details Creates a line object
    #  @param p1 The starting point
    #  @param p2 The end point
    def __init__(self,p1,p2):
        self.b,self.e = p1, p2
    ## @brief Returns the beginning point object
    #  @return Beginning point 
    def beg(self):
        return self.b
    ## @brief Returns the ending point object
    #  @return Ending point 
    def end(self):
        return self.e
    ## @brief Returns the length of the line
    #  @details Uses the dist function in pointADT
    #  @return length of the line
    def len(self):
        return self.b.dist(self.e)
    ## @brief Returns the midpoint of the line
    #  @details Uses the avg function and calculates the avg of the x's and y's
    #  @return The midpoint of the line
    def mdpt(self):
        mdptx = avg(self.b.xcrd(),self.e.xcrd())
        mdpty = avg(self.b.ycrd(),self.e.ycrd())
        return pADT.PointT(mdptx,mdpty)
    ## @brief Rotates the line by angle theta(radians)
    #  @details Rotation occurs about the origin, ccw
    #  @param theta The angle of rotation
    def rot(self,theta):
        self.b.rot(theta)
        self.e.rot(theta)


