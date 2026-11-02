from faker import Faker
import random

fake = Faker("en_IN")

REGIONS = ["North", "South", "East", "West", "Central"]

def generate_warehouses(count):

    for warehouse_id in range(1, count + 1):

        yield (
            warehouse_id,
            f"{fake.city()} Distribution Center",
            random.choice(REGIONS),
            random.randint(10000, 100000),
        )