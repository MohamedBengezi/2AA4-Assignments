
/**
 * Module for GameStateT
 * @author Mohamed Bengezi
 * 400021279
 * bengezim
 */

import java.util.ArrayList;
import java.util.Arrays;

public class GameStateT {
	public final int MAX_ROWS = 10;
	public final int MAX_COLUMNS = 10;
	public Integer[] hitList;
	public ShipT[] shipList;
	private static int hitIndex;

	/**
	 * Constructor for GameStateT
	 * 
	 * @author Mohamed Bengezi
	 * @param shipList
	 *            - List of the ships, which are of {@code ShipT}
	 * @exception InvalidConfigurationException, InvalidPointException
	 */
	public GameStateT(ShipT[] shipList) throws InvalidConfigurationException, InvalidPointException {
		if (!(shipList.length == 5) || !(shipList[0].get_length() == 2) || !(shipList[1].get_length() == 3)
				|| !(shipList[2].get_length() == 3) || !(shipList[3].get_length() == 4)
				|| !(shipList[4].get_length() == 5))
			throw new InvalidConfigurationException();

		for (int i = 0; i < shipList.length; i++) {
			for (int j = 0; j < shipList.length; j++) {
				if (j != i) {
					if (conflict(shipList[i], shipList[j]))
						throw new InvalidConfigurationException();
				}
			}
		}
		this.shipList = shipList;
		hitList = new Integer[5];
	}

	/**
	 * Constructor for GameStateT
	 * 
	 * @author Mohamed Bengezi
	 * @param p
	 *            - a {@code PoinT} Object
	 * @return whether the shot is a hit or a miss
	 */
	public boolean has_been_shot(PointT p) {

		if (checkShot(this.shipList, p)) {
			this.hitList[hitIndex]++;
		}

		return checkShot(shipList, p);
	}

	/**
	 * Constructor for GameStateT
	 * 
	 * @author Mohamed Bengezi
	 * @return whether all ships are sunken
	 */
	public boolean all_ships_lost() {
		for (int i = 0; i < shipList.length; i++) {
			if (shipList[i].get_length() != hitList[i])
				return false;
		}

		return true;
	}

	private boolean pointInLine(PointT p, PointT head, PointT tail) {
		return (head.dist(p) + tail.dist(p)) == head.dist(tail);
	}

	private boolean conflict(ShipT a, ShipT b) throws InvalidPointException {
		PointT temp = new PointT(0, 0);

		// If the first ship is vertical
		if (a.get_head().xcrd() == a.get_tail().xcrd()) {
			// If the head of the ship is higher than the tail
			if (a.get_head().ycrd() > a.get_tail().ycrd()) {
				temp = a.get_tail();
				// i starts at the tail, then goes up the line until the head
				for (PointT i = temp; i.ycrd() <= a.get_head().ycrd(); i = new PointT(i.xcrd(), i.ycrd() + 1)) {
					if (pointInLine(i, a.get_head(), a.get_tail()) && pointInLine(i, b.get_head(), b.get_tail()))
						return true;
				}
			}

			// if the head is lower than the tail
			if (a.get_head().ycrd() < a.get_tail().ycrd()) {
				temp = a.get_head();
				// Start at the head, then go up to the tail
				for (PointT i = temp; i.ycrd() <= a.get_tail().ycrd(); i = new PointT(i.xcrd(), i.ycrd() + 1)) {
					if (pointInLine(i, a.get_head(), a.get_tail()) && pointInLine(i, b.get_head(), b.get_tail()))
						return true;
				}
			}

		}
		// If the first boat is horizontal
		if (a.get_head().ycrd() == a.get_tail().ycrd()) {
			// if the head is after the tail
			if (a.get_head().xcrd() > a.get_tail().xcrd()) {
				temp = a.get_tail();
				for (PointT i = temp; i.xcrd() <= a.get_head().xcrd(); i = new PointT(i.xcrd() + 1, i.ycrd())) {
					if (pointInLine(i, a.get_head(), a.get_tail()) && pointInLine(i, b.get_head(), b.get_tail()))
						return true;
				}
			}

			// If the head is before the tail
			if (a.get_head().xcrd() < a.get_tail().xcrd()) {
				temp = a.get_head();

				for (PointT i = temp; i.xcrd() <= a.get_tail().xcrd(); i = new PointT(i.xcrd() + 1, i.ycrd())) {
					if (pointInLine(i, a.get_head(), a.get_tail()) && pointInLine(i, b.get_head(), b.get_tail()))
						return true;
				}
			}
		}
		return false;
	}

	private boolean checkShot(ShipT[] shipList, PointT p) {
		int count = 0;
		for (ShipT i : shipList) {
			count++;
			if (pointInLine(p, i.get_head(), i.get_tail())) {
				hitIndex = count - 1;
				return true;
			}

		}
		return false;
	}

}
