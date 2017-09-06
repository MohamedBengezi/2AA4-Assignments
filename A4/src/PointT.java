/**
 * Module for PointT
 * @author Mohamed Bengezi
 * 400021279
 * bengezim
 */
public class PointT {
	private double xc;
	private double yc;
	public final int MAX_X = 10;
	public final int MAX_Y = 10;
	/**
	 * Constructor for PointT
	 * 
	 * @author Mohamed Bengezi
	 * @param xc
	 *            - The x-coordinate of the point
	 * @param yc
	 *            - The y-coordinate of the point
	 * @exception InvalidPointException
	 */
	public PointT(double xc, double yc) throws InvalidPointException{
		if (!(0 <= xc) || !(xc <= MAX_X) || !(0 <= yc) || !(yc <= MAX_Y))
			throw new InvalidPointException();
		this.xc = xc;
		this.yc = yc;
	}
	
	/**
	 * x-coordinate getter
	 * 
	 * @author Mohamed Bengezi
	 * @return the x-coordinate
	 */
	public double xcrd(){
		return this.xc;
	}
	
	/**
	 * y-coordinate getter
	 * 
	 * @author Mohamed Bengezi
	 * @return the y-coordinate
	 */
	public double ycrd(){
		return this.yc;
	}
	
	/**
	 * distance between two points
	 * 
	 * @author Mohamed Bengezi
	 * @param that - Another PointT object
	 * @return the distance between these two points
	 */
	public double dist(PointT that){
		return Math.sqrt(Math.pow(this.xc - that.xc, 2) + Math.pow(this.yc-that.yc, 2));
	}
}
