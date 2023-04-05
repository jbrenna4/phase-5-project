from faker import Faker
from random import randint
from datetime import datetime

import random
from app import app
from models import db, Customer, Shop, Worker, Reservation
from faker import Faker

if __name__ == '__main__':
    f = Faker()
    with app.app_context():
        print('Deleting Data...')
        Customer.query.delete()
        Shop.query.delete()
        Worker.query.delete()
        Reservation.query.delete()


    # Add Shops
        shop = Shop(
            img = 'https://www.sbsun.com/wp-content/uploads/2021/12/SBS-L-VILLAGE-1210-03-WL.jpg?w=1024',
            neighborhood = 'Park Slope',
            address = '425 7th Avenue',
            created_at = datetime(2023, 1, 1)
        )
        db.session.add(shop)

        shop = Shop(
            img = 'https://www.scandi.travel/wp-content/uploads/2018/12/santa.jpg',
            neighborhood = 'Crown Heights',
            address = '550 Nostrand Avenue',
            created_at = datetime(2023, 1, 1)
        )
        db.session.add(shop)     

        shop = Shop(
            img = 'https://media.tacdn.com/media/attractions-splice-spp-674x446/06/fb/9f/4c.jpg',
            neighborhood = 'Bay Ridge',
            address = '860 12th Avenue',
            created_at = datetime(2023, 1, 1)
        )
        db.session.add(shop)

        # Add Workers
        santas = ['Santa Claus', 'Kris Kringle', 'Father Christmas', 'Pere Noel', 'Ded Moroz', 'Babbo Natale']
        for name in santas:
            worker = Worker(
                name = name,
                role = 'santa',
                shop_id = random.randint(1, 3),
                created_at = datetime(2023, 1, 1),
                phone_number = f.phone_number()
            )
            db.session.add(worker)

        elfs = ['Buddy', 'Jingles', 'Sparkles', 'Twinkle', 'Sugarplum', 'Peppermint', 'Candy Cane', 'Gingerbread', 'Tinsel', 'Mistletoe', 'Holly', 'Ivy', 'Snowflake', 'Frosty', 'Rudolph']
        for name in elfs:
            worker = Worker(
                name = name,
                role = 'elf',
                shop_id = random.randint(1, 3),
                created_at = datetime(2023, 1, 1),
                phone_number = f.phone_number()
            )
            db.session.add(worker)

        # Add Customers and Reservations
        for i in range(1, 61):
            customer = Customer(
                name = f.name(),
                email = f.email(),
                created_at = datetime(2023, 1, 1),
                password = 'password',
                phone_number = f.phone_number()
            )
            db.session.add(customer)
            db.session.commit()

            reservation = Reservation(
                customer_id = i,
                shop_id = random.randint(1, 3),
                scheduled_time = datetime(2023, 12, random.choice(range(1, 23)), random.choice(range(9, 17))),
                created_at = datetime(2023, 1, 1)
            )
            db.session.add(reservation)

        db.session.commit()

print('Database seeding completed successfully.')
