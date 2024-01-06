class Hot Drink:
    def ＿init＿(self, name, temperature):
        self.name = name
        self.temperature = temperature

def info(self):
    return f"{self.name} is a hot drink served at {self.temperature}°C"

class Coffee(Hot Drink):
    def ＿init＿(self, name, temperature, caffeine_level):
        super().＿init＿(name, temperature)
        self.caffeine_level = caffeine_level

def boost(self):
    return f"{self.name} gives you a caffeine boost of level {self.caffeine_level}"

class Tea(Hot Drink):
    def ＿init＿(self, name, temperature, type):
        super().＿init＿(name,temperature)
        self.type = type

def variety(self):
    return f"{self.name} is a type of {self.type} tea"

# Creating instances
coffee = Coffee("Coffee", 85, "High")
tea = Tea("Tea", 70, "Green")

# Accessing methods
print( coffee.info ())

# Output: Coffee is a hot drink served at 85°C
print(coffee.boost())

# Output: Coffee gives you a caffeine boost of level
High
print( tea.info ())
print(tea.variety())
# Output: Tea is a hot drink served at 70°C
#
Output:
Tea is a type of Green tea