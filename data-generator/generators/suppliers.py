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


def generate_suppliers(count):

    for supplier_id in range(1, count + 1):

        yield (
            supplier_id,
            fake.company(),
            f"supplier{supplier_id}@example.com",
            random.choice(REGIONS)
        )