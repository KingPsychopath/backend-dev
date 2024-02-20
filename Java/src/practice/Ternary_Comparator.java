package practice;

public class Ternary_Comparator {
    public static void main(String[] args) {
        int a = 5;
        int b = 6;
        int c = 7;
        int max = (a > b) ? (a > c ? a : c) : (b > c ? b : c);
        System.out.println(max);

        // Ternary Comparator
        // The ternary operator is a conditional operator that returns a value based on a condition. It is a shorthand for the if-then-else statement.
        // Syntax: (condition) ? (value if true) : (value if false)
        // Example: int max = (a > b) ? (a > c ? a : c) : (b > c ? b : c);
        // The above code compares three numbers and returns the maximum value.
    }
}
