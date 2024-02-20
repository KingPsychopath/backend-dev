package practice;

import java.util.Scanner;

public class Scanning {
    public static void main(String[] args) {
        String words = "TestString 123 Test 123 Haha";
        Scanner fromStr = new java.util.Scanner(words);
        fromStr.useDelimiter("[^0-9]+");
        while (fromStr.hasNext()) {
            if (fromStr.hasNextInt()) {
                System.out.println(fromStr.nextInt());
                System.out.println(fromStr.nextInt());
            } else {
                System.out.println(fromStr.next());
            }
        }
    }
}
