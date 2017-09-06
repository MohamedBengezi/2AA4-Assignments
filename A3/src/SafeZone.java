/**
 * A class that defines a GenericList of size 1 for the safeZone
 * @author Mohamed Bengezi
 * 
 */
public class SafeZone extends GenericList {
	public GenericList<RegionT> safe;
	/**
	 * Constructor for SafeZone
	 * @author Mohamed Bengezi
	 */
	public SafeZone(){
		safe = new GenericList<RegionT>();
		safe.MAX_SIZE = 1;
	}
}
