from datetime import date, timedelta
from faker import Faker
import random

fake = Faker()

STATUSES = [
    "Preparing",
    "In Transit",
    "Delivered",
    "Delayed"
]


def generate_shipments(count, order_count=100000):

    for shipment_id in range(1, count + 1):

        yield (
            shipment_id,
            random.randint(1, order_count),
            fake.company(),
            f"TRK-{shipment_id:010d}",
            date.today() + timedelta(days=random.randint(0, 30)),
            random.choice(STATUSES)
        )