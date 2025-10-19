from abc import ABC, abstractmethod
from typing import List

class Device(ABC):
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self._battery_health = 100

    @property
    def battery_health(self) -> int:
        return self._battery_health

    @battery_health.setter
    def battery_health(self, value: int):
        if not (0 <= value <= 100):
            raise ValueError("Battery health must be between 0 and 100.")
        self._battery_health = value

    @abstractmethod
    def specs(self) -> str:
        pass

    def __str__(self):
        return f"{self.brand} {self.model} (Battery health: {self.battery_health}%)"


class Smartphone(Device):
    def __init__(self, brand: str, model: str, os: str):
        super().__init__(brand, model)
        self.os = os
        self.installed_apps: List[str] = []

    def specs(self) -> str:
        return f"{self.brand} {self.model} running {self.os}, {len(self.installed_apps)} apps installed."

    def drain_battery(self, amount: int):
        self.battery_health = max(0, self.battery_health - amount)

    def charge(self, amount: int):
        self.battery_health = min(100, self.battery_health + amount)

    def install_app(self, name: str):
        if name not in self.installed_apps:
            self.installed_apps.append(name)

    def uninstall_app(self, name: str):
        if name in self.installed_apps:
            self.installed_apps.remove(name)

    def call(self, number: str) -> str:
        if self.battery_health == 0:
            return "Battery dead. Please charge."
        self.drain_battery(1)
        return f"Calling {number} from {self.brand} {self.model}..."

if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "S24", "Android 14")
    phone2 = Smartphone("Apple", "iPhone 15", "iOS 18")
    phone1.install_app("WhatsApp"); phone1.install_app("Spotify")
    phone2.install_app("iMessage")
    print(phone1)
    print(phone1.specs())
    print(phone1.call("+254700000000"))
    phone1.drain_battery(50); print("Battery after drain:", phone1.battery_health)
    phone1.charge(30); print("Battery after charge:", phone1.battery_health)
    print(phone2.specs())
