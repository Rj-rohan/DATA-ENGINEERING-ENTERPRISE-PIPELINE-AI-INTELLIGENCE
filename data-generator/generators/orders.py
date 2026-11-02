from datetime import datetime, timedelta
from faker import Faker
import random

fake = Faker()

STATUSES = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled"
]


def generate_orders(count, customer_count=100000):

    for order_id in range(1, count + 1):

        yield (
            order_id,
            random.randint(1, customer_count),
            datetime.now() - timedelta(days=random.randint(0, 365)),
            random.choice(STATUSES),
            round(random.uniform(10, 5000), 2)
        )