class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

car = Car("Toyota", "Corolla", 2020, "white")

print(car.brand)
print(car.model)
print(car.year)
print(car.color)

