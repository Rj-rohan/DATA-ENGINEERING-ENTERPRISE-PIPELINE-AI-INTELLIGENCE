from faker import Faker
import random

fake = Faker("en_IN")

CATEGORIES = [
    "Electronics",
    "Furniture",
    "Clothing",
    "Food",
    "Hardware"
]

def generate_products(count, supplier_count=2000):

    for product_id in range(1, count + 1):

        yield (
            product_id,
            fake.word().title(),
            random.choice(CATEGORIES),
            round(random.uniform(5, 1000), 2),
            random.randint(1, supplier_count),
        )