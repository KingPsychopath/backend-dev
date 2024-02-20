# Gas Cost

A local car dealership has been advertising the average gas cost for a trip, and how much cargo their cars can stow. They have noticed that this has increased their sales _dramatically_.

They have been doing these calculations by hand, but have asked if you will write them a program that will automate it.

## Challenge

Complete the `Vehicle`, `Car`, and `Truck` classes.

### Vehicle class

#### Constructor

Accepts two parameters (in order) and sets them as instance variables:

- `max_speed_kph`
- `kilometers_per_liter`

#### `get_price_for_trip()`

The formula for calculating the cost of gas for a trip is:

`distance / rate_of_consumption * price`

#### `get_cargo_cap_meters_cubed()`

This method should be left empty. You can use the [pass](https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement) keyword. This will be overridden by child classes.

### Truck class

#### Constructor

Calls the parent constructor, then sets the additional truck-specific instance variables as member variables.

#### `get_price_for_trip()`

Uses the parent method to calculate the cost of gas for a trip, but adds an additional cost to account for the load weight.

The formula for calculating the cost of gas for a trip is:

`base_vehicle_cost + (load_weight_kilos * 0.01)`

#### `get_cargo_cap_meters_cubed()`

Returns the cargo capacity of the truck in meters cubed. A truck's bed is 2 meters deep. Return the volume of the truck's bed by multiplying the area of the bed by its depth.

### Car class

#### Constructor

Calls the parent constructor, then sets the additional car-specific instance variable as a member variable.

#### `get_price_for_trip`

The car class does not need to override this method.

#### `get_cargo_cap_meters_cubed()`

Returns the cargo capacity of the car, which was set in the constructor. No fancy calculations needed here.