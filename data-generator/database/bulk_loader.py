
from database.connection import get_connection


def _copy_records(table, columns, records):
    """
    Bulk-load records into PostgreSQL using COPY.
    """

    with get_connection() as conn:
        with conn.cursor() as cursor:

            column_list = ", ".join(columns)

            query = f"""
                COPY {table} ({column_list})
                FROM STDIN
            """

            with cursor.copy(query) as copy:
                for row in records:
                    copy.write_row(row)

        conn.commit()


# --------------------------------------------------
# CUSTOMERS
# --------------------------------------------------

def load_customers(records):
    _copy_records(
        "customers",
        (
            "customer_id",
            "customer_name",
            "email",
            "region",
        ),
        records,
    )


# --------------------------------------------------
# SUPPLIERS
# --------------------------------------------------

def load_suppliers(records):
    _copy_records(
        "suppliers",
        (
            "supplier_id",
            "supplier_name",
            "country",
        ),
        records,
    )


# --------------------------------------------------
# WAREHOUSES
# --------------------------------------------------

def load_warehouses(records):
    _copy_records(
        "warehouses",
        (
            "warehouse_id",
            "warehouse_name",
            "region",
            "capacity",
        ),
        records,
    )


# --------------------------------------------------
# PRODUCTS
# --------------------------------------------------

def load_products(records):
    _copy_records(
        "products",
        (
            "product_id",
            "product_name",
            "category",
            "price",
            "supplier_id",
        ),
        records,
    )


# --------------------------------------------------
# ORDERS
# --------------------------------------------------

def load_orders(records):
    _copy_records(
        "orders",
        (
            "order_id",
            "customer_id",
            "order_status",
            "order_date",
            "updated_at",
        ),
        records,
    )


# --------------------------------------------------
# ORDER ITEMS
# --------------------------------------------------

def load_order_items(records):
    _copy_records(
        "order_items",
        (
            "order_item_id",
            "order_id",
            "product_id",
            "quantity",
            "unit_price",
        ),
        records,
    )


# --------------------------------------------------
# INVENTORY
# --------------------------------------------------

def load_inventory(records):
    _copy_records(
        "inventory",
        (
            "product_id",
            "warehouse_id",
            "available_quantity",
            "reserved_quantity",
            "last_updated",
        ),
        records,
    )


# --------------------------------------------------
# INVENTORY TRANSACTIONS
# --------------------------------------------------

def load_inventory_transactions(records):
    _copy_records(
        "inventory_transactions",
        (
            "transaction_id",
            "product_id",
            "warehouse_id",
            "transaction_type",
            "quantity_change",
            "reference_id",
            "created_at",
        ),
        records,
    )


# --------------------------------------------------
# SHIPMENTS
# --------------------------------------------------

def load_shipments(records):
    _copy_records(
        "shipments",
        (
            "shipment_id",
            "order_id",
            "warehouse_id",
            "shipment_status",
            "shipped_at",
            "delivered_at",
        ),
        records,
    )


# --------------------------------------------------
# SHIPMENT EVENTS
# --------------------------------------------------

def load_shipment_events(records):
    _copy_records(
        "shipment_events",
        (
            "event_id",
            "shipment_id",
            "event_type",
            "location",
            "event_timestamp",
        ),
        records,
    )
