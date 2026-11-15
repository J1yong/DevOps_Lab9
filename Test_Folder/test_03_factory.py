import sys
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder / "im_sys"))
sys.path.insert(0, str(project_folder))


from im_sys.supplier import Supplier
from im_sys.productfactory import ProductFactory

print("========== SECTION 3: FACTORY PATTERN ==========")
supplier = Supplier("S001", "ABC Supplier", "abc@email.com")
physical = ProductFactory.create("physical", "P002", "Chair", 5, 80.0, supplier, 3.0)
digital = ProductFactory.create("digital", "D001", "Software", 10, 40.0, supplier, 500)

print("Physical product:", type(physical).__name__)
print("Digital product:", type(digital).__name__)
assert type(physical).__name__ == "physical_product"
assert type(digital).__name__ == "digital_product"

try:
    ProductFactory.create("service", "S001", "Installation", 5, 30.0, supplier, 0)
except ValueError as error:
    print("Expected factory error:", error)
    assert "Unknown product type" in str(error)
else:
    raise AssertionError("Unknown product type was accepted")
print("SECTION 3: PASS")
