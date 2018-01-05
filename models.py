class Location:
    def __init__(self, x, y):
        self.lat = float(x)
        self.lng = float(y)


class Parking:
    def __init__(self, x, y):
        self.location = Location(x, y)
        self.taken = False

    def resereve(self):
        self.taken = True


class User:
    def __init__(self, x, y, radius):
        self.location = Location(x, y)
        self.radius = float(radius)
