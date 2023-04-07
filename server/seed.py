from faker import Faker
from random import randint
from datetime import datetime

import random
from app import app
from models import db, User, Shop, Worker, Reservation
from faker import Faker


userTemp = {
    'bios': ['  ']
}

if __name__ == '__main__':
    f = Faker()
    with app.app_context():
        print('Deleting Data...')
        User.query.delete()
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
        # santas = ['Santa Claus', 'Kris Kringle', 'Father Christmas', 'Pere Noel', 'Ded Moroz', 'Babbo Natale']
        # for name in santas:
        #     worker = Worker(
        #         name = name,
        #         role = 'santa',
        #         shop_id = random.randint(1, 3),
        #         created_at = datetime(2023, 1, 1),
        #         phone_number = f.phone_number()
        #     )
        #     db.session.add(worker)

        santa_bios = [
        'Ho Ho Ho! I am Santa Claus, bringing joy and happiness to children all around the world since forever!',
        'Hi there, I am Kris Kringle, also known as Santa Claus, Father Christmas or Saint Nicholas. Nice to meet you!',
        'Oh, you think darkness is your ally. But you merely adopted the dark; I was born in it, moulded by it.',
        'Bonjour! I am Pere Noel, the French version of Santa Claus. I love delivering presents to children on Christmas Eve!',
        'Greetings! I am Ded Moroz, the Russian Santa Claus. I bring presents to children on New Year\'s Eve. Happy holidays!',
        'Ciao! I am Babbo Natale, the Italian Santa Claus. I love Christmas time, when I can deliver presents to all the good children!'
        ]

        santa_pics = [
        'https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/81ITspNsIhL._CR0,0,1414,1414_UX256.jpg',
        'https://s3-us-west-2.amazonaws.com/media.gigroster.com/images/000/003/355/original/SantaMarkKrisKringle_06.jpg?1456330577',
        'https://img.theculturetrip.com/450x/smart/wp-content/uploads/2016/11/1103px-krampus_at_perchtenlauf_klagenfurt.jpg',
        'https://cdn.shortpixel.ai/spai/q_lossy+ret_img+to_auto/https://www.annieandre.com/wp-content/uploads/2021/11/santa-claus-wine-champagne.jpg',
        'https://previews.123rf.com/images/jessaerons/jessaerons1712/jessaerons171200071/92079274-russian-santa-claus.jpg',
        'https://dreamdiscoveritalia.com/wp-content/uploads/2014/12/santa-claus-on-holiday.jpg'

        ]
        santas = ['Santa Claus', 'Kris Kringle', 'Krampus', 'Pere Noel', 'Ded Moroz', 'Babbo Natale']
        for idx, name in enumerate(santas):
            worker = Worker(
                name = name,
                bio = santa_bios[idx],
                role = 'santa',
                shop_id = random.randint(1, 3),
                created_at = datetime(2023, 1, 1),
                phone_number = f.phone_number(),
                img = santa_pics[idx]
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

        # Add Users and Reservations
        for i in range(1, 61):
            user = User(
                name = f.name(),
                email = f.email(),
                created_at = datetime(2023, 1, 1),
                password = 'password',
                phone_number = f.phone_number()
            )
            db.session.add(user)
            db.session.commit()

            reservation = Reservation(
                user_id = i,
                shop_id = random.randint(1, 3),
                scheduled_time = datetime(2023, 12, random.choice(range(1, 23)), random.choice(range(9, 17))),
                created_at = datetime(2023, 1, 1)
            )
            db.session.add(reservation)

        db.session.commit()

print('Database seeding completed successfully.')
