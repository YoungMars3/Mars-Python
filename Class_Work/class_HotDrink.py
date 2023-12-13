class HotDrink:
    def describe_type(self):
        print("Specify a drink")
    def describe_temp(self):
        print("Specify a drink")
class Coffee:
    def describe_type(self):
        print("Espresso")
    def describe_temp(self):
        print("Hot")
class Tea:
    def describe_type(self):
        print("Green Tea")
    def describe_temp(self):
        print("Warm")
class HotChocolate:
    def describe_type(self):
        print("Dark Chocolate")
    def describe_temp(self):
        print("Very Hot")

#Create instances and demonstrate polymorphism
coffee = Coffee()
tea = Tea()
hotchocolate = HotChocolate()

coffee.describe_type()
coffee.describe_temp()
tea.describe_type()
tea.describe_temp()
hotchocolate.describe_type()
hotchocolate.describe_temp()