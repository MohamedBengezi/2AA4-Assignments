import java.util.ArrayList;

/**
 * Module for BattleShip
 * 
 * @author Mohamed Bengezi
 * 400021279
 * bengezim
 */
public class BattleShip {
	private ArrayList<PointT> shots_taken;
	private boolean firstPlayerTurn;
	private GameStateT first_player;
	private GameStateT second_player;

	/**
	 * Initialization for the BattleShip abstract object
	 * 
	 * @author Mohamed Bengezi
	 * @param a
	 *            - List of the ships for first player, which are of
	 *            {@code ShipT}
	 * @param b
	 *            - List of the ships for second player, which are of
	 *            {@code ShipT}
	 * @exception InvalidConfigurationException, InvalidPointException
	 */
	public void init(ShipT[] a, ShipT[] b) throws InvalidConfigurationException, InvalidPointException {
		shots_taken = new ArrayList<PointT>();
		firstPlayerTurn = true;
		first_player = new GameStateT(a);
		second_player = new GameStateT(b);
	}

	/**
	 * Returns a list of all the shots made so far
	 * 
	 * @author Mohamed Bengezi
	 * @return - array of PointT objects representing the shots made so far
	 */
	public PointT[] all_shots() {
		return (PointT[]) this.shots_taken.toArray();
	}

	/**
	 * Placing a shot
	 * 
	 * @author Mohamed Bengezi
	 * @param p
	 *            - A shot, represented by {@code PointT}
	 * @return whether or not the shot was a hit or miss
	 * @exception InvalidShotException
	 */
	public boolean place_shot(PointT p) throws InvalidShotException {
		if (firstPlayerTurn) {
			/*
			 * if(first_player.has_been_shot(p)) throw new
			 * InvalidShotException();
			 */
			for (int i = 0; i < shots_taken.size(); i = i + 2) {
				if (repeatedShot(p, shots_taken.get(i)))
					throw new InvalidShotException();
			}
		}
		if (!firstPlayerTurn) {
			for (int i = 1; i < shots_taken.size(); i = i + 2) {
				if (repeatedShot(p, shots_taken.get(i)))
					throw new InvalidShotException();
			}
		}

		firstPlayerTurn = !firstPlayerTurn;

		shots_taken.add(p);

		if (firstPlayerTurn) {
			return second_player.has_been_shot(p);
		}

		if (!firstPlayerTurn) {
			return first_player.has_been_shot(p);
		}

		return false;
	}

	/**
	 * Checking for a winner
	 * 
	 * @author Mohamed Bengezi
	 * @return whether there is a winner or not
	 */
	public boolean is_winner() {
		if (firstPlayerTurn) {
			return second_player.all_ships_lost();
		}
		if (!firstPlayerTurn) {
			return first_player.all_ships_lost();
		}
		return false;
	}

	private boolean repeatedShot(PointT p, PointT q) {
		return ((p.xcrd() == q.xcrd()) && (p.ycrd() == q.ycrd()));
	}

}
