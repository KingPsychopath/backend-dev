import math
store_name = "Abel's Paint Store"

# Dictionary of paints with their coverage rates and prices
paints = {
    'premium': {'coverage_rate': 400, 'price': 50},
    'standard': {'coverage_rate': 350, 'price': 30},
    'economy': {'coverage_rate': 300, 'price': 20},
}

rooms = [] # List of rooms, each room is a list of walls
windows_doors = [] # List of windows/doors, each window/door is a tuple of shape and dimensions (list)

# Functions for calculating area of shapes

def wall_area(length, height):
    return length * height

def square_area(side):
    return side * side

def circle_area(radius):
    return math.pi * radius * radius

def triangle_area(base, height):
    return 0.5 * base * height

# Functions for calculating paint area

def wall_paint_area(length, height, windows_doors):
    total_area = wall_area(length, height)
    for shape, dimensions in windows_doors:
        if shape == 'square':
            total_area -= square_area(*dimensions)
        elif shape == 'circle':
            total_area -= circle_area(*dimensions)
        elif shape == 'triangle':
            total_area -= triangle_area(*dimensions)
    return total_area

def room_paint_area(walls, windows_doors):
    total_area = 0
    for wall in walls:
        total_area += wall_paint_area(*wall, windows_doors)
    return total_area

def total_paint_area(rooms, windows_doors):
    total_area = 0
    for room in rooms:
        total_area += room_paint_area(room, windows_doors)
    return total_area

def paint_required(total_area, paint_type):
    paint = paints[paint_type]
    coverage_rate = paint['coverage_rate']
    price_per_can = paint['price']

    # Calculate the number of cans needed, rounding up to the nearest whole number
    cans_needed = math.ceil(total_area / coverage_rate)

    # Calculate the total cost
    total_cost = cans_needed * price_per_can

    # Calculate the total volume of paint needed
    total_calculated_volume = total_area / coverage_rate

    return cans_needed, total_cost, total_calculated_volume

def get_paint_type():
    print("Select paint type:")
    for paint in paints:
        print(paint.capitalize())
    paint_type = input("Enter paint type: ")

    # Check if paint type is valid
    while paint_type.lower() not in paints:
        print("Invalid paint type")
        paint_type = input("Enter paint type: ")
    return paint_type

# Functions for user input

def get_dimensions():
    length = float(input("Enter length: "))
    height = float(input("Enter height: "))
    return (length, height)

def get_rooms():
    rooms = []
    num_rooms = int(input("Enter the number of rooms: "))
    for i in range(num_rooms):
        print(f"Room {i+1}")
        num_walls = int(input("Enter the number of walls: "))
        walls = []
        for j in range(num_walls):
            print(f"Wall {j+1}")
            walls.append(get_dimensions())
        rooms.append(walls)
    return rooms

def get_windows_doors():
    windows_doors = []
    num_windows_doors = int(input("Enter the number of windows/doors: "))
    for i in range(num_windows_doors):
        print(f"Window/Door {i+1}")
        shape = input("Enter shape (square/circle/triangle): ")
        if shape.lower() == 'square':
            dimensions = [float(input("Enter side length: "))]
        elif shape.lower() == 'circle':
            dimensions = [float(input("Enter radius: "))]
        elif shape.lower() == 'triangle':
            dimensions = get_dimensions()
        windows_doors.append((shape, dimensions))
    return windows_doors

# Testing

def test_paint_required():
    rooms = [
        [(10, 8), (10, 8), (12, 8), (12, 8)],  # Room 1: 4 walls
        [(15, 8), (15, 8), (20, 8), (20, 8)]   # Room 2: 4 walls
    ]

    windows_doors = [
        ('door', [2, 6]),     # Door: 2x6
        ('window', [2, 2]),   # Window: 2x2
        ('window', [2, 2])    # Window: 2x2
    ]
    paint_type = 'premium'
    total_area = total_paint_area(rooms, windows_doors)

    cans_needed, total_cost, total_volume = paint_required(total_area, paint_type)

    print(cans_needed)
    print(total_cost)
    print(total_volume)
    assert cans_needed == 3
    assert total_cost == 150
    assert total_volume == 2.28

test_paint_required()

print(f"""Hi, welcome to {store_name}!
      I'll help you calculate the amount of paint you need to buy.
      You will need to enter the dimensions of the rooms and windows/doors.
        You can enter as many rooms and windows/doors as you like.
        You can enter the dimensions in feet or meters.
        You can enter the dimensions in decimal form.
      
        Let's get started!
      """)

rooms = get_rooms()
windows_doors = get_windows_doors()
paint_type = get_paint_type()

total_area = total_paint_area(rooms, windows_doors)
cans_needed, total_cost, calculated_volume = paint_required(total_area, paint_type)

print(f'\nTotal Area to be covered: {round(total_area, 2)} metres-squared')
print(f'Total Volume of Paint Required: {round(calculated_volume, 2)} cubic-metres\n')

print(f'Paint cans needed: {cans_needed}')
print(f'Total cost: £{total_cost}')