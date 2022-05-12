class ProductStore:
    def __init__(self):
        self.store = []
        self.income = 0
pr = ProductStore()

pr.income = 123

print(pr.income)
print(pr.store)