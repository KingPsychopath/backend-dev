package practice;

import java.util.ArrayList;

class ArrayLists {
    public static void main(String[] args) {
        // Declaration: you can specify the type of the array 
        // Initialization: you can specify the size of the array 
        ArrayList<Integer> list = new ArrayList<>();

        // Assignment: you can specify the values within the array
        System.out.println("\n Adding elements to the array");
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(3);

        // Print: you can output the value of the array to String
        // The toString() method is automatically called when you print the array
        System.out.println(list);

        // Remove: you can remove the value of the array
        System.out.println("\n Removing the first element");
        list.remove(0);
        System.out.println(list.get(0));

        // Access: you get the value of a specific index
        System.out.println("\n Accessing the array");
        System.out.printf("Index 0: %d%n", list.get(0));

        // Length: you can specify the length of the array
        System.out.println("\n Length of the array");
        System.out.printf("Length: %d%n", list.size());

        // Iteration
        System.out.println("\n Iterating through the array");
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }

        System.out.println("\n Iterating through the array using for-each loop");
        for (int i : list) {
            System.out.println(i);
        }

        System.out.println("\n Iterating through the array using lambda expression i * 2");
        list.forEach(i -> {
            System.out.println(i * 2);
        });

        // Copying
        System.out.println("Copying the array");
        ArrayList<Integer> listCopy = new ArrayList<>(list);
        System.out.println("Copied Array: " + listCopy);

        // Sorting
        System.out.println("\n Sorting the array");
        list.sort(null);

        for (int i : list) {
            System.out.println(i);
        }

        // Searching
        System.out.println("\n Searching the array");
        int index = list.indexOf(3);
        System.out.printf("Index of 3: %d%n", index);

        // Clearing
        System.out.println("\n Clearing the array");
        list.clear();
        System.out.println(list);

    }
}