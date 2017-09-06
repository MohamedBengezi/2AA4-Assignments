/**
 * A class that defines the InvalidRegionException for RegionT
 * @author Mohamed Bengezi
 * 
 */
public class InvalidRegionException extends Exception{
	public InvalidRegionException(){super();}
	public InvalidRegionException(String message) { super(message); }
	public InvalidRegionException(String message, Throwable cause) { super(message, cause); }
	public InvalidRegionException(Throwable cause) { super(cause); }
}
