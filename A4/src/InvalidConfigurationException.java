/**
 * A class that defines the InvalidPlacementException for GameStateT
 * @author Mohamed Bengezi
 * 
 */
public class InvalidConfigurationException extends Exception{
	public InvalidConfigurationException(){super();}
	public InvalidConfigurationException(String message) { super(message); }
	public InvalidConfigurationException(String message, Throwable cause) { super(message, cause); }
	public InvalidConfigurationException(Throwable cause) { super(cause); }
}
