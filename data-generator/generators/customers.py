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

def generate_customers(count):

    for customer_id in range(1, count + 1):

        yield (
            customer_id,
            fake.name(),
            f"customer{customer_id}@example.com",
            random.choice(REGIONS)
        )