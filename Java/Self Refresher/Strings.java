public class Strings {
    public static void main(String[] args) {
        // Declaration: you can specify the type of the array (String str;)
        // Initialization: you can specify the value of the array (String str =
        // "Hello";)
        String str = "Hello";

        // Access: you can specify the index of the array (str.charAt(0);)
        System.out.println(str.charAt(0));
        System.out.println(str.charAt(1));
        System.out.println(str.charAt(2));
        System.out.println(str.charAt(3));
        System.out.println(str.charAt(4));

        // Length: you can specify the length of the array (str.length();)
        System.out.println(String.format("Length: %d", str.length()));

        // Concatenation: you can specify the value of the array (str.concat(" World");)
        System.out.println(str.concat(" World"));

        // Substring: you can specify the value of the array (str.substring(0, 3);)
        System.out.println(str.substring(0, 3));

        // Replace: you can specify the value of the array (str.replace("Hello", "Hi");)
        System.out.println(str.replace("Hello", "Hi")); // Output: Hi

        // Trim: you can specify the value of the array (str.trim();)
        System.out.println("  Hello  ".trim()); // Output: Hello

        // Lowercase: you can specify the value of the array (str.toLowerCase();)
        System.out.println("Hello".toLowerCase()); // Output: hello

        // Uppercase: you can specify the value of the array (str.toUpperCase();)
        System.out.println("Hello".toUpperCase()); // Output: HELLO

        // Empty: you can specify the value of the array (str.isEmpty();)
        System.out.println("".isEmpty()); // Output: true

        // Equals: you can specify the value of the array (str.equals("Hello");)
        System.out.println("Hello".equals("Hello")); // Output: true

        // EqualsIgnoreCase: you can specify the value of the array
        // (str.equalsIgnoreCase("hello");)
        System.out.println("Hello".equalsIgnoreCase("hello")); // Output: true

        // Contains: you can specify the value of the array (str.contains("Hello");)
        System.out.println("Hello".contains("Hello")); // Output: true

        // StartsWith: you can specify the value of the array (str.startsWith("Hello");)
        System.out.println("Hello".startsWith("Hello")); // Output: true

        // EndsWith: you can specify the value of the array (str.endsWith("Hello");)
        System.out.println("Hello".endsWith("Hello")); // Output: true

        // IndexOf: you can specify the value of the array (str.indexOf("Hello");)
        System.out.println("Hello".indexOf("Hello")); // Output: 0

        // Java 15: Text Blocks (Java 13)
        /*
         * Hello,
         * This is a text block in Java.
         * It spans multiple lines.
         */
        String textBlock = """
                Hello,
                This is a text block in Java.
                It spans multiple lines.
                """;

        System.out.println(textBlock);
    }
}
