class vehicle:
    def move(self):
        print("The vehicle is moving")

class car (vehicle):
     def move(self):
         print("Drivingnon the road")

class bicycle (vehicle):
    def move(self):
        print("pedaling on the road")

# demonstrating polymorphism
vehicles = [car(), bicycle()]

for v in vehicles:
    v.move()


