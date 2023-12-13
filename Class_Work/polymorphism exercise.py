class HotDrink:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

class Coffee(HotDrink):
    def __init__(self, name, temperature, coffee_type):
        super().__init__(name, temperature)
        self.coffee_type = coffee_type

    def describe(self):
        print(f"{self.name} is a {self.temperature} degree {self.coffee_type} coffee.")

class Tea(HotDrink):
    def __init__(self, name, temperature, tea_type):
        super().__init__(name, temperature)
        self.tea_type = tea_type

    def describe(self):
        print(f"{self.name} is a {self.temperature} degree {self.tea_type} tea.")

class HotChocolate(HotDrink):
    def __init__(self, name, temperature, chocolate_type):
        super().__init__(name, temperature)
        self.chocolate_type = chocolate_type

    def describe(self):
        print(f"{self.name} is a {self.temperature} degree {self.chocolate_type} hot chocolate.")

#create the instances
coffee = Coffee("Espresso", "hot", "milk")
tea = Tea("Green Tea", "hot", "black")
hot_chocolate = HotChocolate("Dark Chocolate", "hot", "dark")

coffee.describe()  # Output: Espresso is a hot milk coffee.
tea.describe()  # Output: Green Tea is a hot black tea.
hot_chocolate.describe()  # Output: Dark Chocolate is a hot degree dark hot chocolate.
