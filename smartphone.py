
class Smartphone:
    def __init__(self, brand, model, battery_percentage):
       
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    def charge(self):
        """Simulate charging the smartphone"""
        if self.battery_percentage < 100:
            self.battery_percentage += 10
            if self.battery_percentage > 100:
                self.battery_percentage = 100
            print(f"The {self.model} is charging. Battery is now at {self.battery_percentage}%.")
        else:
            print(f"The {self.model} is fully charged.")

    def use(self):
        """Simulate using the smartphone"""
        if self.battery_percentage > 0:
            self.battery_percentage -= 5
            print(f"Using {self.model}. Battery is now at {self.battery_percentage}%.")
        else:
            print(f"{self.model} needs charging!")

phone = Smartphone("Apple", "iPhone 14", 50)


phone.use()
phone.charge()
