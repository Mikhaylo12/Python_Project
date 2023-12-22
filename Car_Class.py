import random

class Car:
    def __init__(self, model, color, economy):
        self.mileage = 0
        self.fuel = 100
        self.model = model
        self.color = color
        self.economy = economy

    def drive(self, distance):
        fuel_needed = distance / 100 * self.economy
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            self.mileage += distance
        else:
            print(f"Not enough fuel to drive {distance} km!")

    def distance_left(self):
        return (self.fuel / self.economy) * 100

    def fuel_up(self):
        self.fuel += 20

# Створюємо пустий список cars
cars = []

# Список доступних моделей
models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]

# Заповнюємо список cars 10 машинами
for _ in range(10):
    model = random.choice(models)
    color = random.choice(["Red", "Blue", "Green", "Silver", "Black"])
    economy = random.randint(5, 15)  # Рандомні значення витрат пального на 100 км
    car = Car(model, color, economy)
    cars.append(car)

# Кожна машина в cars: проїжджає 200 км, дозаправляється, проїжджає ще 100 км
for car in cars:
    car.drive(200)
    car.fuel_up()
    car.drive(100)

# Знаходимо машину з найбільшим залишком пального
car_with_most_fuel = max(cars, key=lambda car: car.fuel)

# Виводимо опис машини з найбільшим залишком пального
print(f"Car with the most fuel left: Model - {car_with_most_fuel.model}, Color - {car_with_most_fuel.color}, Mileage - {car_with_most_fuel.mileage} km, Fuel Left - {car_with_most_fuel.fuel} liters")