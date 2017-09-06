import java.util.Random;
/**
 * A class that defines a Region object on the Map
 * @author Mohamed Bengezi
 * 
 */
public class RegionT {
	//Declaring the state variables
	private static PointT lower_left;
	private static double width;
	private static double height;
	/**
	 * Constructor for RegionT, assigns values to the lower_left point, width, and height
	 * @author Mohamed Bengezi
	 * @param p - the lower left point of the region
	 * @param w - The width of the Region (x-axis)
	 * @param h - The height of the Region (y-axis)
	 * @exception InvalidRegionException is thrown when the region specified is not valid
	 */
	//Constructor for RegionT
	public RegionT(PointT p, double w, double h) throws InvalidRegionException{
		//Throws exception if w or h is negative, or if 
		if (w < 0) throw new InvalidRegionException("w < 0: " + w);
		if (h < 0) throw new InvalidRegionException("h < 0: " + h);
		if ((p.xcrd() + w) > Constants.MAX_X) throw new InvalidRegionException("p.xcrd() + w > MAX_X: " + (p.xcrd() + w ));
		if ((p.ycrd() + h) > Constants.MAX_Y) throw new InvalidRegionException("p.ycrd() + h > MAX_X: " + (p.ycrd() + h ));
		this.lower_left = p;
		this.width = w;
		this.height  = h;
	}
	
	/**
	 * This checks if p is in the region by checking 
	 * whether the distance between p and a random point in the region is less than the TOLERANCE
	 * @author Mohamed Bengezi
	 * @param p - The point to check
	 * @return True if p is in the region
	 * @exception InvalidRegionException is thrown when the region specified is not valid
	 */
	public static boolean pointInRegion(PointT p) throws InvalidRegionException{
		PointT[] a = Region();
		if ((a[0].ycrd() > p.ycrd()) && (a[0].ycrd() - p.ycrd() <= Constants.TOLERANCE) && (lower_left.xcrd() - Constants.TOLERANCE <= p.xcrd() && p.xcrd() <= lower_left.xcrd() + width + Constants.TOLERANCE)) return true;
		if ((a[1].ycrd() < p.ycrd()) && (p.ycrd() - a[1].ycrd() <= Constants.TOLERANCE) && (lower_left.xcrd() - Constants.TOLERANCE <= p.xcrd() && p.xcrd() <= lower_left.xcrd() + width + Constants.TOLERANCE)) return true;
		if ((a[2].xcrd() > p.xcrd()) && (a[2].xcrd() - p.xcrd()) <= Constants.TOLERANCE && (lower_left.ycrd() - Constants.TOLERANCE <= p.ycrd() && p.ycrd() <= lower_left.ycrd() + height + Constants.TOLERANCE)) return true;
		if ((a[3].xcrd() < p.xcrd()) && (p.xcrd() - a[3].xcrd()) <= Constants.TOLERANCE && (lower_left.xcrd() - Constants.TOLERANCE <= p.xcrd() && p.xcrd() <= lower_left.xcrd() + height + Constants.TOLERANCE)) return true;
		if (lower_left.dist(p) <= Constants.TOLERANCE) return true;
		if (new PointT(lower_left.xcrd() + width, lower_left.ycrd()).dist(p) <= Constants.TOLERANCE) return true;
		if (new PointT(lower_left.xcrd() + width, lower_left.ycrd() + height).dist(p) <= Constants.TOLERANCE) return true;
		if (new PointT(lower_left.xcrd(), lower_left.ycrd() + height).dist(p) <= Constants.TOLERANCE) return true;
		return false;
	}
	
	/**
	 * A private method for creating a random point in the region, used in pointInRegion()
	 * @author Mohamed Bengezi
	 * @return A random point that is in the region 
	 * @exception InvalidRegionException is thrown when the region specified is not valid
	 * @see #pointInRegion(PointT)
	 */
	private static PointT[] Region() throws InvalidRegionException{
		Random random = new Random();
		Double n1 = lower_left.xcrd() + width/2.0;
		Double n2 = lower_left.ycrd();
		Double n5 = lower_left.ycrd() + height;
		
		Double n3 = lower_left.ycrd() + height/2.0;
		Double n4 = lower_left.xcrd();
		Double n6 = lower_left.xcrd()+ width;
//		while (!(lower_left.xcrd() <= n1 && n1 <= (lower_left.xcrd() + width))){
//			n1 = new Double(random.nextDouble());
//		}
//		
//		while (!(lower_left.ycrd() <= n3 && n3 <= (lower_left.ycrd() + height))){
//			n3 = new Double(random.nextDouble());
//		}
		PointT[] a = new PointT[4];
		a[0] = new PointT(n1,n2);
		a[1] = new PointT(n1,n5);
		a[2] = new PointT(n4,n3);
		a[3] = new PointT(n6,n3);
		return a;
	}
	
	public static void main(String[] args) throws Exception, InvalidRegionException {
		RegionT a = new RegionT(new PointT(0.0,0.0),5.0,5.0);
		PointT p = new PointT(-5.0,1.0);
		System.out.println(pointInRegion(p));
	}
}
