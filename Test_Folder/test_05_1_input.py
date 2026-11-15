import sys
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_folder / "im_sys"))
sys.path.insert(0, str(project_folder))

from unittest.mock import patch

print("========== SECTION 5.1: USER INPUT ==========")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

with patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
    price = get_positive_float("Enter price: ")

print("Valid price returned:", price)
assert price == 12.5
print("SECTION 5.1: PASS")
