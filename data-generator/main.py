
from generators.customers import generate_customers
from generators.suppliers import generate_suppliers
from generators.products import generate_products
from generators.warehouses import generate_warehouses
from generators.orders import generate_orders
from generators.inventory import generate_inventory
from generators.shipments import generate_shipments

from database.bulk_loader import (
    load_customers,
    load_suppliers,
    load_products,
    load_warehouses,
    load_orders,
    load_inventory,
    load_shipments,
)

# --------------------------------------------------
# DATASET CONFIGURATION
# --------------------------------------------------

CUSTOMER_COUNT = 1000
SUPPLIER_COUNT = 100
PRODUCT_COUNT = 500
WAREHOUSE_COUNT = 10
ORDER_COUNT = 5000
SHIPMENT_COUNT = 4000


# --------------------------------------------------
# EXECUTION
# --------------------------------------------------

def execute_job(name, records, loader):

    print(f"\nStarting {name} generation and loading...")

    loader(records)

    print(f"Successfully loaded {name}.")


def main():

    print("====================================")
    print("SUPPLY CHAIN DATA GENERATION")
    print("====================================")

    jobs = [

        (
            "Customers",
            generate_customers(CUSTOMER_COUNT),
            load_customers,
        ),

        (
            "Suppliers",
            generate_suppliers(SUPPLIER_COUNT),
            load_suppliers,
        ),

        (
            "Warehouses",
            generate_warehouses(WAREHOUSE_COUNT),
            load_warehouses,
        ),

        (
            "Products",
            generate_products(
                PRODUCT_COUNT,
                supplier_count=SUPPLIER_COUNT,
            ),
            load_products,
        ),

        (
            "Orders",
            generate_orders(
                ORDER_COUNT,
                customer_count=CUSTOMER_COUNT,
            ),
            load_orders,
        ),

        (
            "Inventory",
            generate_inventory(
                product_count=PRODUCT_COUNT,
                warehouse_count=WAREHOUSE_COUNT,
            ),
            load_inventory,
        ),

        (
            "Shipments",
            generate_shipments(
                SHIPMENT_COUNT,
                order_count=ORDER_COUNT,
                warehouse_count=WAREHOUSE_COUNT,
            ),
            load_shipments,
        ),
    ]

    for name, records, loader in jobs:

        execute_job(name, records, loader)

    print("\n====================================")
    print("ALL DATASETS LOADED SUCCESSFULLY")
    print("====================================")


if __name__ == "__main__":
    main()
