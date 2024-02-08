class Arrays {
    public static void main(String[] args) {
        // Declaration: you can specify the type of the array (int[] arr;)
        // Initialization: you can specify the size of the array (int[] arr = new
        // int[5];)
        int[] arr = new int[5];

        // Assignment: you can specify the value of the array (arr[0] = 1;)
        arr[0] = 1;
        arr[1] = 2;
        arr[2] = 3;
        arr[3] = 4;
        arr[4] = 3;

        // Access: you can specify the index of the array (arr[0];)
        System.out.println("\n Accessing the array");
        System.out.println("Index 3: " + arr[3]);

        
        // Print: you can output the value of the array to String
        System.out.println("\n Printing the array");   
        String[] array = new String[] {"John", "Mary", "Bob"};
        System.out.println(java.util.Arrays.toString(array));
        System.out.println(java.util.Arrays.toString(arr));
        
        // Length: you can specify the length of the array (arr.length;)
        System.out.println("\n Length of the array");
        System.out.println(String.format("Length: %d", arr.length));

        // Iteration
        System.out.println("\n Iterating through the array");
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }

        System.out.println("\n Iterating through the array using for-each loop");
        for (int i : arr) {
            System.out.println(i);
        }

        // Copying
        System.out.println("\n Copying the array");
        int[] arrCopy = new int[arr.length];
        System.arraycopy(arr, 0, arrCopy, 0, arr.length);
        System.out.println("Copied Array: ");
        for (int i : arrCopy) {
            System.out.println(i);
        }

        // Sorting
        System.out.println("\n Sorting the array");
        java.util.Arrays.sort(arr);

        for (int i : arr) {
            System.out.println(i);
        }

        // Searching
        System.out.println("\n Searching the array");
        int index = java.util.Arrays.binarySearch(arr, 3);
        System.out.println(String.format("Index of 3: %d", index));

        // Conversion
        System.out.println("\n Converting the array to String");
        String arrString = java.util.Arrays.toString(arr);
        System.out.println(arrString);


        // Multidimensional Arrays
        System.out.println("\n Multidimensional Arrays");
        int[][] arr2D = new int[2][3];
        arr2D[0][0] = 1;
        arr2D[0][1] = 2;
        arr2D[0][2] = 3;
        arr2D[1][0] = 4;
        arr2D[1][1] = 5;
        arr2D[1][2] = 6;

        int[][] arr2D2 = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        // Printing 2D Array
        for (int i = 0; i < arr2D.length; i++) {
            for (int j = 0; j < arr2D[i].length; j++) {
                System.out.print(arr2D[i][j] + " ");
            }
            System.out.println();
        }
        
    }
}