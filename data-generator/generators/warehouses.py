from faker import Faker
import random

fake = Faker()

REGIONS = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]


def generate_warehouses(count):

    for warehouse_id in range(1, count + 1):

        yield (
            warehouse_id,
            fake.company() + " Warehouse",
            fake.city(),
            random.choice(REGIONS)
        )