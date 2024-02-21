def is_single_branching_polyline(lines):
    # Create a dictionary to store the connections for each point
    # This will help us keep track of how many other points each point is connected to
    connections = {}

    # Iterate over the lines
    for line in lines:
        # Unpack the line into two points
        # These are the two endpoints of the line
        point1, point2 = line

        # Add the points to the connections dictionary
        # If a point is not already in the dictionary, we add it and initialize its set of connected points
        if point1 not in connections:
            connections[point1] = set()
        if point2 not in connections:
            connections[point2] = set()

        # Add the connection between the two points
        # We add each point to the set of connected points for the other point
        connections[point1].add(point2)
        connections[point2].add(point1)

    # Check if the polyline is single branching
    # A single branching polyline will have exactly two endpoints (points connected to only one other point)
    # and all other points will be connected to exactly two other points
    endpoints = 0
    for _, connected_points in connections.items():
        if len(connected_points) == 1:
            # This is an endpoint, so we increment the count of endpoints
            endpoints += 1
        elif len(connected_points) != 2:
            # This point is connected to more or less than two other points, so the polyline is not single branching
            return False

    # If we have exactly two endpoints and all other points are connected to exactly two other points,
    # then the polyline is single branching
    return endpoints == 2

# Test case 1: A simple straight line
lines = [(1, 2), (2, 3), (3, 4)]
print(is_single_branching_polyline(lines))  # Expected output: True

# Test case 2: A polyline with a branch
lines = [(1, 2), (2, 3), (3, 4), (2, 5)]
print(is_single_branching_polyline(lines))  # Expected output: False

# Test case 3: A polyline with a loop
lines = [(1, 2), (2, 3), (3, 4), (4, 1)]
print(is_single_branching_polyline(lines))  # Expected output: False

# Test case 4: A single point
lines = [(1, 1)]
print(is_single_branching_polyline(lines))  # Expected output: False

# Test case 5: Two separate lines
lines = [(1, 2), (3, 4)]
print(is_single_branching_polyline(lines))  # Expected output: False
