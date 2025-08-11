# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method.")


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"


# List of different vehicles (polymorphism in action)
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Loop through and call move() without knowing the specific class
for v in vehicles:
    print(v.move())
