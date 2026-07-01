from dataclasses import dataclass, field

#The purpose of a dataclass in Python is to make classes for storing data simpler and cleaner.
@dataclass
class Product:
	name: str
	price: float
	quantity: int = 1
	tags: list[str] = field(default_factory=list)
	total_value: float = field(init=False)

	def __post_init__(self):
		if self.price < 0:
			raise ValueError("price must be non-negative")
		if self.quantity < 0:
			raise ValueError("quantity must be non-negative")

		# Computed after initialization so it stays derived from input fields.
		self.total_value = self.price * self.quantity


if __name__ == "__main__":
	item = Product(name="Notebook", price=4.5, quantity=3, tags=["school", "paper"])
	print(item)
	print("Name:", item.name)
	print("Total value:", item.total_value)
