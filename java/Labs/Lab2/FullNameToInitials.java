import java.util.Scanner;

/* 
 * Write a program that takes a full name string, converts it to initials and prints 
 * For example, if the full name is "John Jacob Schmidt" then the program outputs:
 * John Jacob Schmidt: J.J.S.
 */

public class FullNameToInitials {
	public static void main(String[] args) {
		String fullNames[] = { "Timothy John McInerney", "Rick Valenzano", "Inigo Montoya", "Gaga", "Doja Cat",
				"Lil Nas X" };

		// -----------Start below here. To do: approximate lines of code = 2
		// go through all the full names in the array fullNames and use the initials()
		// method to convert each to their initials
		// print the fullName followed by a ": " followed by the initials
		for (int i = 0; i < fullNames.length; i++) {
			String initial = initials(fullNames[i]);
			System.out.println(fullNames[i] + ":" + initial);
		}

		// -----------------End here. Please do not remove this comment. Reminder: no
		// changes outside the todo regions.
		System.out.println("Expected:\nTimothy John McInerney: T.J.M.\n"
				+ "Rick Valenzano: R.V.\n"
				+ "Inigo Montoya: I.M.\n"
				+ "Gaga: G.\n"
				+ "Doja Cat: D.C.\n"
				+ "Lil Nas X: L.N.X.");
	}

	// Takes a full name string as input, extracts and returns the initials
	// Each initial should be followed by a "."
	static String initials(String fullName) {
		// -----------Start below here. To do: approximate lines of code = 6
		// Hint: use a scanner and read each name from the full name, extract the first
		// character
		// and add it (i.e. concatenate) to a result string
		String st = "";
		Scanner in = new Scanner(fullName);

		while (in.hasNext()) {
			String w = in.next();
			st += w.charAt(0) + ".";
		}

		in.close();
		return st;

		// -----------------End here. Please do not remove this comment. Reminder: no
		// changes outside the todo regions.
	}
}
