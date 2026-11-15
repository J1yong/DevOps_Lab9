import sys
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder / "im_sys"))
sys.path.insert(0, str(project_folder))


from im_sys.supplier import Supplier
from im_sys.productfactory import ProductFactory
from im_sys.order import order

print("========== SECTION 4: VALIDATION ==========")
supplier = Supplier("S001", "ABC Supplier", "abc@email.com")
product = ProductFactory.create("physical", "P001", "Desk Lamp", 10, 50.0, supplier, 2.0)
my_order = order("O001")

def expect_value_error(label, action):
    try:
        action()
    except ValueError as error:
        print(f"{label}: {error}")
    else:
        raise AssertionError(f"{label}: expected ValueError")

expect_value_error(
    "Invalid price",
    lambda: ProductFactory.create("physical", "P003", "Bad Price", 5, -10.0, supplier, 2.0)
)
expect_value_error(
    "Invalid stock",
    lambda: ProductFactory.create("digital", "D002", "Bad Stock", -5, 40.0, supplier, 500)
)
expect_value_error("Invalid order quantity", lambda: my_order.add_order_line(product, 0))
expect_value_error("Invalid stock update", lambda: product.updating_stock(-3))
print("SECTION 4: PASS")
