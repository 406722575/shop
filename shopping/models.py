from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    product_description = models.TextField(blank=True)
    product_picture = models.ImageField(upload_to='category', blank=True)

    class Meta:
        verbose_name_plural = '商品类别表'
        db_table = '商品类别表'

    def __str__(self):
        return self.product_name


class Productlist(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    product_description = models.TextField(blank=True)
    product_picture = models.ImageField(upload_to='category', blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    stock = models.IntegerField(default=0)
    shelves = models.BooleanField(default=True)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '产品列表'
        db_table = '产品列表'
        ordering = ('-create_time',)

    def __str__(self):
        return self.product_name