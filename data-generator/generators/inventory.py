import random


def generate_inventory(count, product_count=100000, warehouse_count=100):

    for inventory_id in range(1, count + 1):

        yield (
            inventory_id,
            random.randint(1, product_count),
            random.randint(1, warehouse_count),
            random.randint(0, 10000)
        )