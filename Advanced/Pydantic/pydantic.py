from __future__ import annotations

from datetime import datetime
from pathlib import Path
import sys
from typing import Literal

# Prevent this file name (pydantic.py) from shadowing the installed package.
CURRENT_DIR = Path(__file__).resolve().parent
sys.path = [p for p in sys.path if Path(p or ".").resolve() != CURRENT_DIR]

from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator


class Address(BaseModel):
	line1: str
	city: str
	postal_code: str
	country: str = "IN"

	@field_validator("postal_code")
	@classmethod
	def validate_postal_code(cls, value: str) -> str:
		cleaned = value.strip().replace(" ", "")
		if not cleaned.isdigit() or len(cleaned) not in (5, 6):
			raise ValueError("postal_code must have 5 or 6 digits")
		return cleaned


class OrderItem(BaseModel):
	sku: str
	quantity: int = Field(gt=0)
	unit_price: float = Field(gt=0)

	@property
	def line_total(self) -> float:
		return self.quantity * self.unit_price


class Customer(BaseModel):
	name: str = Field(min_length=2)
	email: str
	shipping_address: Address

	@field_validator("email")
	@classmethod
	def normalize_email(cls, value: str) -> str:
		value = value.strip().lower()
		if "@" not in value or value.startswith("@") or value.endswith("@"):
			raise ValueError("email must look like a valid address")
		return value


class Order(BaseModel):
	order_id: str
	created_at: datetime
	status: Literal["pending", "paid", "shipped"] = "pending"
	customer: Customer
	items: list[OrderItem]
	discount_percent: float = Field(default=0, ge=0, le=100)

	@model_validator(mode="after")
	def validate_order(self) -> Order:
		if not self.items:
			raise ValueError("order must contain at least one item")

		total_qty = sum(item.quantity for item in self.items)
		if total_qty > 100:
			raise ValueError("total quantity cannot exceed 100")
		return self

	@property
	def subtotal(self) -> float:
		return sum(item.line_total for item in self.items)

	@property
	def total(self) -> float:
		return round(self.subtotal * (1 - self.discount_percent / 100), 2)


def main() -> None:
	payload = {
		"order_id": "ORD-1001",
		"created_at": "2026-07-01T10:30:00",
		"status": "paid",
		"discount_percent": 10,
		"customer": {
			"name": "Bala",
			"email": "  BALA@EXAMPLE.COM  ",
			"shipping_address": {
				"line1": "12, MG Road",
				"city": "Bengaluru",
				"postal_code": "560 001",
			},
		},
		"items": [
			{"sku": "KB-100", "quantity": 2, "unit_price": 999.0},
			{"sku": "MS-300", "quantity": 1, "unit_price": 499.0},
		],
	}

	order = Order.model_validate(payload)

	print("Validated model:")
	print(order)
	print("\nComputed totals:")
	print(f"Subtotal: {order.subtotal}")
	print(f"Total after discount: {order.total}")

	print("\nSerialized dict:")
	print(order.model_dump())

	print("\nSerialized JSON:")
	print(order.model_dump_json(indent=2))

	print("\nValidation error example:")
	bad_payload = {
		**payload,
		"customer": {
			**payload["customer"],
			"shipping_address": {
				**payload["customer"]["shipping_address"],
				"postal_code": "12AB",
			},
		},
	}
	try:
		Order.model_validate(bad_payload)
	except ValidationError as exc:
		print(exc)


if __name__ == "__main__":
	main()
