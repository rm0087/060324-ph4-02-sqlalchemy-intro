#!/usr/bin/env python3

from config import app, db
# from models import MODELS GO HERE
from faker import Faker
from models import Candy, Vegetable
import random

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Candy.query.delete()
        Vegetable.query.delete()
        # MANUAL WAY
        # c1 = Candy(name="Reese's", brand="Hersheys", price=2)
        # c2 = Candy(name="Skittles", brand="Mars", price=3)
        # c3 = Candy(name="Snickers", brand="Mars", price=3)

        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        # END MANUAL WAY

        # THE LOOP WAY
        for _ in range(1000):
            new_candy = Candy(name=faker.name(), brand=faker.address(), price=random.choice(range(1, 6)))
            db.session.add(new_candy)

        for vegetable in range(1000):
            new_vegetable = Vegetable(name=faker.name(), is_tasty=random.choice(range(0,1)))
            db.session.add(new_vegetable)
        # END THE LOOP WAY
        
        
        db.session.commit()


        print("Seeding complete!")
