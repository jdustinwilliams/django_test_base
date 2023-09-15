from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    release_date = models.DateField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="products/")
    manufacturer = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_duration = models.DurationField()
    color_choices = (
        ("red", "Red"),
        ("blue", "Blue"),
        ("green", "Green"),
        ("black", "Black"),
        ("white", "White"),
    )
    color = models.CharField(max_length=10, choices=color_choices)
    product_type_choices = (
        ("electronics", "Electronics"),
        ("clothing", "Clothing"),
        ("appliances", "Appliances"),
        ("books", "Books"),
    )
    product_type = models.CharField(max_length=255, choices=product_type_choices)

    def __str__(self):
        return self.name
