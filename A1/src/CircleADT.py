##Mohamed Bengezi
##bengezim
import math
## @brief CircleT is an ADT that stores data on a circle
#  @details It consists of various methods that return and/or manipulate the circles
class CircleT:
    ## @brief Initializes an object of type CircleT
    #  @param x is the x coordinate of the centre of the circle
    #  @param y is the y coordinate of the centre of the circle
    #  @param z is the radius of the circle
    def __init__(self,x,y,z):
        ## x-coordinate,y-coordinate,radius respectively
        self.x,self.y,self.z = x,y,z

    ## @brief Returns the x-coordinate of the centre of the circle
    #  @return The x-coordinate of the centre
    def xcoord(self):
        return self.x
    
    ## @brief Returns the y-coordinate of the centre of the circle
    #  @return The y-coordinate of the centre
    def ycoord(self):
        return self.y
    
    ## @brief Returns the radius of the circle
    #  @return The radius
    def radius(self):
        return self.z

    ## @brief Calculates the area of the circle
    #  @return The area of the circle
    def area(self):
        return math.pi*self.z**2

    ## @brief Calculates the circumference of the circle
    #  @return The circumference of the circle
    def circumference(self):
        return 2*math.pi*self.z

    ## @brief Checks if the circle is inside the box
    #  @details Taking in the details of a box as input,
    #  it determines if the circle lies inside the box. Used pythagorean theorum
    #  @param x0 the x coordinate of the left side of a box
    #  @param y0 the y coordinate of the top of a box
    #  @param w the width of the box
    #  @param h the height of the box
    #  @return true if cirlce is inside the box
    ##check insideBox
    def insideBox(self,x0,y0,w,h):
        if (self.x-self.z) >= x0 and (self.x+self.z) <= (x0+w) and (self.y+self.z)<= y0+h and (self.y-self.z)>=(y0):
            return True
        else:
            return False
        
    ## @brief Checks if one circle intersects another
    #  @details Implemented using pythagorean theorum. Assumption made that two circles intersect only if the distance between centers is less than the two radii combined
    #  @param c the second circle to be compared
    #  @return true if cirlces intersect
    def intersect(self,c):
        ## r is xcoordinate of circle minus that of second circle 
        r = self.x-c.x
        ## r is ycoordinate of circle minus that of second circle
        s = self.y-c.y
        ## dist is the result of the pythagorean theorum
        dist = math.sqrt(r**2 + s**2)
        if dist < (self.z + c.z):
            return True
        else:
            return False

    ## @brief Scales the radius of the circle
    #  @details radius is increased/decreased by factor k
    #  @param k the float k that the radius is scaled by
    def scale(self,k):
        self.z = self.z*k
        
    ## @brief Moves the centre of the circle
    #  @details x and y coordinates are translated by factors dx, dy respectively
    #  @param dx amount translated in the x
    #  @param dy amount translated in the y
    def translate(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy

