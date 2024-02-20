**Could you give me a hint as to how I would do implement the 4 corners of the rectangle in an overlapping function, how many conditions would I need to check for the overlaps with my current refactor of the rectangle class to using tuples with the coordinates**

To determine the logic for the overlaps() function, let's prime our thoughts with a question: when would two rectangles (A & B) not overlap?

They would not overlap when one is to the extreme right or left, or the top or bottom of the other, agreed? So, in a sense, all four corners of rectangle A are 'more' to one side than rectangle B, and vice versa, would denote a lack of overlap.

In your tuple-powered Rectangle, this translates to: Rectangle A doesn't overlap with Rectangle B if any one of these conditions is true:

    The topmost point of A is below the bottommost point of B
    The bottommost point of A is above the topmost point of B
    The leftmost point of A is to the right of the rightmost point of B
    The rightmost point of A is to the left of the leftmost point of B

See if you can translate these conditions into code! Avoid thinking about the overlapping scenario and focus on when they do not overlap, and negate the statement. Sometimes, thinking about the converse scenario makes it easier to implement the logic.



**I'm not sure, which condition is missing?**


No worries! Let's go through this together.

You already have:

    The left x-coordinate of Rectangle A is less than or equal to the right x-coordinate of Rectangle B
    The right x-coordinate of Rectangle A is greater than or equal to the left x-coordinate of Rectangle B
    The top y-coordinate of Rectangle A is greater than or equal to the bottom y-coordinate of Rectangle B

Now let's consider when Rectangle A could be completely below rectangle B. How would the bottom y-coordinate of Rectangle A compare to the top y-coordinate of Rectangle B in this case?

**The bottom y-coordinate of Rectangle A is less than or equal to the top y-coordinate of Rectangle B?**

That's exactly right! If Rectangle A is completely below Rectangle B, then the bottom y-coordinate of Rectangle A is definitely less than or equal to the top y-coordinate of Rectangle B.

Now you should have all the conditions you need for the overlaps() function! With all four conditions, you're ensuring that neither rectangle is completely to the left, right, above or below the other, which means they must overlap.


**Is my code too complex now?**

Would it be better to just have the bottom left and top right as variables in the constructor to represent a straight line from one corner to another and calculate the other individual points by using the indexes of those tuples in the get_bottom_right etc. methods

Your current approach isn't unnecessarily complex, but indeed, the choice between storing all four corners or two distance corners depends on various factors like memory usage, cleanliness of code, or the methods being implemented using these points.

Storing just two corners, such as bottom left and top right (or any other two diagonal corners), will indeed reduce memory usage compared to storing all four corners. And given that you can calculate the other two corners from these points, it's a reasonable approach if methods like overlaps are the main usage of these points.

To help decide, imagine you needed to add more methods to the Rectangle class that deal with the coordinates. Would calculating the other corners every time be more efficient, or would it be better to have all four corners readily available?

Also, how would readability and maintainability of code be impacted by the change you proposed? Could there be potential for confusion or mistakes when calculating other corners?

Keep these factors in mind while making your decision and implement what you think would be best for the specific situation and anticipated future scenarios.
