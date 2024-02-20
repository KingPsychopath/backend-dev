# Define a function that takes a matrix as input
def transpose_matrix(matrix):
    # Create an empty list to store the transposed matrix
    transposed_matrix = []
    # Loop through the range of the length of the first row of the matrix
    for i in range(len(matrix[0])):
        # Create an empty list to store each transposed row
        transposed_row = []
        # Loop through each row in the matrix
        for row in matrix:
            # Append the element at index i of each row to the transposed row list
            transposed_row.append(row[i])
        # Append the transposed row list to the transposed matrix list
        transposed_matrix.append(transposed_row)

        #  Equivalent to
        # transposed_row = [row[i] for row in matrix]
        
    # Return the transposed matrix
    return transposed_matrix

# Define a matrix
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
new_matrix = [row[i] for row in matrix for i in range(len(matrix[0]))]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Call the transpose_matrix function with the matrix as input and print the result
print(transpose_matrix(matrix))
print(new_matrix)

# Explain the syntax difference why is it now transposed? What does the bracketing of the first loop do
'''
The two lines of code you provided are list comprehensions in Python, which are a concise way to create lists.

new_matrix = [row[i] for row in matrix for i in range(len(matrix[0]))]

This line of code is trying to create a new matrix, but it doesn't correctly transpose the original matrix. The inner loop (for i in range(len(matrix[0]))) is inside the outer loop (for row in matrix), but without any grouping brackets. This means that for each row in the matrix, it's trying to add every element from every column to the new matrix, which results in a flattened list rather than a transposed matrix.

transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

This line of code correctly transposes the original matrix. The difference here is the placement of the brackets. The inner list comprehension ([row[i] for row in matrix]) is grouped together, which means for each i in the range of the length of the first row of the matrix, it's creating a new list where each element is the ith element from each row. This effectively turns the columns of the original matrix into rows, creating the transposed matrix.

In summary, the bracketing of the first loop in the second line of code groups the inner loop together, creating a new list for each iteration of the outer loop. This results in a list of lists (a matrix), rather than a flattened list.
'''
# Which part of each nestled loop in the list comprehension is executed first in both cases
'''
In Python, list comprehensions are executed from left to right, but the order of execution can be a bit tricky to understand when there are nested loops. Here's how it works for both of your list comprehensions:

new_matrix = [row[i] for row in matrix for i in range(len(matrix[0]))]

In this list comprehension, the for row in matrix loop is executed first. For each row, the inner loop for i in range(len(matrix[0])) is then executed. The expression row[i] is evaluated for each combination of row and i.

transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

In this list comprehension, the outer loop for i in range(len(matrix[0])) is executed first. For each i, a new list is created by the inner list comprehension [row[i] for row in matrix]. This inner list comprehension iterates over each row in matrix and evaluates the expression row[i].

So, in both cases, the outer loop is executed first, and then for each iteration of the outer loop, the inner loop is executed. The difference between the two list comprehensions is the placement of the loops and the use of brackets, which changes how the results are grouped.
'''