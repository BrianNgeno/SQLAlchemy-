import random
from faker import Faker
fake = Faker()

print("Seeding cars data ...")

cars = [
    Car(
        name=fake.name(),
        chasis=random.randint(1000, 9800)
    )
for i in range(50)]

session.bulk_save_objects(cars)
session.commit()