Sure, here are some examples of lambda expressions in Java:

1. **Sorting a list of strings by length:**

    ```java
    List<String> words = Arrays.asList("Lambda", "expressions", "are", "cool");
    Collections.sort(words, (s1, s2) -> Integer.compare(s1.length(), s2.length()));
    ```

2. **Running a thread:**

    ```java
    new Thread(() -> System.out.println("Running a thread")).start();
    ```

3. **Filtering a list:**

    ```java
    List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
    List<Integer> evenNumbers = numbers.stream()
                                        .filter(n -> n % 2 == 0)
                                        .collect(Collectors.toList());
    ```

4. **Mapping a list to a different value:**

    ```java
    List<String> words = Arrays.asList("Lambda", "expressions", "are", "cool");
    List<Integer> wordLengths = words.stream()
                                      .map(s -> s.length())
                                      .collect(Collectors.toList());
    ```

5. **Reducing a list to a single value:**

    ```java
    List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
    int sum = numbers.stream()
                     .reduce(0, (a, b) -> a + b);
    ```

In all these examples, the part after the `->` is the body of the lambda, which gets executed when the lambda is called. The part before the `->` are the parameters of the lambda.