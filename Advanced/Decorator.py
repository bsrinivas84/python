import time

#Decorators are used to add behavior to functions or classes without changing their original code.
def log_call(func):
	"""Function decorator: logs when a function starts and ends."""

	def wrapper(*args, **kwargs):
		print(f"[log] Calling {func.__name__}...")
		result = func(*args, **kwargs)
		print(f"[log] {func.__name__} finished.")
		return result

	return wrapper


class repeat:
	"""Class decorator: repeats a function call N times."""

	def __init__(self, times):
		self.times = times

	def __call__(self, func):
		def wrapper(*args, **kwargs):
			last_result = None
			for _ in range(self.times):
				last_result = func(*args, **kwargs)
			return last_result

		return wrapper


@log_call
def greet(name):
	print(f"Hello, {name}!")


@repeat(times=3)
def show_time():
	print("Current time:", time.strftime("%H:%M:%S"))


if __name__ == "__main__":
	greet("Alice")
	show_time()
