package practice;

import java.util.HashMap;

public class Hashmaps { // Equivalent to Python's Dictionary
    public static void main(String[] args) {
        // Declaration: you can specify the type of the Hashmap
        // Initialization: you can specify the size of the Hashmap
        HashMap<String, Integer> examScores = new HashMap<>(); // Key: String, Value: Integer

        // Assignment: you can specify the values within the Hashmap
        System.out.println(" Adding elements to the Map");
        examScores.put("John", 90);
        examScores.put("Mary", 80);
        examScores.put("Bob", 85);
        examScores.put("Alice", 95);
        examScores.put("John", 100); // Duplicate

        // Print: you can output the value of the Hashmap to String
        System.out.println(examScores);
        // or System.out.println(examScores.toString());

        // Remove: you can remove the value of the Hashmap
        System.out.println("\n Removing the first element");
        System.out.println("Removing John's Exam Score: " + examScores.get("John"));
        examScores.remove("John");
        System.out.println(".. Attempting to get John's Exam Scores: " + examScores.get("John"));

        // Access: you get the value of a specific key
        System.out.println("\n Accessing the Map");
        System.out.println("Alice's Exam Score: " + examScores.get("Alice"));

        // GetorDefault: you can specify a default value if the key does not exist
        System.out.println("\n Getting the value of a specific key with a default value");
        System.out.println(".. Attempting to get John's Exam Scores: " + examScores.get("John"));
        System.out.println("+John's Exam Score: " + examScores.getOrDefault("John", 0));

        // Contains: you can check if the key or value exists
        System.out.println("\n Checking if the Map contains a specific key");
        System.out.println("Does the Map contain John? " + examScores.containsKey("John"));
        System.out.println("Does the Map contain Alice? " + examScores.containsKey("Alice"));
        System.out.println("Does the Map contain the value 85? " + examScores.containsValue(85));

        // Replace: you can replace the value of a specific key
        System.out.println("\n Replacing the value of a specific key");
        System.out.println("Bob's Exam Score: " + examScores.get("Bob"));
        examScores.replace("Bob", 90);
        System.out.println("Bob's New Exam Score: " + examScores.get("Bob"));

        // Length: you can specify the length of the Hashmap
        System.out.println("\n Length of the Map");
        System.out.println("Length: " + examScores.size());

        // Iteration
        System.out.println("\n Iterating through the Map");
        for (String key : examScores.keySet()) {
            System.out.println(key + ": " + examScores.get(key));
        }

        // Iteration using for-each loop
        System.out.println("\n Iterating through the Map using for-each loop (+5 to scores)");
        examScores.forEach((key, value) -> {
            examScores.replace(key, value + 5);
            System.out.println(key + ": " + value);
        });

        // Copying
        System.out.println("\n Copying the Map");
        HashMap<String, Integer> examScoresCopy = new HashMap<>(examScores);
        System.out.println("Copied Map: " + examScoresCopy.toString());

        // Searching
        System.out.println("\n Searching the Map");
        System.out.println("Does the Map contain John? " + examScores.containsKey("John"));
        System.out.println("Does the Map contain Alice? " + examScores.containsKey("Alice"));

        // Clearing
        System.out.println("\n Clearing the Map");
        examScores.clear();
        System.out.println("Cleared Map: " + examScores.toString());

        // isEmpty: you can check if the Hashmap is empty
        System.out.println("\n Checking if the Map is empty");
        System.out.println("Is the Map empty? " + examScores.isEmpty());

        
    }
}
