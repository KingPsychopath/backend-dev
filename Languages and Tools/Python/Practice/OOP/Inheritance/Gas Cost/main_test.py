from main import *

run_cases = [
    (Vehicle(100, 10), 100, 3.54, 35.4),
    (Truck(100, 10, 2000, 5.0), 100, 3.54, 55.4),
    (Car(100, 10, 2.0), 100, 3.54, 35.4),
]

submit_cases = run_cases + [
    (Vehicle(60, 5), 100, 3.54, 70.8),
    (Truck(80, 5, 2000, 4.0), 100, 3.54, 90.8),
    (Car(90, 4, 2.5), 100, 10, 250),
]


def test(vehicle, distance, price_per_liter, expected_cost):
    try:
        vehicle_type = vehicle.__class__.__name__
        print("---------------------------------")
        print(
            f"Testing {vehicle_type}: Max Speed {vehicle.max_speed_kph} kph, Efficiency {vehicle.kilometers_per_liter} km/l"
        )
        print(f"Distance: {distance} km, Price per Liter: {price_per_liter} per liter")
        print(f"Expected Trip Cost: {expected_cost}")
        actual_cost = vehicle.get_price_for_trip(distance, price_per_liter)
        print(f"Actual Trip Cost: {actual_cost}")
        if actual_cost == expected_cost:
            print("Pass")
            return True
        else:
            print("Fail")
            return False
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
