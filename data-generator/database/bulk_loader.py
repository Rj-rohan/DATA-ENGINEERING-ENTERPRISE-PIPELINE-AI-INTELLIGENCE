from database.connection import get_connection


def _copy_records(table, columns, records):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            column_list = ", ".join(columns)
            with cursor.copy(f"COPY {table} ({column_list}) FROM STDIN") as copy:
                for row in records:
                    copy.write_row(row)

        conn.commit()


def load_customers(records):
    _copy_records(
        "customers",
        ("customer_id", "customer_name", "email", "region"),
        records,
    )


def load_suppliers(records):
    _copy_records(
        "suppliers",
        ("supplier_id", "supplier_name", "email", "region"),
        records,
    )


def load_products(records):
    _copy_records(
        "products",
        ("product_id", "product_name", "category", "price"),
        records,
    )


def load_warehouses(records):
    _copy_records(
        "warehouses",
        ("warehouse_id", "warehouse_name", "city", "region"),
        records,
    )


def load_orders(records):
    _copy_records(
        "orders",
        ("order_id", "customer_id", "order_date", "status", "total_amount"),
        records,
    )


def load_inventory(records):
    _copy_records(
        "inventory",
        ("inventory_id", "product_id", "warehouse_id", "quantity"),
        records,
    )


def load_shipments(records):
    _copy_records(
        "shipments",
        (
            "shipment_id",
            "order_id",
            "carrier",
            "tracking_number",
            "shipment_date",
            "status",
        ),
        records,
    )