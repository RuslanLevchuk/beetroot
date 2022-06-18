class myObj:
  def func(self):
      pass

y = myObj()

c = y.func


x = hasattr(y.func, '__call__')

print(x)