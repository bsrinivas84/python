from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, Protocol, TypeVar


# Type variables used by generic functions and classes.
T = TypeVar("T")
U = TypeVar("U")


def first_item(items: list[T]) -> T:
	"""Return the first item from a typed list."""
	return items[0]


class Box(Generic[T]):
	"""Generic class that stores one value of any type."""

	def __init__(self, value: T):
		self.value = value

	def get(self) -> T:
		return self.value


def apply_twice(func: Callable[[T], U], value: T) -> tuple[U, U]:
	"""Call a typed function twice with the same input value."""
	return func(value), func(value)


class Describable(Protocol):
	"""Structural type: any object with describe() -> str matches."""

	def describe(self) -> str:
		...


def show_description(item: Describable) -> str:
	return item.describe()


@dataclass
class User:
	name: str

	def describe(self) -> str:
		return f"User(name={self.name})"


@dataclass
class Product:
	sku: str

	def describe(self) -> str:
		return f"Product(sku={self.sku})"


def main() -> None:
	# Generic function + TypeVar
	print("first_item(ints):", first_item([10, 20, 30]))
	print("first_item(strings):", first_item(["a", "b", "c"]))

	# Generic class
	int_box = Box[int](42)
	str_box = Box[str]("hello")
	print("int_box:", int_box.get())
	print("str_box:", str_box.get())

	# Callable
	square: Callable[[int], int] = lambda x: x * x
	print("apply_twice(square, 5):", apply_twice(square, 5))

	# Protocol (duck typing with static type support)
	user = User("Bala")
	product = Product("KB-100")
	print(show_description(user))
	print(show_description(product))


if __name__ == "__main__":
	main()
