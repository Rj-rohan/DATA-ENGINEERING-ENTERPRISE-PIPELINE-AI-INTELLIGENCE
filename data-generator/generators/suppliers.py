from faker import Faker

fake = Faker("en_IN")

def generate_suppliers(count):

    for supplier_id in range(1, count + 1):

        yield (
            supplier_id,
            fake.company(),
            fake.country(),
        )