/**
 * CS062: silverdollar 
 *	a simple coin-moving game implemented with ArrayLists
 *
 * @author YOUR-NAME-HERE
 */

package silverdollar; 

import java.util.Random; 
import java.util.Scanner; 
import java.util.ArrayList;

public class TextCoinStrip { 
	int coins = 0;

	/** 
	 * the strip of coins. It is an arraylist with locations 
	 * indexed starting at 0. A square is occupied by a coin 
	 * if the boolean value at that location is true. 
	 */ 
	protected ArrayList<Boolean> theStrip; 

	/** 
	 * Constructs a representation of the Silver Dollar Game 
	 * 
	 * @param squares the number of squares 
	 * @param coins the number of coins 
	 * pre: 0 < coins < squares 
	 */ 
	public TextCoinStrip (int squares, int coins) { 
		this.coins = coins;
		if (0 > coins || coins >= squares) { // Check precondition
			System.out.println("Game must be played with number of\n"+
						"coins less than number of squares");
			
			// This is how exceptions are raised/thrown in Java.  We'll talk more about this later
			// When an exception is thrown, the method exits and, if nothing handles the exception,
			// the program will exit.
			throw new IllegalArgumentException("# coins: "+coins+" must be positive "
								+ "and less than # squares: "+squares);
		}
		
		theStrip = new ArrayList<Boolean>(); 
		//populate all squares with false values
		for (int i = 0; i < squares; i++){ 
			theStrip.add(false); 
		} 

		//place #coins randomly on the strip
		Random rand = new Random (); 
		
		while (0 < coins) { 
			int i = rand.nextInt (squares); //range: [0, squares-1]
			if (!theStrip.get(i)) { 
				theStrip.set(i, true); //what does element: do?
				coins--; 
			} 
		} 
	} 

	/** 
	 * toString returns the string representation of a strip. 
	 * 
	 * @return the string representation 
	 */ 
	public String toString() { 
		String stringStrip = "";
		for (int i=0; i<theStrip.size(); i++){
			if(theStrip.get(i)){
				stringStrip = stringStrip + "o";
			} else {
				stringStrip = stringStrip + "_";
			}
		}
		return stringStrip;
	} 

	/** 
	 * isLegalMove determines if a move is legal. 
	 * 
	 * @param start the location of the coin to be moved 
	 * @param distance how far the coin is to move 
	 * @return true if the move is legal 
	 */ 
	public boolean isLegalMove(int start, int distance) {
		//no coins jumping over each other
		int destination = start-distance;
		if (destination <0 || start > theStrip.size()-1 || start < 0) {
			return false;
		} else {
			return !theStrip.get(destination);
		}
	} 

	/** 
	 * makeMove makes a (legal) move. 
	 * 
	 * @param start the location of the coin to be moved 
	 * @param distance how far the coin is to move 
	 * pre: the move must be a legal one 
	 */ 

	public void makeMove(int start, int distance) { 
		
		if (isLegalMove(start, distance)){
			theStrip.set(start-distance, true);
		}
		theStrip.set(start, false);
	} 

	/** 
	 * gameIsOver determines if a game is completed. 
	 * 
	 * @return true if there are no more moves 
	 */ 
	public boolean gameIsOver() { 
		//if anything until idx coins-1 is false then return false
		for(int i=0; i<coins; i++){
			if (!theStrip.get(i)) {
				return false;
			}
		}

		//if anything beyond index coins-1 is true then return false
		for(int j=coins; j<coins; j++){
			if (theStrip.get(j)){
				return false;
			}
		}

		//else game is over (everything until coins-1 is true, the rest false) return true
		return true;	
	} 

	/** 
	 * play is a method to play the Silver Dollar Game 
	 * until it is finished. 
	 */ 
	public void play() { 
		Scanner scanner = new Scanner(System.in); 
		int start = 0; 
		int distance = 0; 
		
		while (!gameIsOver()) { 
			System.out.print(toString() + " Next move? "); 
			start = scanner.nextInt(); 
			distance = scanner.nextInt(); 
			
			if (isLegalMove(start, distance)) { 
				makeMove(start, distance); 
			} else { 
				System.out.println("Illegal move!"); 
			} 
		} 
		
		System.out.println(toString() + "You win!!"); 
		scanner.close();
	} 

	/** 
	 * A demonstration main method. It simply constructs 
	 * a 12-square strip with 5 coins and then plays 
	 * the Silver Dollar Game. 
	 */ 
public static void main (String[] args) { 
		TextCoinStrip tcs = new TextCoinStrip (12, 5); 
		tcs.play();

	
		
	} 

	
}
