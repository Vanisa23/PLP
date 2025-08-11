# Assignment 1: Design Your Own Class - Smartphone Example

# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Initialize parent attributes
        self.__storage = storage        # Encapsulation (private attribute)
        self.battery = battery

    # Method to display smartphone details
    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.__storage}GB | Battery: {self.battery}mAh"

    # Method to simulate taking a photo
    def take_photo(self):
        return f"{self.brand} {self.model} takes a photo 📸"

    # Getter for private attribute
    def get_storage(self):
        return self.__storage

    # Setter for private attribute
    def upgrade_storage(self, new_storage):
        if new_storage > self.__storage:
            self.__storage = new_storage
            return f"Storage upgraded to {self.__storage}GB."
        else:
            return "New storage must be larger than current storage."


# Another Child Class to show Polymorphism
class Smartwatch(Device):
    def device_info(self):
        return f"{self.brand} {self.model} (Smartwatch Edition) ⌚"


# Creating Objects
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 5000)
phone2 = Smartphone("Apple", "iPhone 15 Pro", 128, 4500)
watch1 = Smartwatch("Apple", "Watch Series 9")

# Testing Methods
print(phone1.phone_info())
print(phone1.take_photo())
print(phone1.upgrade_storage(512))
print(phone1.get_storage())

print(phone2.phone_info())
print(watch1.device_info())  # Polymorphism in action
