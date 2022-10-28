class Item:

    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"name = {self.name}, price = {self.price}, description = {self.description}, dimensions = {self.dimensions}"


class User:

    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"name = {self.name}, surname = {self.surname}, phone_number = {self.phone_number}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        tmp = ''
        for item, cnt in self.products.items():
            tmp += f'{str(item.name)}: {cnt} pcs. \n'
        return f'User: {self.user.name} {self.user.surname} \nItems \n{tmp} '

    def get_total(self):
        for key, cnt in self.products.items():
            self.total += key.price * cnt
        return self.total


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
orange = Item('orange',4,'orange','normal',)
buyer = User("Ivan", "Ivanov", "02628162")

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
cart.add_item(orange,5)
print(cart)
print(cart.get_total())  # 60