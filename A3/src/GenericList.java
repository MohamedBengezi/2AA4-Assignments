import java.util.ArrayList;
import java.util.List;
/**
 * A class that defines a generic list and its various methods
 * @author Mohamed Bengezi
 * 
 */
public class GenericList<T> {
	//Creating the constant MAX_SIZE
	public static int MAX_SIZE = 100;
	List<T> list;
	/**
	 * Constructor for GenericList, initializes a generic arraylist
	 * @author Mohamed Bengezi
	 */
	@SuppressWarnings("unchecked")
	//Constructor for GenericLisT
	public GenericList(){
		 list = new ArrayList<T>();
	}
	/**
	 * Constructor for RegionT, assigns values to the lower_left point, width, and height
	 * @author Mohamed Bengezi
	 * @param i - the index at which to add the item
	 * @param p - the item to add
	 * @exception InvalidPositionException, FullSequenceException
	 */
	public void add(int i, T p) throws InvalidPositionException, FullSequenceException{
		if (i < 0 || i >= list.size()+1) throw new InvalidPositionException();
		if (list.size() == MAX_SIZE) throw new FullSequenceException();
		list.add(i, p);
	}
	/**
	 * Deletes the item at the specified index
	 * @author Mohamed Bengezi
	 * @param i - the index at which to delete the item
	 * @exception InvalidPositionException, FullSequenceException
	 */
	public void del(int i) throws InvalidPositionException{
		if (i < 0 || i >= list.size()) throw new InvalidPositionException();
		list.remove(i);
	}
	/**
	 * replaces the item at the specified index with the specified item
	 * @author Mohamed Bengezi
	 * @param i - the index at which to delete the item
	 * @param p - the new item
	 * @exception InvalidPositionException
	 */

	public void setval(int i, T p) throws InvalidPositionException{
		if (i < 0 || i >= list.size()) throw new InvalidPositionException();
		list.set(i, p);
	}
	
	/**
	 * Gets the item at the specified index
	 * @author Mohamed Bengezi
	 * @param i - the index at which the item is located
	 * @exception InvalidPositionException
	 */
	public T getval(int i) throws InvalidPositionException{
		if (i < 0 || i >= list.size()) throw new InvalidPositionException();
		return list.get(i);
	}
	
	/**
	 * Returns the size of the list
	 * @author Mohamed Bengezi
	 * @param i - the index at which the item is located
	 * @return the size of the list
	 */
	public int size(){
		return list.size();
	}
	public static void main(String[] args) throws InvalidPositionException, FullSequenceException, InvalidRegionException{
		GenericList<PointT> a = new GenericList<PointT>();
		PointT p = new PointT(0.0, 30.0);
		a.add(0, p);
		a.add(0, p);
		System.out.println(a.getval(0));
	}
}
