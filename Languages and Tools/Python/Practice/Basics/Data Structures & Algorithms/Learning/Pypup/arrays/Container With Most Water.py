# Define a function called max_area that takes in a list of integers called height
def max_area(height):
   # Initialize two pointers, left and right, to the start and end of the list respectively
   left = 0
   right = len(height) - 1
   # Initialize a variable called max_area to 0
   max_area = 0

   # While the left pointer is less than the right pointer
   while left < right:
       # Calculate the current area by taking the minimum value between the heights at the left and right pointers and multiplying it by the distance between them
       current_area = min(height[left], height[right]) * (right - left)
       # Update the max_area variable to be the maximum value between the current area and the previous max_area
       max_area = max(max_area, current_area)

       # If the height at the left pointer is less than the height at the right pointer, move the left pointer to the right
       if height[left] < height[right]:
           left += 1
       # Otherwise, move the right pointer to the left
       else:
           right -= 1

   # Return the max_area variable
   return max_area

'''
The distance between the two lines is represented by (right - left) because left and right are indices in the height list that represent the positions of the two lines.

In the context of this problem, the "distance" between two lines is the number of positions between them in the list. Since list indices in Python start at 0 and increase by 1 for each position, the difference between the indices of two positions is equal to the number of positions between them.

For example, if left is at index 2 and right is at index 5, the distance between them is 5 - 2 = 3, which means there are 3 positions between them. This distance is used to calculate the area of the water that can be contained between the two lines, as the area is equal to the distance between the lines (the width of the container) multiplied by the height of the shorter line (the depth of the water).
'''