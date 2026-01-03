class FoodItem:
    def __init__(self, name, price, rating, is_veg):
        self.name = name
        self.price = price
        self.rating = rating
        self.is_veg = is_veg

class DeliveryAgent:
    def __init__(self, name, rating, ph_no):
        self.name = name
        self.rating = rating
        self.ph_no = ph_no

class Restaurant:
    def __init__(self, name, addr, rating):
        self.name = name
        self.addr = addr
        self.rating = rating
        self.pizza = FoodItem('Pizza', 500, 4.5, False)
    def assign_delivery_agent(self, agent):
        self.agent = agent
        