class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        dic_item = {"name": name, "price": price}
        self.items.append(dic_item)


    def stock_price(self):
        # total = 0
        # for item in self.items:
        #     total += item["price"]
        # return total
        return sum([item["price"] for item in self.items])

store = Store("Starbuck")

print(store.add_item("mail", 25))
print(store.stock_price())