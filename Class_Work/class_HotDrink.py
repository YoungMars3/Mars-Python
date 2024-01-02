class HotDrink:
    def __init__(self, temperature):
        self.temperature = temperature

    def describe(self):
        return 0

class Coffee(HotDrink):
    def __init__(self, coffee_type, temperature):
        super().__init__(temperature)
        self.coffee_type = coffee_type

    def describe(self):
        return f"Coffee - Type: {self.coffee_type}, Temperature: {self.temperature}"

class Tea(HotDrink):
    def __init__(self, tea_type, temperature):
        super().__init__(temperature)
        self.tea_type = tea_type

    def describe(self):
        return f"Tea - Type: {self.tea_type}, Temperature: {self.temperature}"

class HotChocolate(HotDrink):
    def __init__(self, chocolate_type, temperature):
        super().__init__(temperature)
        self.chocolate_type = chocolate_type

    def describe(self):
        return f"Hot Chocolate - Type: {self.chocolate_type}, Temperature: {self.temperature}"

#Creating instances
espresso = Coffee("Espresso", "Hot")
green_tea = Tea("Green Tea", "Warm")
dark_chocolate = HotChocolate("Dark Chocolate", "Very Hot")

#Accessing methods
print(espresso.describe())
print(green_tea.describe())
print(dark_chocolate.describe())