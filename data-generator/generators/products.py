from faker import Faker
import random

fake = Faker()

CATEGORIES = [
    "Electronics",
    "Furniture",
    "Clothing",
    "Food",
    "Hardware"
]


def generate_products(count):

    for product_id in range(1, count + 1):

        yield (
            product_id,
            fake.word().title(),
            random.choice(CATEGORIES),
            round(random.uniform(5, 1000), 2)
        )