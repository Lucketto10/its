class Restaurant:
   
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type  

    def describe_restaurant(self):
        print(f"The name is {self.restaurant_name}")
        print(f"The cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open")

r1 = Restaurant("Indian Spice", "Indian")
r2 = Restaurant("Pasta Heaven", "Italian")
r3 = Restaurant("Sushi World", "Japanese")

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()
