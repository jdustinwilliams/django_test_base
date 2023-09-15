import random
from datetime import timedelta
from io import BytesIO

from django.core.management.base import BaseCommand
from django.core.files import File

from PIL import Image, ImageDraw, ImageFont
from faker import Faker

from products.models import Product


# Generate a random pattern to make the dummy images more interesting
def generate_pattern_image():
    width = random.randint(100, 2048)
    height = random.randint(100, 2048)

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Generate random patterns or text
    for _ in range(random.randint(1, 5)):
        x0 = random.randint(0, width)
        y0 = random.randint(0, height)
        x1 = random.randint(x0, width)
        y1 = random.randint(y0, height)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.rectangle([x0, y0, x1, y1], fill=color)

    font = ImageFont.load_default()
    text = "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        for _ in range(5)
    )
    draw.text(
        (random.randint(0, width - 30), random.randint(0, height - 20)),
        text,
        fill="black",
        font=font,
    )

    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    return buffer


def generate_dummy_data(num_records):
    fake = Faker()

    for _ in range(num_records):
        num_words = random.randint(1, 3)
        product_name = " ".join(fake.words(nb=num_words))

        product = Product(
            name=product_name,
            description=fake.text(),
            price=random.uniform(10, 1000),
            is_available=random.choice([True, False]),
            release_date=fake.date_between(start_date="-1y", end_date="today"),
            rating=random.uniform(1, 5),
            manufacturer=fake.company(),
            weight=random.uniform(0.1, 50),
            warranty_duration=timedelta(days=random.randint(30, 365 * 5)),
            color=random.choice(["red", "blue", "green", "black", "white"]),
            product_type=random.choice(
                ["electronics", "clothing", "appliances", "books"]
            ),
        )

        # Generate and save a random image
        buffer = generate_pattern_image()
        product.image.save(f"{fake.word()}.jpg", File(buffer))

        product.save()


class Command(BaseCommand):
    help = "Generate dummy data for the Product model"

    def handle(self, *args, **kwargs):
        num_records = int(input("Enter the number of dummy records to create: "))
        generate_dummy_data(num_records)
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {num_records} dummy records.")
        )
