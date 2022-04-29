class Product:
    def __init__(self):
        self.product_type = None
        self.product_name = None
        self.product_price = None

class ProductStore(Product):
    def __init__(self):
        Product.__init__(self)
        self.store = []
        self.income = 0

    def add_product(self, type, product, price, amount=1):
        self.product_type = type.title()
        self.product_name = product.title()
        self.product_price = round(price*1.3, 2)
        for item in self.store:
            if self.product_name in item.values():
                item['amount'] += amount
                return
        else:
            self.store.append(
                {'type': self.product_type,
                 'name': self.product_name,
                 'price': self.product_price,
                 'amount': amount})

    def set_discount(self, name, discount):
        for item in self.store:
            if name.title() in item.values():
                item['price'] = round(item['price'] * (100-int(discount))/100, 2)
                return
        else:
            raise KeyError('There no such product in store')

    def sell_product(self, name, amount=1):
        amount = int(amount)
        for item in self.store:
            if name.title() in item.values():
                if item['amount'] >= amount:
                    item['amount'] -= amount
                    self.income += item['price']*amount
                    if item['amount'] == 0:
                        self.store.pop(num)
                    return
                else:
                    raise ValueError('There are not enough goods')
        else:
            raise KeyError('There no such product in store')


    def get_income(self):
        return f'You have total {self.income} USD in your income'


    def get_all_products(self):
        some_str = 'Available products: \n==============\n'
        for item in self.store:
            for key, val in item.items():
                some_str += key.title() + ': ' + str(val).title() + '\n'
            some_str += '==============\n'
        return some_str


    def get_product_info(self, name):
        for item in self.store:
            if name.title() in item.values():
                return name.title(), item['price']
        else:
            raise KeyError('There are not enough goods')


pr = ProductStore()

pr.add_product('одяг', 'шкарпетки', 130)
pr.add_product('одяг', 'шкарпетки', 130, 5)
pr.add_product('одяг', 'джінси', 800)

print(pr.store)

pr.set_discount('джінси', 23)

print(pr.store)

pr.sell_product('шкарпетки', 5)

print(pr.store)

print(pr.get_income())

print(pr.get_all_products())

print(pr.get_product_info('джінси'))