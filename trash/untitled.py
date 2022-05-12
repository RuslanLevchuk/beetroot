import functools
import time

def timer(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		t1 = time.perf_counter()
		f = func(*args, **kwargs)
		t2 = time.perf_counter()
		print(f"Час виконання функції {t2 - t1}")
		return f
	return wrapper

@timer
def waster (N):
	for i in range (N):
		for j in range(N):
			for z in range(N):
				#print(z, j, i)
				pass



waster(10)
waster(100)
waster(1000)
waster(10000)

