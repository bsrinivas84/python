from contextlib import contextmanager

#The purpose of a context manager in Python is to manage setup and cleanup automatically around a block of code.
class FileManager:
	"""Class-based context manager for safe file handling."""

	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		self.file = None

	def __enter__(self):
		print("Opening file...")
		self.file = open(self.filename, self.mode, encoding="utf-8")
		return self.file

	def __exit__(self, exc_type, exc_value, traceback):
		print("Closing file...")
		if self.file:
			self.file.close()

		if exc_type:
			print(f"An error occurred: {exc_value}")

		# Return False so exceptions are not suppressed.
		return False


@contextmanager
def timer(label):
	"""Function-based context manager to measure execution time."""
	import time

	start = time.time()
	print(f"[{label}] Start")
	try:
		yield
	finally:
		end = time.time()
		print(f"[{label}] End - took {end - start:.4f} seconds")


if __name__ == "__main__":
	# Example 1: class-based context manager
	with FileManager("sample.txt", "w") as f:
		f.write("Hello from a class-based context manager!\n")

	# Example 2: function-based context manager
	with timer("Demo block"):
		total = sum(range(1_000_000))
		print("Total:", total)
