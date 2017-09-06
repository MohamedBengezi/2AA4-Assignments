/**
 * A class that defines a GenericList of PointT objects that make up the path
 * @author Mohamed Bengezi
 * 
 */
public class PathT extends GenericList{
	public GenericList<PointT> paths;
	/**
	 * Constructor for PathT
	 * @author Mohamed Bengezi
	 */
	public PathT(){
		paths = new GenericList<PointT>();
	}
}
