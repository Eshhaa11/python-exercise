class Car:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

car = Car("Toyota", 2025, "white")


print(car.brand)
print(car.year)
print(car.color)


car.year = 2028
print(car.year)

