# Room Painter 

This Python program calculates the amount of paint needed to paint a set of rooms, taking into account the dimensions of the rooms, the number and types of windows and doors, and the type of paint used.

## Features

- Calculates the total area of paintable surface in a room, subtracting the area of windows and doors.
- Supports different shapes of windows and doors, including squares, circles, and triangles.
- Supports different types of paint, each with its own coverage rate and price.
- Recommends the best paint option based on the total area and the paint types.

## Usage

1. Define the rooms, windows, and doors in the `rooms` and `windows_doors` lists at the top of the script. Each room is a list of walls, and each wall is a tuple of (length, height). Each window or door is a tuple of (shape, dimensions).

2. Run the script. The script will calculate the total area of paintable surface and the amount of paint needed.

# Intuition

The Volume though relevant is not the most important factor here; in order to determine how many cans of paint we need to cover a certain area we need a comparable factor - that is the coverage rate. The coverage rate of a paint is the amount of surface area(meters-squared) that can be covered by a given volume of paint.

The coverage rate of a paint is typically provided by the manufacturer because it depends on the specific formulation of the paint, including factors like the type and amount of pigment and binder used. It's not something that can be calculated from the volume alone.

However, if you know the coverage rate for a specific volume (for example, 400 square feet per gallon), and you want to find out the coverage rate for a different volume, you can use a simple proportion.

For example, if you know that one gallon (approximately 3.78 liters) covers 400 square feet, and you want to find out how much area one liter will cover, you can set up the following proportion:

```400 sq ft     x sq ft
---------  =  --------
1 gallon      1 liter```

Solving for x gives x = 400 sq ft / 3.78 = 105.82 sq ft. So one liter of this paint will cover approximately 105.82 square feet.

```

In Python, you could calculate this as follows:

```python
coverage_rate_per_gallon = 400  # coverage rate in square feet per gallon
gallons_per_liter = 1 / 3.78  # conversion factor from gallons to liters
coverage_rate_per_liter = coverage_rate_per_gallon * gallons_per_liter
```

This will give you the coverage rate in square feet per liter.

Whether you're painting a powder room or the exterior of your house, paint coverage is fairly universal. The general rule of thumb is one gallon(4L) per 400 square feet.
--> https://www.architecturaldigest.com/story/how-much-paint-do-i-need


# Solution

## Calculating the Total Area of Paintable Surface
The coverage rate for paint is typically given in square meters per litre. This means that one litre of paint will cover a certain number of square meters.

When you divide the total area to be painted (in square meters) by the coverage rate (in square meters per litre), the square meter units cancel out, leaving you with the result in litres.

This is because when you divide a quantity by a rate, you get the amount of the rate's denominator required to cover the quantity. In this case, you're dividing an area (in square meters) by a rate of area per volume (in square meters per litre), so you get a volume (in litres).

This is a common calculation in many fields. For example, if you're driving a car and you know how many miles you're going to drive and your car's fuel efficiency in miles per gallon, you can calculate how many gallons of fuel you'll need by dividing the total miles by the miles per gallon.

## The Recomennded Paint Option
The recommended paint option is the one that gives the best value for money. In other words, it's the one that gives you the most paint for the least amount of money.

To calculate this, you need to know the price of each paint option and the amount of paint it provides. You can then divide the price by the amount of paint to get the price per unit of paint. The paint option with the lowest price per unit of paint is the best value for money.

To calculate this I used both a brute force method and a more elegant method. The brute force method is to calculate the price per unit of paint for each paint option, and then compare them to find the lowest price per unit of paint.

The more elegant method used dynamic programming to calculate the price per unit of paint for each paint option, and then compare them to find the lowest price per unit of paint (*I could not get this to work yet*)

## Calculating the Total Cost
The total cost is the price of the paint multiplied by the number of cans required.

# Issues Faced
At one point, I was calculating the total area of the windows and doors, and then subtracting that from the total area of each wall. 

However, this was giving me the wrong answer. My original intention was to subtract the flat area of shapes from the flat area of walls. This resulted in  my paintable area being too small.

I solved this by refactoring my functions to calculate the area of the walls, windows, and doors separately; and then subtracting the area of the windows and doors from the area of the walls.

## Functions
The `room_painter.py` script contains the following main functions:

**The initial general use functions are:**
- `wall_area(length, height)`: Returns the area of a wall.
- `square_area(side)`: Returns the area of a square.
- `circle_area(radius)`: Returns the area of a circle.
- `triangle_area(base, height)`: Returns the area of a triangle.

**The implementation specific functions include:**
1. `total_paintable_area(rooms, windows_doors)`: This function calculates the total paintable area in square meters. It takes two arguments: `rooms`, a list of rooms where each room is represented as a list of walls, and `windows_doors`, a list of windows and doors where each window/door is represented as a tuple of shape and dimensions.

2. `total_paint_volume(total_area, paint_type)`: This function calculates the total volume of paint required in liters. It takes two arguments: `total_area`, the total paintable area in square meters, and `paint_type`, a string representing the type of paint to be used.

3. `total_paint_cans(total_area, paint_type)`: This function calculates the total number of paint cans required. It takes the same arguments as `total_paint_volume`.

4. `total_paint_cost(total_area, paint_type)`: This function calculates the total cost of the paint required. It also takes the same arguments as `total_paint_volume`.

5. `run_room_painter()`: This is the main function that runs the room painter program. It doesn't take any arguments. It prompts the user to input the details of the rooms, windows, doors, and the type of paint to be used, and then it calculates and prints the total paintable area, the volume of paint required, the number of paint cans required, and the total cost.

6. 'best_paint_option(total_area, paint_types)': This function calculates the best paint option based on the total area and the paint types. It takes two arguments: `total_area`, the total paintable area in square meters, and `paint_types`, a list of paint types.

Please note that these functions assume that the dimensions of the walls, windows, and doors are in meters, and that the volume of the paint cans is in liters.

## Future Improvements

1. Add support for different units of measurement, including feet, inches, and gallons.
2. Add support for different shapes of windows and doors, including trapezoids and parallelograms.
3. Add support for curved walls, windows, and doors.
4. Add a GUI.
5. Add a comparison function that compares the cost of different types of paint; for example, it could calculate the cost of painting the same room with different types of paint, and then print the results in a table and suggest the cheapest option, or the set of options that give the best value for money.
6. Change invalid literal for int() with base 10: '' to a more user friendly message (e.g. "Please enter a number") - happens when you put a string into some inputs i.e rooms.

### DP Solution
 The idea is to use a table to store the minimum cost for each possible total area up to the given total area. Then, for each type of paint, we update the table entries for all total areas that can be covered by that type of paint.

```python
def best_paint_option(total_area):
    # Initialize the cost table with infinity for all entries except the first one
    cost_table = [0] + [float('inf')] * total_area

    # For each type of paint...
    for paint_type, paint in paints.items():
        # For each total area that can be covered by this type of paint...
        for area in range(paint['coverage_rate'], total_area + 1):
            # Update the cost table entry for this total area if using this type of paint is cheaper
            cost_table[area] = min(cost_table[area], cost_table[area - paint['coverage_rate']] + paint['price'])

    # Find the best paint option by finding the type of paint that results in the minimum cost for the given total area
    best_option = {paint_type: 0 for paint_type in paints}
    area = total_area
    while area > 0:
        for paint_type, paint in paints.items():
            if area >= paint['coverage_rate'] and cost_table[area] == cost_table[area - paint['coverage_rate']] + paint['price']:
                best_option[paint_type] += 1
                area -= paint['coverage_rate']
                break

    return best_option
```

This function assumes that the `paints` dictionary is available in the global scope and that it's acceptable to buy more paint than needed as long as it's the cheapest option. If these assumptions are not correct, you may need to adjust the function accordingly.

This function is more efficient than the brute force one because it only needs to iterate over each total area once for each type of paint, rather than iterating over all possible combinations of paint cans. However, it uses more memory because it needs to store a cost table entry for each total area.


## Dependencies

This program requires Python 3. It uses the `math` module from the Python Standard Library.

## License

This project is licensed under the terms of the MIT license.