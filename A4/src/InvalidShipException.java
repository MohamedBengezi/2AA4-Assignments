/**
 * A class that defines the InvalidShipException for ShipT
 * @author Mohamed Bengezi
 * 
 */
public class InvalidShipException extends Exception{
	public InvalidShipException(){super();}
	public InvalidShipException(String message) { super(message); }
	public InvalidShipException(String message, Throwable cause) { super(message, cause); }
	public InvalidShipException(Throwable cause) { super(cause); }
}