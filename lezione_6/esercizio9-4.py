class Restaurant:
   
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type  
        self.number_served = 0  

    def describe_restaurant(self):
        print(f"The name is {self.restaurant_name}")
        print(f"The cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open")
    
    def describe_number_served(self):
        print(f"The restaurant has served {self.number_served} customers.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("Restaurant from your class", "Indian")

restaurant.describe_number_served()

restaurant.number_served = 50
restaurant.describe_number_served()

restaurant.set_number_served(100)
restaurant.describe_number_served()

restaurant.increment_number_served(25)
restaurant.describe_number_served()
