from abc import ABC, abstractmethod
from typing import List

class Vehicle(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def move(self) -> str:
        pass

    def __str__(self):
        return self.name

class Car(Vehicle):
    def move(self) -> str:
        return f"{self.name}: Driving 🚗"

class Plane(Vehicle):
    def move(self) -> str:
        return f"{self.name}: Flying ✈️"

class Boat(Vehicle):
    def move(self) -> str:
        return f"{self.name}: Sailing ⛵"

class Bike(Vehicle):
    def move(self) -> str:
        return f"{self.name}: Pedaling 🚴"

def demo_fleet(fleet: List[Vehicle]):
    for v in fleet:
        print(v.move())

if __name__ == "__main__":
    fleet = [
        Car("Sedan"),
        Plane("Boeing 737"),
        Boat("Catamaran"),
        Bike("Mountain Bike"),
    ]
    demo_fleet(fleet)

