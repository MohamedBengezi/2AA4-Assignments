/**
 * A class that defines the entire map(obstacles, destinations, safeZone)
 * @author Mohamed Bengezi
 * 
 */
public class Map {
	Obstacles obstacles;
	Destinations destinations;
	SafeZone safeZone;
	/**
	 * Constructor for Map, assigns values to the obstacles, destinations, and the safeZone
	 * @author Mohamed Bengezi
	 * @param o - The #GenericList of Obstacles
	 * @param d - The GenericList of Destinations
	 * @param s - The GenericList of size 1 that contains the safeZone
	 */
	public Map(Obstacles o, Destinations d, SafeZone s){
		obstacles = o;
		destinations = d;
		safeZone = s;
	}
	/**
	 * A getter for the obstacles
	 * @author Mohamed Bengezi
	 * @return GenericList of Obstacles
	 */
	public Obstacles get_obstacles(){return obstacles;}
	/**
	 * A getter for the destinations
	 * @author Mohamed Bengezi
	 * @return GenericList of destinations
	 */
	public Destinations get_destinations(){return destinations;}
	/**
	 * A getter for the safeZone
	 * @author Mohamed Bengezi
	 * @return The safeZone
	 */
	public SafeZone get_safeZone(){return safeZone;}
}
