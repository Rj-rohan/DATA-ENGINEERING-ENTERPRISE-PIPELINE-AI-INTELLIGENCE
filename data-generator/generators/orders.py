from datetime import datetime, timedelta, timezone
import random

STATUSES = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled"
]

def generate_orders(count, customer_count=100000):

    now = datetime.now(timezone.utc)

    for order_id in range(1, count + 1):

        yield (
            order_id,
            random.randint(1, customer_count),
            random.choice(STATUSES),
            now - timedelta(days=random.randint(0, 365)),
            now,
        )