import random
from datetime import datetime, timezone

def generate_inventory(
    product_count=10000,
    warehouse_count=50
):

    inventory_id = 1

    for product_id in range(1, product_count + 1):

        for warehouse_id in range(1, warehouse_count + 1):

            available = random.randint(0, 1000)
            reserved = random.randint(0, min(available, 100))

            yield (
                product_id,
                warehouse_id,
                available,
                reserved,
                datetime.now(timezone.utc),
            )

            inventory_id += 1