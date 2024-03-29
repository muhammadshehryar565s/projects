# Generated by Django 4.2 on 2023-05-21 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("selling_price", models.FloatField(max_length=100)),
                ("discount_price", models.FloatField(max_length=100)),
                ("composition", models.TextField()),
                ("discription", models.TextField()),
                ("prodapp", models.TextField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("CR", "Curd"),
                            ("ML", "Milk"),
                            ("LS", "Lassi"),
                            ("MS", "Milikshake"),
                            ("PN", "Paneer"),
                            ("CZ", "Cheese"),
                            ("IC", "Ice-Cream"),
                        ],
                        max_length=2,
                    ),
                ),
                ("product_image", models.ImageField(upload_to="product")),
            ],
        ),
    ]
