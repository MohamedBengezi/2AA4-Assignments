import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;
import org.junit.After;
public class TestPathCalculation {
	PathT p = new PathT();
	PathT q = new PathT();
	PathT r = new PathT();

	@Before
	public void setUp() throws Exception {
		//There are five line segments, each of length 5, so the total distance should be 25.0
		//The total number of turns should be 3, rest of the lines are colinear
		//The estimated time should be approx 1.88 seconds
		p.add(0, new PointT(0.0,0.0));
		p.add(1, new PointT(5.0,0.0));
		p.add(2, new PointT(5.0,5.0));
		p.add(3, new PointT(10.0,5.0));
		p.add(4, new PointT(10.0,10.0));
		p.add(5, new PointT(10.0,15.0));
		p.add(6, new PointT(10.0,20.0));
		//There are three line segments
		//Total distance should be sqrt(72) + 6 + 14 = 28.4853
		//The total number of turns should be 2.
		//The estimated time should be approx 1.88 seconds
		q.add(0, new PointT(0.0,0.0));
		q.add(1, new PointT(6.0,6.0));
		q.add(2, new PointT(12.0,6.0));
		q.add(3, new PointT(12.0,20.0));
		//A path of length 0
		r.add(0,  new PointT(0.0,0.0));
		r.add(1,  new PointT(0.0,0.0));		
	}
	@Test
	public void testTotalDistance() throws Exception{
		System.out.println(PathCalculation.totalDistance(r));
		assertTrue(PathCalculation.totalDistance(p) == 30.0);
		assertEquals(28.4853, PathCalculation.totalDistance(q), 0.05);
		assertTrue(PathCalculation.totalDistance(r) == 0.0);
	}
	
	@Test
	public void testTotalTurns() throws Exception{
		assertTrue(PathCalculation.totalTurns(p) == 3);
		assertTrue(PathCalculation.totalTurns(q) == 2);		
	}
	
	@Test
	public void testEstimatedTime() throws Exception{
		double actual = PathCalculation.estimatedTime(p), expected = 2.16;
		System.out.println(actual);
		assertEquals(expected, actual, 0.05);
	}
	

}
