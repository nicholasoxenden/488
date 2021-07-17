### Basic Instantiation
class Complex():
    def __init__(self,name,address,rating):
        self.name = name
        self.address = address
        self.rating = rating
    def __str__(self):
        print(self.name)

complex_objects = {}

failed_complexes = []
