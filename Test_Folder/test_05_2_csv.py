import sys
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder / "im_sys"))
sys.path.insert(0, str(project_folder))


import csv
from im_sys.inventory import Inventory
from im_sys.supplier import Supplier
from im_sys.productfactory import ProductFactory

print("========== SECTION 5.2: CSV LOADING ==========")

def load_products(path, inventory, supplier):
    try:
        with open(path, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            loaded = 0
            for row_number, row in enumerate(reader, start=2):
                try:
                    if len(row) != 5:
                        raise ValueError("Expected 5 CSV columns")
                    product_type, product_id, name, price, stock = row
                    extra_value = 0
                    product = ProductFactory.create(
                        product_type, product_id, name,
                        int(stock), float(price), supplier, extra_value
                    )
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as error:
                    product_id = row[1] if len(row) > 1 else "unknown"
                    print(f"Skipping invalid row {row_number} ({product_id}): {error}")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")

supplier = Supplier("S001", "ABC Supplier", "abc@email.com")
inventory = Inventory()
csv_path = Path(__file__).resolve().parent / "products.csv"
load_products(str(csv_path), inventory, supplier)
print("Products in inventory:", len(inventory.get_all_products()))
assert len(inventory.get_all_products()) == 3

print("\nTesting missing CSV file:")
missing_path = csv_path.parent / "missing_products.csv"
# Do not delete or overwrite any user's files to simulate a missing file.
assert not missing_path.exists(), "Please rename existing missing_products.csv before this test."
missing_inventory = Inventory()
load_products(str(missing_path), missing_inventory, supplier)
assert len(missing_inventory.get_all_products()) == 0
print("SECTION 5.2: PASS")
