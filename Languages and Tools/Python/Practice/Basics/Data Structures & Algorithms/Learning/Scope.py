# Global variable x
x = 1

# Define an outer function
def outer():
    # Local variable x in the scope of outer function
    x = 2

    # Define an inner function
    def inner():
        # Local variable x in the scope of inner function
        x = 3
        # Print the value of x in the scope of inner function -> looks for variable in the nearest scope
        print(f"Inner sees x equals to {x}")
        return
    
    # Call the inner function
    inner()
    # Print the value of x in the scope of outer function
    print(f"Outer sees x equals to {x}")
    return

# Call the outer function
outer()
# Print the value of x in the scope of Global function
print(f"Global sees x equals to {x}")

# Output: 3, 2 , 1
# ALl 3 of these variables are each named x, but they are in different scopes so they are located in different areas in memory 
# thus their values are different.
