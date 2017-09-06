/**
 * ADT that defines a point object
 * @author Mohamed Bengezi
 * 
 */
public class PointT {
	//defining the state variables xc and yc
	private double xc;
	private double yc;
	/**
	 * Constructor for PointT, which takes an xcrd and ycrd as arguments
	 * @author Mohamed Bengezi
	 * @param x - x-coordinate
	 * @param y - y-coordinate
	 */
	//constructor for PointT, which takes an xcrd and ycrd as arguments
	public PointT(double x, double y) throws InvalidRegionException{
		if (xc < 0 ) throw new InvalidRegionException("xc < 0: " + xc);
		if (xc > Constants.MAX_X ) throw new InvalidRegionException("xc > MAX_X: " + xc);
		if (yc < 0) throw new InvalidRegionException("yc < 0: " + yc);
		if (yc > Constants.MAX_X  )throw new InvalidRegionException("yc > MAX_Y: " + yc);
		this.xc = x;
		this.yc = y;
	}
	//Getters for the xcrd and ycrd
	/**
	 * A getter for the x-coordinate
	 * @author Mohamed Bengezi
	 * @return x-coordinate
	 */
	public double xcrd(){return this.xc;}
	/**
	 * A getter for the y-coordinate
	 * @author Mohamed Bengezi
	 * @return y-coordinate
	 */
	public double ycrd(){return this.yc;}
	
	//method for finding the distance between two points
	/**
	 * Returns the distance between two PointT
	 * @author Mohamed Bengezi
	 * @param p - The second point
	 * @return The distance as a real number
	 */
	public double dist(PointT p){
		double a = this.xcrd() - p.xcrd();
		double b = this.ycrd() - p.ycrd();
		double c = a*a + b*b;
		return Math.sqrt(c);
	}

}
