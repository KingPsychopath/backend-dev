import math
store_name = "Abel's Paint Store"

# Dictionary of paints with their coverage rates(m^2), prices and volumes(l) (stored as a dictionary of dictionaries)
paints = {
    'premium': {'coverage_rate': 400, 'price': 50, 'volume': 4},
    'standard': {'coverage_rate': 350, 'price': 30, 'volume': 5},
    'economy': {'coverage_rate': 300, 'price': 20, 'volume': 10},
}
# Premium covers 400 metres-squared per can and costs £50 meaning it has a coverage rate of 8 metres-squared per £1
# Standard covers 350 metres-squared per can and costs £30 meaning it has a coverage rate of 11.67 metres-squared per £1
# Economy covers 300 metres-squared per can and costs £20 meaning it has a coverage rate of 15 metres-squared per £1

# The amount of litres of paint required is the total area divided by the coverage rate
# The total volume is the total area divided by the coverage rate (Litres is a measure of volume)

# The number of cans required is the amount of litres required divided by the volume of a can (5 litres)
# The total cost is the number of cans required multiplied by the price per can

# The total area is the sum of the areas of each wall minus the area of each window/door

rooms = [] # List of rooms, each room is a list of walls - stored as (length: float, height: float)
windows_doors = [] # List of windows/doors, each window/door is a tuple of shape and dimensions - stored as (shape: string, [dimensions: float])

# Base Functions for calculating area of shapes
#  Each function takes the dimensions as arguments

def rect_area(length, height) -> float:
    return length * height

def square_area(side) -> float:
    return side * side

def circle_area(radius) -> float:
    return math.pi * radius * radius

def triangle_area(base, height) -> float:
    return 0.5 * base * height

# Functions for calculating Paint Area for all relevant items
#   Each function takes a list of dimensions as an argument

def wall_paint_area(length: float, height: float, windows_doors: list[tuple[str, list[float]]]) -> float:
    '''
    Returns the area of paintable surface on a wall.
        Calls rect_area() for the total area of the wall. (length * height)
        Subtracts the area of each window/door from the total area.
    '''
    total_area = rect_area(length, height)
    if windows_doors:
        for shape, dimensions in windows_doors:
            if shape == 'square':
                total_area -= square_area(*dimensions)
            elif shape == 'rectangle':
                total_area -= rect_area(*dimensions)
            elif shape == 'circle':
                total_area -= circle_area(*dimensions)
            elif shape == 'triangle':
                total_area -= triangle_area(*dimensions)
    return total_area

def room_paint_area(walls: list[tuple[float, float]], windows_doors: list[tuple[str, list[float]]]) -> int:
    '''
    Returns the total area of paintable surface in a room.
        Calls wall_paint_area() for each wall.
    '''
    total_area = 0
    for wall in walls:
        total_area += wall_paint_area(*wall, windows_doors)
    #print(f'Total Area of Room (including fixtures): {total_area}')
    return total_area

def total_paint_area(rooms: list[list[tuple[float, float]]], windows_doors: list[tuple[str, list[float]]]) -> int:
    '''
    Returns the total area of paintable surface.
        Calls room_paint_area() for each room.
    '''
    total_area = 0
    for room in rooms:
        total_area += room_paint_area(room, windows_doors)
    return total_area

## Functions for calculating volume of paint required

def total_paint_volume(total_area: int, paint_type: str) -> float:
    """
    Returns the total volume of paint required.
    """
    coverage_rate = paints[paint_type]['coverage_rate']
    volume_required = total_area / coverage_rate
   # liters_required = cubic_meters_to_liters(cubic_meters_required)

    return volume_required

def total_paint_cans(total_area: int, paint_type: str):
    '''
    Returns the number of cans of paint required.
    '''
    coverage_rate = paints[paint_type]['coverage_rate']
    cans_required = math.ceil(total_area / coverage_rate)

    return cans_required

def total_paint_cost(total_area: int, paint_type: str) -> int:
    '''
    Returns the total cost of paint required.
    '''
    paint = paints[paint_type]
    price_per_can = paint['price']

    total_cost = total_paint_cans(total_area, paint_type) * price_per_can
    return total_cost
    

def get_paint_type() -> str:
    '''
    Prompts the user to select a paint type.
    Returns the paint type.
    '''
    print("Select paint type:")
    for paint in paints:
        print(paint.capitalize())

    paint_type = input("Enter paint type: ").lower()
    while paint_type not in paints:
        print("Invalid paint type")
        paint_type = input("Enter paint type: ").lower()
    return paint_type

# Functions for user input

def get_dimensions() -> tuple[float, float]:
    """
    Prompts the user to enter the length and height of a shape.
    Returns a tuple of the length and height.
    """
    while True:
        try:
            length = float(input("      Enter length: "))
            height = float(input("      Enter height: "))
            if (length <= 0 or height <= 0) or (type(length) != float or type(height) != float):
                raise ValueError("Length and height must be positive numbers.")
            break
        except ValueError as err:
            print(f"Invalid input: {err}")
    return (length, height)

def get_rooms() -> list[list[tuple[float, float]]]:
    """
    Prompts the user to enter the number of rooms and their respective walls' dimensions.
    Returns a list of rooms, where each room is represented by a list of walls' dimensions.
    """
    rooms = []
    while True:
        try:
            num_rooms = int(input("Enter the number of rooms: "))
            if num_rooms <= 0 or type(num_rooms) != int:
                raise ValueError("Number of rooms must be a positive integer.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    for i in range(num_rooms):
        print(f"Room {i+1}")
        while True:
            try:
                num_walls = int(input(" Enter the number of walls: "))
                if num_walls <= 0 or type(num_walls) != int:
                    raise ValueError("Number of walls must be a positive integer.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        walls = []
        for j in range(num_walls):
            print(f"Wall {j+1}")
            walls.append(get_dimensions())
        rooms.append(walls)
    return rooms

def get_windows_doors() -> list[tuple[str, list[float]]]:
    '''
    Prompts the user to enter the number of windows/doors and their respective dimensions.
    Returns a list of windows/doors, where each window/door is represented by a tuple of shape and dimensions.
    '''
    windows_doors = []
    while True:
        try:
            num_windows_doors = int(input("Enter the number of windows/doors: "))
            if type(num_windows_doors) != int:
                raise ValueError("Number of windows/doors must be an integer.")
            if num_windows_doors < 0:
                raise ValueError("Number of windows/doors must be a positive integer, greater than 0.")
            if num_windows_doors == 0:
                print("You've chosen no Windows/Doors.")
                return windows_doors
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    for i in range(num_windows_doors):
        print(f"Window/Door {i+1}")
        while True:
            try:
                shape = input(" Enter shape (square/circle/triangle/rectangle): ").lower()
                if shape not in ['square', 'circle', 'triangle', 'rectangle']:
                    raise ValueError("Invalid shape. Please enter 'square', 'circle', or 'triangle'.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        if shape == 'square':
            while True:
                try:
                    side_length = float(input("     Enter side length: "))
                    if side_length <= 0 or type(side_length) != float:
                        raise ValueError("Side length must be a positive number.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")
            dimensions = [side_length]
        elif shape == 'circle':
            while True:
                try:
                    radius = float(input("      Enter radius: "))
                    if radius <= 0 or type(radius) != float:
                        raise ValueError("Radius must be a positive number.")
                    break
                except ValueError as e:
                    print(f"Error: {e}")
            dimensions = [radius]
        elif shape == 'triangle':
            dimensions = get_dimensions()
        elif shape == 'rectangle':
            dimensions = get_dimensions()
        windows_doors.append((shape, dimensions))
    return windows_doors

# Testing

def test_paint_required(rooms=[], windows_doors=[]):
    if not rooms:
        print("No rooms entered. Settings Default Values of 2 Rooms, 4 Walls Each, 2 Windows/Doors Each")
        
        rooms = [
            [(5, 5)],  # Room 1: 4 walls
            [(10, 10)]   # Room 2: 4 walls
        ]

        windows_doors = [
            ('rectangle', [2, 5])     # Door: 2x6
        ]
    paint_type = 'premium'
    total_area = total_paint_area(rooms, windows_doors)
    total_volume = total_paint_volume(total_area, paint_type)

    cans_needed, total_cost = total_paint_cans(total_area, paint_type), total_paint_cost(total_area, paint_type)

    print(f'\nTotal Area to be Painted: {round(total_area, 2)} meter-squared')
    print(f'Coverage Rate: {paints[paint_type]["coverage_rate"]} meter-squared per can')
    print(f'Litres of Paint per Can: {paints[paint_type]["volume"]} Litres')
    print(f'Volume of Paint Required: {round(total_volume, 2)} Liters\n')

    print(f'Cans of Paint Required: {cans_needed}')
    print(f'Total Cost: £{total_cost}')

    #assert cans_needed == 2
    #assert total_cost == 100
    #assert total_area == 768

test_paint_required()

def print_welcome():
    print(f"""
        Hi, welcome to {store_name}!
        I'll help you calculate the amount of paint you need to buy.
        You will need to enter the dimensions of the rooms and windows/doors.
            You can enter as many rooms and windows/doors as you like.
            You can enter the dimensions in meters.
            You can enter the dimensions in decimal form.
        
            Let's get started!
        """)

def run_room_painter():
    print_welcome()
    rooms = get_rooms()
    windows_doors = get_windows_doors()
    paint_type = get_paint_type()

    total_area = total_paint_area(rooms, windows_doors)
    total_volume = total_paint_volume(total_area, paints[paint_type]['coverage_rate'])

    cans_needed, total_cost = total_paint_cans(total_area, paint_type), total_paint_cost(total_area, paint_type)

    print(f'\nTotal Area to be Painted: {round(total_area, 2)} meter-squared')
    print(f'Coverage Rate: {paints[paint_type]["coverage_rate"]} meter-squared per can')
    print(f'Litres of Paint per Can: {paints[paint_type]["volume"]} Liters')
    print(f'Volume of Paint Required: {round(total_volume, 2)} Liters\n')

    print(f'Cans of Paint Required: {cans_needed}')
    print(f'Total Cost: £{total_cost}')

run_room_painter()