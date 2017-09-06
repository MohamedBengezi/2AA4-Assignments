##Mohamed Bengezi
##bengezim
import numpy as np
import CircleADT
## @file Statistics.py contains methods for creating statistics for the CircleADT class
#  @brief Method uses include getting the average, standard deviation, and rank of the radii of Circles


## @brief Calculates the average radius of the given list
#  @details Takes in a list of CircleT objects as input, and outputs the average of all the radii
#  @param list1 is the list of CircleT objects
#  @return The average radius of the given list of CircleT objects
def average(list1):
    x = radiusList(list1)
    return np.average(x)

## @brief Calculates the standard deviation of the radii of all circles on list
#  @details Takes in a list of CircleT objects as input, and outputs the standard deviation of the radii
#  @param list1 is the list of CircleT objects
#  @return The standard deviation of the radii of the given list of CircleT objects
def stdDev(list1):
    x = radiusList(list1)
    return np.std(x)

## @brief Ranks the objects of the given list by radius
#  @details Takes in a list of CircleT objects as input, and outputs a list ranked by radius. Assumption made that if there is a tie, the first is labeled bigger then the second
#  @param list1 is the list of CircleT objects
#  @return The list of objects ranked by radius
def rank(list1):
    x = radiusList(list1)
    ranked = [0]*len(x)
    for i in range(len(x)):
        ranked[x.index(max(x))] = i + 1
        x[x.index(max(x))] = min(x) - 1
                
    return ranked
          
## @brief Creates a list of the radii for the list of CircleT object
#  @details Takes in a list of CircleT objects as input, and outputs a list of their radii
#  @param list1 is the list of CircleT objects
#  @return The list of radii       
def radiusList(list1):
    rlist = []
    for i in list1:
        rlist.append(i.radius())
    return rlist
