##Mohamed Bengezi
##bengezim
import CircleADT as CADT
import Statistics as Stats
import math
import numpy as np

## @brief The Test class for CircleADT.py and Statistics.py
#  @details Consists of two test cases for each method
class TestCases():
    ## @brief Checks whether the method xcoord() works as expected
    #  @details Compares the actual result with the expected result
    #  @return A string displaying the result of both test cases
    def test_xcoord(self):
        #Test Case 1
        a = CADT.CircleT(5,5,5)
        if (a.xcoord() == 5):
            result = "xcoord() Test case 1: Expected: "+str(5)+" , Result: " + str(a.xcoord()) +". Passed \n"
        else:
            result = "xcoord() Test case 1: Expected: "+str(5)+" , Result: " + str(a.xcoord()) +". Failed \n"
        #Test Case 2
        b = CADT.CircleT(7,2,9)
        if (b.xcoord() == 7):
            result = result+ "xcoord() Test case 2: Expected: "+str(7)+" , Result: " + str(b.xcoord()) +". Passed "
        else:
            result = result+ "xcoord() Test case 2: Expected: "+str(7)+" , Result: " + str(b.xcoord()) +". Failed "
        return result

    ## @brief Checks whether the method ycoord() works as expected
    #  @details Compares the actual result with the expected result
    #  @return A string displaying the result of both test cases
    def test_ycoord(self):
        #Test Case 1
        a = CADT.CircleT(-3,19,5)
        if (a.ycoord() == 19):
            result = "ycoord() Test case 1: Expected: "+str(19)+" , Result: " + str(a.ycoord()) +". Passed \n"
        else:
            result = "ycoord() Test case 1: Expected: "+str(19)+" , Result: " + str(a.ycoord()) +". Failed \n"
        #Test Case 2
        b = CADT.CircleT(4,3,1)
        if (b.ycoord() == 3):
            result = result +"ycoord() Test case 2: Expected: "+str(3)+" , Result: " + str(b.ycoord()) +". Passed "
        else:
            result = result +"ycoord() Test case 2: Expected: "+str(3)+" , Result: " + str(b.ycoord()) +". Failed "
        return result

    ## @brief Checks whether the method radius() works as expected
    #  @details Compares the actual retrieved radius with the expected radius
    #  @return A string displaying the result of both test cases
    def test_radius(self):
        #Test Case 1
        a = CADT.CircleT(5,5,16)
        if (a.radius() == 16):
            result = "radius() Test case 1: Expected: "+str(16)+" , Result: " + str(a.radius()) +". Passed \n"
        else:
            result = "radius() Test case 1: Expected: "+str(16)+" , Result: " + str(a.radius()) +". Failed \n"
        #Test Case 2
        b = CADT.CircleT(7,2,9)
        if (b.radius() == 9):
            result = result +"radius() Test case 2: Expected: "+str(9)+" , Result: " + str(b.radius()) +". Passed "
        else:
            result = result +"radius() Test case 2: Expected: "+str(9)+" , Result: " + str(b.radius()) +". Failed "
        return result

    ## @brief Checks whether the method area() works as expected
    #  @details Compares the calculated area with the expected area
    #  @return A string displaying the result of both test cases
    def test_area(self):
        #Test Case 1
        a = CADT.CircleT(5,5,16)
        if (a.area() == math.pi*a.radius()**2):
            result = "area() Test case 1: Expected: "+str(math.pi*a.radius()**2)+" , Result: " + str(a.area()) +". Passed\n "
        else:
            result = "area() Test case 1: Expected: "+str(math.pi*a.radius()**2)+" , Result: " + str(a.area()) +". Failed\n "
        #Test Case 2
        b = CADT.CircleT(7,2,9)
        if (b.area() == math.pi*b.radius()**2):
            result = result +"area() Test case 2: Expected: "+str(math.pi*b.radius()**2)+" , Result: " + str(b.area()) +". Passed "
        else:
            result = result +"area() Test case 2: Expected: "+str(math.pi*b.radius()**2)+" , Result: " + str(b.area()) +". Failed "
        return result

    ## @brief Checks whether the method circumference() works as expected
    #  @details Compares the calculated circumference with the expected result
    #  @return A string displaying the result of both test cases
    def test_circumference(self):
        #Test Case 1
        a = CADT.CircleT(5,5,16)
        if (a.circumference() == 2*math.pi*a.radius()):
            result = "circumference() Test case 1: Expected: "+str(2*math.pi*a.radius())+" , Result: " + str(a.circumference()) +". Passed \n"
        else:
            result = "circumference() Test case 1: Expected: "+str(2*math.pi*a.radius())+" , Result: " + str(a.circumference()) +". Failed \n"
        #Test Case 2
        b = CADT.CircleT(7,2,9)
        if (b.circumference() == 2*math.pi*b.radius()):
            result = result + "circumference() Test case 2: Expected: "+str(2*math.pi*b.radius())+" , Result: " + str(b.circumference()) +". Passed"
        else:
            result = result + "circumference() Test case 2: Expected: "+str(2*math.pi*b.radius())+" , Result: " + str(b.circumference()) +". Failed"
        return result

    ## @brief Checks whether the method insideBox() works as expected
    #  @details Tested by determining the expected answer(T/F) by hand,
    #  then comparing with the method calculated answer.
    #  Assumption made that we are only looking at the fourth quadrant
    #  @return A string displaying the result of both test cases
    def test_insideBox(self):
        #Test Case 1
        a = CADT.CircleT(5,5,16)
        if (a.insideBox(5,5,5,5) == False):
            result = "insideBox() Test case 1: Expected: False , Result: " + str(a.insideBox(5,5,5,5)) +". Passed \n"
        else:
            result = "insideBox() Test case 1: Expected: False , Result: " + str(a.insideBox(5,5,5,5)) +". Failed \n"
        #Test Case 2
        b = CADT.CircleT(5,5,1)
        if (b.insideBox(1,1,10,10) == True):
            result = result + "insideBox() Test case 2: Expected: True , Result: " + str(a.insideBox(1,1,10,10)) +". Passed \n"
        else:
            result = result +"insideBox() Test case 2: Expected: True , Result: " + str(a.insideBox(1,1,10,10)) +". Failed \n"
        #Test Case 3
        b = CADT.CircleT(5,6,4)
        if (b.insideBox(0,0,10,12) == True):
            result = result +"insideBox() Test case 3: Expected: True , Result: " + str(a.insideBox(0,0,10,12)) +". Passed"
        else:
            result = result +"insideBox() Test case 3: Expected: True , Result: " + str(a.insideBox(0,0,10,12)) +". Failed"
        return result
        

    ## @brief Checks whether the method insideBox() works as expected
    #  @details Tested by determining the expected answer(T/F) by hand,
    #  then comparing with the method calculated answer
    #  @return A string displaying the result of both test cases
    def test_intersect(self):
        #Test Case 1
        a = CADT.CircleT(5,5,16)
        b = CADT.CircleT(5,5,10)
        if (a.intersect(b) == True):
            result = "Intersect() Test case 1: Expected: True , Result: " + str(a.intersect(b)) +". Passed \n"
        else:
            result = "Intersect() Test case 1: Expected: True , Result: " + str(a.intersect(b)) +". Failed \n"
        #Test Case 2
        a = CADT.CircleT(5,5,1)
        b = CADT.CircleT(1,1,1)
        if (a.intersect(b) == False):
            result = result + "Intersect() Test case 2: Expected: False , Result: " + str(a.intersect(b)) +". Passed \n"
        else:
            result = result + "Intersect() Test case 2: Expected: False , Result: " + str(a.intersect(b)) +". Failed \n"
        #Test Case 3
        a = CADT.CircleT(0,0,1)
        b = CADT.CircleT(2,0,1)
        if (a.intersect(b) == False):
            result = result + "Intersect() Test case 3: Expected: False , Result: " + str(a.intersect(b)) +". Passed"
        else:
            result = result + "Intersect() Test case 3: Expected: False , Result: " + str(a.intersect(b)) +". Failed"
        return result    
    
    ## @brief Checks whether the method scale() works as expected
    #  @details Compares the new radius with the expected radius
    #  @return A string displaying the result of both test cases
    def test_scale(self):
        #Test Case 1
        a = CADT.CircleT(5,5,16)
        b = CADT.CircleT(5,5,10)
        r1 = a.radius()
        a.scale(3)
        if (a.radius() == r1*3):
            result = "scale() Test case 1: Expected: "+str(r1*3)+", Result: " + str(a.radius()) +". Passed\n"
        else:
            result = "scale() Test case 1: Expected: "+str(r1*3)+", Result: " + str(a.radius()) +". Failed\n"
        #Test Case 2
        r1 = b.radius()
        b.scale(7)
        if (b.radius() == r1*7):
            result = result + "scale() Test case 1: Expected: "+str(r1*7)+", Result: " + str(b.radius()) +". Passed"
        else:
            result = result + "scale() Test case 1: Expected: "+str(r1*7)+", Result: " + str(b.radius()) +". Failed"
        return result
    
    ## @brief Checks whether the method translate() works as expected
    #  @details Compares the new x and y coordinates with the expected ones
    #  @return A string displaying the result of both test cases
    def test_translate(self):
        #Test Case 1
        a = CADT.CircleT(5,5,16)
        b = CADT.CircleT(5,5,10)
        x1 = a.xcoord()
        y1 = a.ycoord()
        a.translate(5,6)
        if ((a.xcoord() == x1+5) and (a.ycoord() == y1+6)):
            result = "translate() Test case 1: Expected: x = "+str(x1+5)+" y = "+str(y1+6)+" , Result: x = " + str(a.xcoord()) +" y = "+str(a.ycoord())+". Passed\n"
        else:
            result = "translate() Test case 1: Expected: x = "+str(x1+5)+" y = "+str(y1+6)+" , Result: x = " + str(a.xcoord()) +" y = "+str(a.ycoord())+". Failed\n"
        #Test Case 2
        x2 = b.xcoord()
        y2 = b.ycoord()
        b.translate(3,3)
        if ((b.xcoord() == x2+3) and (b.ycoord() == y2+3)):
            result = result + "translate() Test case 2: Expected: x = "+str(x2+3)+" y = "+str(y2+3)+" , Result: x = " + str(b.xcoord()) +" y = "+str(b.ycoord())+". Passed"
        else:
            result = result + "translate() Test case 2: Expected: x = "+str(x2+3)+" y = "+str(y2+3)+" , Result: x = " + str(b.xcoord()) +" y = "+str(b.ycoord())+". Failed"
        return result
    ## @brief Checks whether the method average() works as expected
    #  @details Compares the calculated average with the pre-determined average
    #  @return A string displaying the result of both test cases
    def test_average(self):
        #Test Case 1
        a = CADT.CircleT(5,5,16)
        b = CADT.CircleT(5,5,10)
        c = CADT.CircleT(5,5,8)
        d = CADT.CircleT(1,1,12)
        x = [a,b,c,d]
        x1 = [a.radius(),b.radius(),c.radius(),d.radius()]
        if (Stats.average(x) == (np.average(x1))):
            result =  "average() Test case 1: Expected: "+str(np.average(x1))+", Result: " + str(Stats.average(x)) +". Passed\n"
        else:
            result =  "average() Test case 1: Expected: "+str(np.average(x1))+", Result: " + str(Stats.average(x)) +". Failed\n"
        #Test Case 2
        a = CADT.CircleT(5,5,-9)
        b = CADT.CircleT(5,5,20)
        c = CADT.CircleT(5,5,400)
        d = CADT.CircleT(1,1,7)
        x = [a,b,c,d]
        x1 = [a.radius(),b.radius(),c.radius(),d.radius()]
        if (Stats.average(x) == (np.average(x1))):
            result = result + "average() Test case 2: Expected: "+str(np.average(x1))+", Result: " + str(Stats.average(x)) +". Passed"
        else:
            result = result + "average() Test case 2: Expected: "+str(np.average(x1))+", Result: " + str(Stats.average(x)) +". Failed"

        return result

    ## @brief Checks whether the method stdDev() works as expected
    #  @details Compares the calculated standard deviation with the expected
    #  @return A string displaying the result of both test cases
    def test_stdDev(self):
        #Test Case 1
        a = CADT.CircleT(5,5,16)
        b = CADT.CircleT(5,5,10)
        c = CADT.CircleT(5,5,8)
        d = CADT.CircleT(1,1,12)
        x = [a,b,c,d]
        x1 = [a.radius(),b.radius(),c.radius(),d.radius()]
        if (Stats.stdDev(x) == (np.std(x1))):
            result =  "stdDev() Test case 1: Expected: "+str(np.std(x1))+", Result: " + str(Stats.stdDev(x)) +". Passed\n"
        else:
            result =  "stdDev() Test case 1: Expected: "+str(np.std(x1))+", Result: " + str(Stats.stdDev(x)) +". Failed\n"
        #Test Case 2
        a = CADT.CircleT(5,5,-9)
        b = CADT.CircleT(5,5,20)
        c = CADT.CircleT(5,5,400)
        d = CADT.CircleT(1,1,7)
        x = [a,b,c,d]
        x1 = [a.radius(),b.radius(),c.radius(),d.radius()]
        if (Stats.stdDev(x) == (np.std(x1))):
            result = result + "stdDev() Test case 2: Expected: "+str(np.std(x1))+", Result: " + str(Stats.stdDev(x)) +". Passed"
        else:
            result = result + "stdDev() Test case 2: Expected: "+str(np.std(x1))+", Result: " + str(Stats.stdDev(x)) +". Failed"
        return result
    ## @brief Checks whether the method rank() works as expected
    #  @details Compares the ranked list with the expected one
    #  @return A string displaying the result of both test cases
    def test_rank(self):
        #Test Case 1
        a = CADT.CircleT(5,5,16)
        b = CADT.CircleT(5,5,10)
        c = CADT.CircleT(5,5,8)
        d = CADT.CircleT(1,1,12)
        x = [a,b,c,d]
        x1 = [a.radius(),b.radius(),c.radius(),d.radius()]
        if (Stats.rank(x) == ([1,3,4,2])):
            result =  "rank() Test case 1: Expected: "+str([1,3,4,2])+", Result: " + str(Stats.rank(x)) +". Passed\n"
        else:
            result =  "rank() Test case 1: Expected: "+str([1,3,4,2])+", Result: " + str(Stats.rank(x)) +". Failed\n"
        #Test Case 2
        a = CADT.CircleT(5,5,-9)
        b = CADT.CircleT(5,5,20)
        c = CADT.CircleT(5,5,20)
        d = CADT.CircleT(1,1,7)
        x = [a,b,c,d]
        x1 = [a.radius(),b.radius(),c.radius(),d.radius()]
        if (Stats.rank(x) == ([4,1,2,3])):
            result = result + "rank() Test case 1: Expected: "+str([4,1,2,3])+", Result: " + str(Stats.rank(x)) +". Passed\n"
        else:
            result = result + "rank() Test case 1: Expected: "+str([4,1,2,3])+", Result: " + str(Stats.rank(x)) +". Failed\n"
        return result
    
b = TestCases()
print b.test_xcoord()
print b.test_ycoord()
print b.test_radius()
print b.test_area()
print b.test_circumference()
print b.test_insideBox()
print b.test_intersect()
print b.test_scale()
print b.test_translate()
print b.test_average()
print b.test_stdDev()
print b.test_rank()
