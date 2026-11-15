import sys
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder / "im_sys"))
sys.path.insert(0, str(project_folder))

from im_sys.supplier import Supplier
from im_sys.productfactory import ProductFactory
from im_sys.order import order
from im_sys.discountstrategy import (
    NoDiscount,
    BulkDiscount,
    PercentageDiscount,
    StudentDiscount
)

print("========== SECTION 2: STRATEGY PATTERN ==========")
supplier = Supplier("S001", "ABC Supplier", "abc@email.com")
product = ProductFactory.create("physical", "P001", "Desk Lamp", 10, 50.0, supplier, 2.0)
my_order = order("O001", BulkDiscount(200, 20))
my_order.add_order_line(product, 5)

for name, strategy, expected in [
    ("BulkDiscount", BulkDiscount(200, 20), 230.0),
    ("PercentageDiscount", PercentageDiscount(10), 225.0),
    ("StudentDiscount", StudentDiscount(), 237.5),
    ("NoDiscount", NoDiscount(), 250.0),
]:
    my_order.set_discount(strategy)
    actual = my_order.calculate_total()
    print(f"{name}: {actual} (expected {expected})")
    assert actual == expected

shared = PercentageDiscount(10)
first = order("O002", shared)
second = order("O003", shared)
first.add_order_line(product, 2)
second.add_order_line(product, 3)
print("Shared strategy totals:", first.calculate_total(), second.calculate_total())
assert first.calculate_total() == 90.0
assert second.calculate_total() == 135.0
print("SECTION 2: PASS")
