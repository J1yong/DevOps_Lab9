from product import Product
from physical_product import physical_product
from digital_product import digital_product
from supplier import Supplier


class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, stock: int,
               price: float, supplier: Supplier, extra_value: float) -> Product:
        if product_type == "physical":
            return physical_product(product_id, name, stock, price, supplier, extra_value)
        elif product_type == "digital":
            return digital_product(product_id, name, stock, price, supplier, extra_value)
        else:
            raise ValueError(f"Unknown product type: {product_type}")
