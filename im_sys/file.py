import json
from inventory import Inventory
from productfactory import ProductFactory
from supplier import Supplier


FILE = "inventory.json"


def load_json(inventory: Inventory) -> None:
    try:
        with open(FILE, "r", encoding="utf-8") as source:
            data = json.load(source)
    except FileNotFoundError:
        print(f"No existing inventory file found: {FILE}")
        return
    except json.JSONDecodeError:
        print(f"Inventory file is not valid JSON: {FILE}")
        return

    if not isinstance(data, list):
        print("Inventory file should contain a list of products.")
        return

    loaded = 0
    for row_number, item in enumerate(data, start=1):
        try:
            product_type = item["type"]
            product_id = str(item["[Product] id"])
            name = str(item["[Product] name"])
            stock = int(item["[Product] stock"])
            price = float(item["[Product] price"])
            supply = Supplier(
                str(item["[Supplier] id"]),
                str(item["[Supplier] name"]),
                str(item["[Supplier] email"]),
            )
            if product_type == "physical":
                extra_value = float(item["[Product] weight"])
            elif product_type == "digital":
                extra_value = int(item["[Product] digital_size"])
            else:
                # Pass unknown types to the Factory so it raises ValueError.
                extra_value = 0

            product = ProductFactory.create(
                product_type, product_id, name, stock, price, supply, extra_value
            )
            inventory.add_product(product)
            loaded += 1
        except (ValueError, TypeError, KeyError) as error:
            print(f"Skipping invalid saved product on row {row_number}: {error}")

    print(f"{loaded} products loaded from JSON.")


def save_json(inventory: Inventory) -> None:
    dictdata = []
    for product in inventory.get_all_products():
        dictdata.append(product.to_dictionary())
    with open(FILE, "w", encoding="utf-8") as target:
        json.dump(dictdata, target, indent=4)
