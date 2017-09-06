##Mohamed Bengezi
##400021279

import unittest
import pointADT as pADT
import lineADT as lADT
import circleADT as cADT
from deque import *
import math
class CircleDeque(unittest.TestCase):
    def test_point_xcrd(self):
        a = pADT.PointT(3,0)
        self.assertTrue(a.xcrd() == 3)
    def test_point_ycrd(self):
        a = pADT.PointT(0,4)
        self.assertTrue(a.xcrd() == 0)
    def test_point_dist(self):
        a = pADT.PointT(0,0)
        b = pADT.PointT(5,0)
        self.assertTrue(a.dist(b) == 5)
    def test_point_rot_neg(self):
        b = pADT.PointT(5,0)
        b.rot(-math.pi/2.0)
        self.assertAlmostEqual(b.xcrd(),0.0,places=10,msg=None,delta=None)
        self.assertAlmostEqual(b.ycrd(),-5.0,places=10,msg=None,delta=None)
    def test_point_rot_pos(self):
        b = pADT.PointT(5,0)
        b.rot(math.pi/2.0)
        self.assertAlmostEqual(b.xcrd(),0.0,places=10,msg=None,delta=None)
        self.assertAlmostEqual(b.ycrd(),5.0,places=10,msg=None,delta=None)
    def test_point_rot_zero(self):
        b = pADT.PointT(5,0)
        b.rot(0)
        self.assertAlmostEqual(b.xcrd(),5.0,places=10,msg=None,delta=None)
        self.assertAlmostEqual(b.ycrd(),0.0,places=10,msg=None,delta=None)
    def test_point_rot_abovepi(self):
        b = pADT.PointT(5,0)
        b.rot(2*math.pi)
        self.assertAlmostEqual(b.xcrd(),5.0,places=10,msg=None,delta=None)
        self.assertAlmostEqual(b.ycrd(),0.0,places=10,msg=None,delta=None)
    
    def test_line_beg(self):
        a = pADT.PointT(0,0)
        b = pADT.PointT(5,5)
        c = lADT.LineT(a,b)
        self.assertTrue(c.beg().xcrd() == 0 and c.beg().ycrd() == 0)
    def test_line_end(self):
        a = pADT.PointT(0,0)
        b = pADT.PointT(5,5)
        c = lADT.LineT(a,b)
        self.assertTrue(c.end().xcrd() == 5 and c.end().ycrd() == 5)
    def test_line_len(self):
        a = pADT.PointT(0,0)
        b = pADT.PointT(0,5)
        c = lADT.LineT(a,b)
        self.assertTrue(c.len() == 5)
    def test_line_mdpt_zero(self):
        a = pADT.PointT(0,0)
        b = pADT.PointT(0,0)
        c = lADT.LineT(a,b)
        self.assertTrue(c.mdpt().xcrd() == 0.0 and c.mdpt().ycrd() == 0.0)
    def test_line_mdpt(self):
        a = pADT.PointT(0,0)
        b = pADT.PointT(0,6)
        c = lADT.LineT(a,b)
        self.assertTrue(c.mdpt().xcrd() == 0.0 and c.mdpt().ycrd() == 3.0)

    def test_line_rot(self):
        a = pADT.PointT(0,0)
        b = pADT.PointT(0,6)
        c = lADT.LineT(a,b)
        c.rot(2*math.pi)
        self.assertAlmostEqual(c.beg().xcrd(),0.0,places=10,msg=None,delta=None)
        self.assertAlmostEqual(c.beg().ycrd(),0.0,places=10,msg=None,delta=None)
        self.assertAlmostEqual(c.end().xcrd(),0.0,places=10,msg=None,delta=None)
        self.assertAlmostEqual(c.end().ycrd(),6.0,places=10,msg=None,delta=None)
    def test_line_avg(self):
        self.assertTrue(lADT.avg(4,4) == 4.0)
    def test_circle_cen(self):
        a = cADT.CircleT(pADT.PointT(0,0),5)
        self.assertTrue(a.cen().xcrd() == 0 and a.cen().ycrd() == 0)
    def test_circle_rad(self):
        a = cADT.CircleT(pADT.PointT(0,0),5)
        self.assertTrue(a.rad() == 5)
    def test_circle_area(self):
        a = cADT.CircleT(pADT.PointT(0,0),5)
        self.assertTrue(a.area() == math.pi*5**2)
    def test_circle_intersect(self):
        a = cADT.CircleT(pADT.PointT(0,0),5)
        b = cADT.CircleT(pADT.PointT(9,9),2)
        self.assertTrue(a.intersect(b) == False)
    def test_circle_connection(self):
        a = cADT.CircleT(pADT.PointT(0,0),5)
        b = cADT.CircleT(pADT.PointT(9,9),2)
        d = a.connection(b)
        self.assertTrue(d.beg().xcrd() == 0 and d.end().xcrd() == 9)
        self.assertTrue(d.beg().ycrd() == 0 and d.end().ycrd() == 9)
    def test_circle_force(self):
        q = cADT.CircleT(pADT.PointT(0,0),3)
        self.assertTrue(q.force(lambda x: x)(cADT.CircleT(pADT.PointT(1.0,0.0),2.0)) == (math.pi*((q.rad())**2.0))*math.pi*2.0**2) 
        self.assertTrue(q.force(lambda x: x*3)(cADT.CircleT(pADT.PointT(0,0),0)) == 0.0)
    def test_circle_insideCircle(self):
        a = cADT.CircleT(pADT.PointT(0,0),10)
        b = pADT.PointT(9,0)
        self.assertTrue(cADT.insideCircle(b,a) == True)
    def test_deque_pushBack(self):
        Deq.init()
        b = cADT.CircleT(pADT.PointT(0,0),10)
        for i in range(20):
            Deq.pushBack(b)
        self.assertTrue(Deq.s == [b]*20)
        c = cADT.CircleT(pADT.PointT(4,5),3)
        with self.assertRaises(FULL):
            Deq.pushBack(c)
    def test_deque_pushFront(self):
        Deq.init()
        b = cADT.CircleT(pADT.PointT(0,0),10)
        for i in range(20):
            Deq.pushFront(b)
        self.assertTrue(Deq.s == [b]*20)
        c = cADT.CircleT(pADT.PointT(4,5),3)
        with self.assertRaises(FULL):
            Deq.pushFront(c)
    def test_deque_popBack(self):
        Deq.init()
        b = cADT.CircleT(pADT.PointT(0,0),10)
        Deq.pushFront(b)
        c = cADT.CircleT(pADT.PointT(4,5),3)
        Deq.pushFront(c)
        Deq.popBack()
        self.assertTrue(Deq.s == [c])
    def test_deque_popFront(self):
        Deq.init()
        b = cADT.CircleT(pADT.PointT(0,0),10)
        Deq.pushFront(b)
        c = cADT.CircleT(pADT.PointT(4,5),3)
        Deq.pushFront(c)
        Deq.popFront()
        self.assertTrue(Deq.s == [b])
        
    def test_deque_back(self):
        Deq.init()
        b = cADT.CircleT(pADT.PointT(0,0),10)
        Deq.pushFront(b)
        c = cADT.CircleT(pADT.PointT(4,5),3)
        Deq.pushFront(c)
        self.assertTrue(Deq.back() == b)
    def test_deque_front(self):
        Deq.init()
        b = cADT.CircleT(pADT.PointT(0,0),10)
        Deq.pushFront(b)
        c = cADT.CircleT(pADT.PointT(4,5),3)
        Deq.pushFront(c)
        self.assertTrue(Deq.front() == c)
    def test_deque_size(self):
        Deq.init()
        b = cADT.CircleT(pADT.PointT(0,0),10)
        Deq.pushFront(b)
        c = cADT.CircleT(pADT.PointT(4,5),3)
        Deq.pushFront(c)
        self.assertTrue(Deq.size() == 2)
    def test_deque_disjoint(self):
        Deq.init()
        with self.assertRaises(EMPTY):
            self.assertTrue(Deq.disjoint())
        b = cADT.CircleT(pADT.PointT(0,0),3)
        Deq.pushFront(b)
        self.assertTrue(Deq.disjoint())
        c = cADT.CircleT(pADT.PointT(14,15),3)
        Deq.pushFront(c)
        self.assertTrue(Deq.disjoint())
        d = cADT.CircleT(pADT.PointT(30,30),4)
        Deq.pushFront(d)
        self.assertTrue(Deq.disjoint())
##    def test_deque_sumFx(self):
##        Deq.init()
##        with self.assertRaises(EMPTY): # Case of sumFx with no circle
##            Deq.sumFx(lambda s: s)
##        c1 = cADT.CircleT(pADT.PointT(0.0,0.0),6.0)
##        temp = (math.pi*((c1.rad())**2.0))*math.pi
##        Deq.pushFront(c1)
##        Deq.pushBack((cADT.CircleT(pADT.PointT(5.0,5.0),3.0)))
##        Deq.pushBack((cADT.CircleT(pADT.PointT(5.0,5.0),3.0)))
##        Deq.pushBack((cADT.CircleT(pADT.PointT(5.0,5.0),3.0)))
##        self.assertAlmostEqual(Deq.sumFx(lambda s: s),temp*3.0,places=10,msg=None,delta=None)

##    def test_deque_Fx(self):
##    def test_deque_xcomp(self):
    if __name__ == '__main__':
        unittest.main()
        
