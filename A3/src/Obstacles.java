/**
 * A class that defines a GenericList of RegionT objects that are the obstacles on the map
 * @author Mohamed Bengezi
 * 
 */
public class Obstacles extends GenericList{
	public GenericList<RegionT> obstacles;
	/**
	 * Constructor for Obstacles
	 * @author Mohamed Bengezi
	 */
	public Obstacles(){
		obstacles = new GenericList<RegionT>();
	}
}