class GreatNumerator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        if self.n > len(self.lst):
            raise StopIteration
        return f"{self.n - 1} {self.lst[self.n - 1]}"


lists = ['111', 'cat', 'got', 'ddd', '222']
t = GreatNumerator(lists)
for i in t:
    print(i)

# Я набрив в мереж сспосіб задання ітератора і його толчків в одному класі, дандер ітератора повертає сам об'єкт
# а потім працює дандер некст
# ми розглядали варіант з двома класами, чи прийнятний мій спосіб?
