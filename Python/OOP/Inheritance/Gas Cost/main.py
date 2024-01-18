class Vehicle:
    def __init__(self, max_speed_kph, kilometers_per_liter):
        self.max_speed_kph = max_speed_kph
        self.kilometers_per_liter = kilometers_per_liter

    def get_price_for_trip(self, distance_kilometers, price_per_liter):
        return (distance_kilometers / self.kilometers_per_liter) * price_per_liter

    def get_cargo_cap_meters_cubed(self):
        pass


class Truck(Vehicle):
    def __init__(
        self,
        max_speed_kph,
        kilometers_per_liter,
        load_weight_kilos,
        bed_area_meters_squared,
    ):
        super().__init__(max_speed_kph, kilometers_per_liter)
        self.__load_weight_kilos = load_weight_kilos
        self.__bed_area_meters_squared = bed_area_meters_squared
        self.__bed_depth = 2
        
    def get_price_for_trip(self, distance_kilometers, price_per_liter):
        return super().get_price_for_trip(distance_kilometers, price_per_liter) + (self.__load_weight_kilos * 0.01) 

    def get_cargo_cap_meters_cubed(self):
        return self.bed_area_meters_squared * self.__bed_depth


class Car(Vehicle):
    def __init__(self, max_speed_kph, kilometers_per_liter, cargo_cap_meters_cubed):
        super().__init__(max_speed_kph, kilometers_per_liter)
        self.__cargo_cap_meters_cubed = cargo_cap_meters_cubed

    def get_cargo_cap_meters_cubed(self):
        return __cargo_cap_meters_cubed
