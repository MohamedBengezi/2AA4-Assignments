/**
 * Module for ShipT
 * 
 * @author Mohamed Bengezi
 * 400021279
 * bengezim
 */
public class ShipT {
	public final int MAX_SIZE = 5;
	public final int MIN_SIZE = 2;
	private PointT head;
	private PointT tail;
	private int length;

	/**
	 * Initialization for ShipT
	 * 
	 * @author Mohamed Bengezi
	 * @param l
	 *            - The length of the ship
	 * @param a
	 *            - The head/starting point of the ship
	 * @param b
	 *            - The tail/end point of the ship
	 * @exception InvalidShipException
	 */
	public ShipT(int l, PointT a, PointT b) throws InvalidShipException {
		if (!(MIN_SIZE <= l) || !(l <= MAX_SIZE))
			throw new InvalidShipException();

		if ((a.xcrd() != b.xcrd()) && (a.ycrd() != b.ycrd()))
			throw new InvalidShipException();

		this.length = l;
		this.head = a;
		this.tail = b;
	}

	/**
	 * Length getter
	 * 
	 * @author Mohamed Bengezi
	 * @return the length, an integer
	 */
	public int get_length() {
		return this.length;
	}

	/**
	 * Head getter
	 * 
	 * @author Mohamed Bengezi
	 * @return the head, a point
	 */
	public PointT get_head() {
		return this.head;
	}

	/**
	 * Tail getter
	 * 
	 * @author Mohamed Bengezi
	 * @return the tail, a point
	 */
	public PointT get_tail() {
		return this.tail;
	}

}
