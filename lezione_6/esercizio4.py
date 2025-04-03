class Food:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class Menu:
    def __init__(self, foods=None):
        if foods is None:
            foods = []
        self.foods = foods

    def addFood(self, food):
        self.foods.append(food)

    def removeFood(self, food_name):
        self.foods = [food for food in self.foods if food.name != food_name]

    def printPrices(self):
        for food in self.foods:
            print(f"{food.name}: ${food.price}")

    def getAveragePrice(self):
        if not self.foods:
            return 0  
        total_price = sum(food.price for food in self.foods)
        return total_price / len(self.foods)

pizza = Food("Pizza", 12.99, "A cheesy, delicious pizza with tomato sauce and toppings.")
burger = Food("Burger", 8.49, "A beef burger with lettuce, tomato, and cheese.")
pasta = Food("Pasta", 10.99, "A plate of spaghetti with marinara sauce and parmesan.")
salad = Food("Salad", 6.99, "A healthy bowl of mixed greens with a vinaigrette dressing.")
sushi = Food("Sushi", 14.99, "Fresh sushi rolls with tuna, salmon, and avocado.")

menu = Menu()

menu.addFood(pizza)
menu.addFood(burger)
menu.addFood(pasta)
menu.addFood(salad)
menu.addFood(sushi)

menu.printPrices()

average_price = menu.getAveragePrice()
print(f"Average Price: ${average_price:.2f}")
