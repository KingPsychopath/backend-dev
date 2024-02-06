
A binary search algorithm is a common example of an `O(log(n))` algorithm. Binary searches work on a sorted list of elements.

The algorithm is as follows:

Given an array of `n` elements sorted from least to greatest, and a target value:

- Set low=0 and high=n-1.
- While low <= high:
    - Set median (the position of the middle element) to `(low+high)//2`, which is the greatest integer less than or equal to `(low+high)/2`
    - If `array[median]` < `target`, set low to `median+1`
    - Otherwise set high to `median-1`
- If (`low != n`) AND (`array[low]` == `target`), return True; the target was found, otherwise return False

Because at each iteration of the search we are halving the size of the search space, the algorithm has a complexity of log2, or `O(log(n))`.

In other words, to add another step to the runtime, we need to double the size of the input. Binary searches are _fast_.