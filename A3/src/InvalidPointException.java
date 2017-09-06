/**
 * A class that defines the InvalidPointException for PointT
 * @author Mohamed Bengezi
 * 
 */
public class InvalidPointException extends Exception{
	public InvalidPointException(){super();}
	public InvalidPointException(String message) { super(message); }
	public InvalidPointException(String message, Throwable cause) { super(message, cause); }
	public InvalidPointException(Throwable cause) { super(cause); }
}
