class Smartphone:
    def __init__(self, model, brand, price, storage_capacity):
        self.model = model
        self.brand = brand
        self.price = price
        self.storage_capacity = storage_capacity

class SmartphoneRetailer:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.smartphones_inventory = []

    def add_smartphone(self, model, brand, price, storage_capacity):
        smartphone = Smartphone(model, brand, price, storage_capacity)
        self.smartphones_inventory.append(smartphone)

   
