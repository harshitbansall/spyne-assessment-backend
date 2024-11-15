from django.db import models
from django.core.exceptions import ValidationError

from authentication.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return 'Product {} : {}'.format(self.id, self.user)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_images/")

    class Meta:
        db_table = 'product_images'

    def clean(self):
        if self.product.images.count() >= 10:
            raise ValidationError("A product cannot have more than 10 images.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Product Image : {}'.format(self.image)
