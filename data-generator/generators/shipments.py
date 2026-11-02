from datetime import datetime, timedelta, timezone
import random

STATUSES = [
    "Preparing",
    "In Transit",
    "Delivered",
    "Delayed"
]

def generate_shipments(
    count,
    order_count=100000,
    warehouse_count=50
):

    now = datetime.now(timezone.utc)

    for shipment_id in range(1, count + 1):

        status = random.choice(STATUSES)

        shipped_at = now - timedelta(days=random.randint(0, 30))

        delivered_at = (
            shipped_at + timedelta(days=random.randint(1, 7))
            if status == "Delivered"
            else None
        )

        yield (
            shipment_id,
            random.randint(1, order_count),
            random.randint(1, warehouse_count),
            status,
            shipped_at,
            delivered_at,
        )