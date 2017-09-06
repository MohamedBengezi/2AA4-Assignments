/**
 * A class that contains methods that calculate stats of the path
 * @author Mohamed Bengezi
 * 
 */
public class PathCalculation {
	/**
	 * Calculates the total distance of the specified path
	 * @author Mohamed Bengezi
	 * @param p - the path
	 * @return the total distance as a real number
	 * @exception InvalidPositionException 
	 */
	public static double totalDistance(PathT p) throws InvalidPositionException{
		double d = 0.0;
		for (int i = 0; i < p.size()-1;i++)
			d += ((PointT) p.getval(i)).dist((PointT) p.getval(i+1));
		return d;
	}
	/**
	 * Calculates the total number of turns in the specified path
	 * @author Mohamed Bengezi
	 * @param p - the path
	 * @return the total number of turns
	 * @exception InvalidPositionException, InvalidRegionException
	 */
	public static int totalTurns(PathT p) throws InvalidPositionException, InvalidRegionException{
		int turns = 0;
		for (int i =0; i < p.size() -2; i++){
			if (angle((PointT) p.getval(i), (PointT) p.getval(i+1), (PointT) p.getval(i+2) ) != 0)
				turns++;
		}
		return turns;
	}
	
	/**
	 * Calculates the estimated time to take the specified path
	 * @author Mohamed Bengezi
	 * @param p - the path
	 * @return the estimated time
	 * @exception InvalidPositionException, InvalidRegionException
	 */
	public static double estimatedTime(PathT p) throws InvalidPositionException, InvalidRegionException{
		return linear_time(p)+angular_time(p);
	}
	
	
	/**
	 * A local function that calculates the angle between two lines
	 * @author Mohamed Bengezi
	 * @param p1 - first point
	 * @param p2 - second point
	 * @param p3 - third point
	 * @return the angle
	 * @exception InvalidRegionException
	 */
	private static double angle(PointT p1, PointT p2, PointT p3) throws InvalidRegionException{
		double num = (p2.xcrd() - p1.xcrd()) * (p3.xcrd() - p2.xcrd()) + (p2.ycrd() - p1.ycrd()) * (p3.ycrd() - p2.ycrd());
		double d = p1.dist(p2) * p2.dist(p3);
		return Math.acos(num/d);
	}
	/**
	 * A local function that calculates the linear time
	 * @author Mohamed Bengezi
	 * @param p - the path
	 * @return the linear time
	 * @exception InvalidPostionException
	 */

	private static double linear_time(PathT p) throws InvalidPositionException{
		double t = 0.0;
		for (int i = 0; i < p.size()-1;i++)
			t += ((PointT) p.getval(i)).dist((PointT) p.getval(i+1))/Constants.VELOCITY_LINEAR;
		return t;
	}
	
	/**
	 * A local function that calculates the angular time
	 * @author Mohamed Bengezi
	 * @param p - the path
	 * @return the angular time
	 * @exception InvalidPostionException, InvalidRegionException
	 */
	private static double angular_time(PathT p) throws InvalidPositionException, InvalidRegionException{
		double t = 0.0;
		for (int i = 0; i < p.size()-2;i++)
			t += angle((PointT) p.getval(i),(PointT) p.getval(i+1),(PointT) p.getval(i+2))/Constants.VELOCITY_ANGULAR;
		return t;
	}
	public static void main(String[] args) throws Exception{
		PathT p = new PathT();
		p.add(0, new PointT(0.0,0.0));
		p.add(1, new PointT(5.0,0.0));
		p.add(2, new PointT(5.0,5.0));
		p.add(3, new PointT(10.0,5.0));
		p.add(4, new PointT(10.0,10.0));
		p.add(5, new PointT(10.0,15.0));
		p.add(6, new PointT(10.0,20.0));


		System.out.println(totalDistance(p));
		
	}
}
