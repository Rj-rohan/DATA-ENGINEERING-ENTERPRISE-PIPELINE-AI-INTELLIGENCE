from generators.customers import generate_customers
from generators.inventory import generate_inventory
from generators.orders import generate_orders
from generators.products import generate_products
from generators.shipments import generate_shipments
from generators.suppliers import generate_suppliers
from generators.warehouses import generate_warehouses
from database.bulk_loader import (
    load_customers,
    load_inventory,
    load_orders,
    load_products,
    load_shipments,
    load_suppliers,
    load_warehouses,
)

CUSTOMER_COUNT = 100000
SUPPLIER_COUNT = 10000
PRODUCT_COUNT = 100000
WAREHOUSE_COUNT = 100
ORDER_COUNT = 100000
INVENTORY_COUNT = 100000
SHIPMENT_COUNT = 100000

def main():
    jobs = (
        ("customers", generate_customers(CUSTOMER_COUNT), load_customers),
        ("suppliers", generate_suppliers(SUPPLIER_COUNT), load_suppliers),
        ("products", generate_products(PRODUCT_COUNT), load_products),
        ("warehouses", generate_warehouses(WAREHOUSE_COUNT), load_warehouses),
        (
            "inventory",
            generate_inventory(
                INVENTORY_COUNT,
                product_count=PRODUCT_COUNT,
                warehouse_count=WAREHOUSE_COUNT,
            ),
            load_inventory,
        ),
        (
            "orders",
            generate_orders(ORDER_COUNT, customer_count=CUSTOMER_COUNT),
            load_orders,
        ),
        (
            "shipments",
            generate_shipments(SHIPMENT_COUNT, order_count=ORDER_COUNT),
            load_shipments,
        ),
    )

    for name, records, loader in jobs:
        print(f"Loading {name}...")
        loader(records)
        print(f"{name.capitalize()} loading completed.")

if __name__ == "__main__":
    main()