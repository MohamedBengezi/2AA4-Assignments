/**
 * A class that defines the InvalidPositionException for GenericList
 * @author Mohamed Bengezi
 * 
 */
public class InvalidPositionException extends Exception{
	public InvalidPositionException(){super();}
	public InvalidPositionException(String message) { super(message); }
	public InvalidPositionException(String message, Throwable cause) { super(message, cause); }
	public InvalidPositionException(Throwable cause) { super(cause); }
}