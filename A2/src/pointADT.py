##Mohamed Bengezi
##400021279

## @file pointADT.py
#  @author Mohamed Bengezi
#  @brief ADT for a point, for use in lineADT and circleADT.
#  @date Feb 19, 2017
import math

class PointT:
    ## @brief Constructor for pointT
    #  @details Creates a point with coordinates x and y
    #  @param x  x-coordinate of point
    #  @param y y-coordinate of poin
    def __init__(self,x,y):
        self.xc,self.yc = x,y
    ## @brief Returns the x-coordinate of the point
    #  @return the x-coordinate
    def xcrd(self):
        return self.xc
    ## @brief Returns the y-coordinate of the point
    #  @return the y-coordinate
    def ycrd(self):
        return self.yc
    ## @brief Returns the distance of the point from another point
    #  @return the distance
    def dist(self,p):
        return math.sqrt((self.xc-p.xcrd())**2+(self.yc-p.ycrd())**2)
    ## @brief Rotates the point by angle theta(radians)
    #  @details rotation occurs about the origin, ccw
    #  @param theta The angle of rotation
    def rot(self, theta):
        x = self.xcrd()
        y = self.ycrd()
        self.xc = math.cos(theta)*x - math.sin(theta)*y
        self.yc = math.sin(theta)*x + math.cos(theta)*y
