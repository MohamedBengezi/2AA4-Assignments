/**
 * A class that defines a GenericList of RegionT objects that are the destinations of the robot
 * @author Mohamed Bengezi
 * 
 */
public class Destinations extends GenericList {
	public GenericList<RegionT> dests;
	/**
	 * Constructor for Destinations
	 * @author Mohamed Bengezi
	 */
	public Destinations(){
		dests = new GenericList<RegionT>();
	}
}
