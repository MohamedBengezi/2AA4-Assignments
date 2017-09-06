/**
 * A class that defines the FullSequenceException for GenericList
 * @author Mohamed Bengezi
 * 
 */
public class FullSequenceException extends Exception{
	public FullSequenceException(){super();}
	public FullSequenceException(String message) { super(message); }
	public FullSequenceException(String message, Throwable cause) { super(message, cause); }
	public FullSequenceException(Throwable cause) { super(cause); }
}
