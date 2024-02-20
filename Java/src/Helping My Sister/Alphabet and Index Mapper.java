import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

// Print the position of the letter in the alphabet
class Assignment1 {
	public static void main(String[] args) {
		Map<Character, Integer> alphabet = new HashMap<>();
		int index = 1;
		for (char curr = 'a'; curr <= 'z'; curr++) {
			alphabet.put(curr, index++);
		}
		/*
		 * alphabet.put('a', 1);
		 * alphabet.put("b", 2);
		 * alphabet.put("c", 3);
		 * alphabet.put("d", 4);
		 * alphabet.put("e", 5);
		 * alphabet.put("f", 6);
		 * alphabet.put("g", 7);
		 */
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter a Lowercase Letter:");
		char currentLetter = scanner.nextLine().charAt(0);
		scanner.close();

		System.out.println(alphabet.get(currentLetter));
	}
}
