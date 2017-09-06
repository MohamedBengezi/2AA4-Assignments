##Mohamed Bengezi
##400021279

## @file deque.py
#  @author Mohamed Bengezi
#  @brief A deque class that uses circleADT objects
#  @date Feb 19, 2017

import circleADT as cADT
import math

## @brief A Deque class designed specifically for the circleADT module
class Deq:
    MAX_SIZE = 20
    s = []
    ## @brief A constructer for the deque
    #  @details Initializes the EMPTY deque
    @staticmethod
    def init():
        Deq.s = []
    ## @brief Adding a circleT object into the deque
    #  @details pushes it onto the end of the stack
    #  @param c The CircleT object
    #  @exception A FULL deque
    @staticmethod
    def pushBack(c):
        s = Deq.s
        size = len(Deq.s)
        if size == Deq.MAX_SIZE:
            raise FULL("Maximum size exceeded")
        s = s[0:size] + [c]
        Deq.s = s
    ## @brief Adding a circleT object into the deque
    #  @details pushes it onto the front of the stack
    #  @param c The CircleT object
    #  @exception A FULL deque
    @staticmethod
    def pushFront(c):
        s = Deq.s
        size = len(Deq.s)
        if size == Deq.MAX_SIZE:
            raise FULL("Maximum size exceeded")
        s =  [c] + s[0:size]
        Deq.s = s
    ## @brief Removing a circleT object from the deque
    #  @details pops the last object from the end of the stack
    #  @exception An EMPTY deque
    @staticmethod
    def popBack():
        s = Deq.s
        size = len(Deq.s)
        if size == 0:
            raise EMPTY("Nothing to pop")
        s = s[0:size-1]
        Deq.s = s
    ## @brief Removing a circleT object from the deque
    #  @details pops the first object from the front of the stack
    #  @exception An EMPTY deque
    @staticmethod
    def popFront():
        s = Deq.s
        size = len(Deq.s)
        if size == 0:
            raise FULL("Nothing to pop")
        s = s[1:size]
        Deq.s = s
    ## @brief Returns the last element on the deque
    #  @return The last CircleT object on the deque
    #  @exception An EMPTY deque
    @staticmethod
    def back():
        size = len(Deq.s)
        if size == 0:
            raise EMPTY("EMPTY deque")
        return Deq.s[len(Deq.s)-1]
    ## @brief Returns the first element on the deque
    #  @return The first CircleT object on the deque
    #  @exception An EMPTY deque
    @staticmethod
    def front():
        size = len(Deq.s)
        if size == 0:
            raise EMPTY("EMPTY deque")
        return Deq.s[0]
    ## @brief Returns the size of the deque
    #  @return size of the deque
    @staticmethod
    def size():
        return len(Deq.s)
    ## @brief Checks if none of the circles intersect each other
    #  @details Uses the intersect method from CircleT
    #  @return True(if none intersect) or False
    #  @exception An EMPTY deque
    @staticmethod
    def disjoint():
        size = len(Deq.s)
        if size == 0:
            raise EMPTY("EMPTY Deque")
        for i in range(0, size):
            for j in range(0, size):
                if i != j:
                    if ((Deq.s[i]).intersect(Deq.s[j])):
                        return False
        return True

    
    ## @brief Sums all the forces in the x plane
    #  @details Uses the local method Fx, and sums all the forces on the first circle with the other circles
    #  @param f The gravitational law
    #  @return The sum of all forces
    #  @exception An EMPTY deque
    @staticmethod
    def sumFx(f):
        size = len(Deq.s)
        t = 0
        if size == 0:
            raise EMPTY("EMPTY deque")
        for i in range(1,size):
            t += Fx(f,Deq.s[i],Deq.s[0])
        return t
    
    ## @brief A total area function, though the implementation is not required
    #  @details  It sums the areas of all the circle in the deque. The exceptions are coded as a precaution
    #  @exception An EMPTY deque
    @staticmethod
    def totalArea():
        size = len(Deq.s)
        if size == 0:
            raise EMPTY("EMPTY deque")
    ## @brief An average radius function, though the implementation is not required
    #  @details Gets the average radius. The exceptions are coded as a precaution
    #  @exception An EMPTY deque
    @staticmethod
    def averageRadius():
        size = len(Deq.s)
        if size == 0:
            raise EMPTY("EMPTY deque")

## @brief Local function for calculating the Force between two ciircles
#  @param f The gravitational law
#  @param ci The first circle
#  @param cj The second circle
#  @return The force between the circles 
def Fx(f,ci,cj):
    xcomp(ci.force(f)(cj),ci,cj)

## @brief Local function used for determining the x-component of the force
#  @param F The force
#  @param ci The first circle
#  @param cj The second circle
#  @return The x component of the force between the circles 
def xcomp(F,ci,cj):
    F*((ci.cen().xcrd()-cj.cen().xcrd())/ci.connection(cj).len())
## @brief The exception for a FULL deque
class FULL(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)
## @brief The exception for an EMPTY deque
class EMPTY(Exception):
  def __init__(self, ivalue):
    self.ivalue = ivalue
  def __str__(self):
    return str(self.ivalue)




