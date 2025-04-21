from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_categories'
        ordering = ['sort', 'name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __iter__(self):
        for car in self.cars.all():
            yield car

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='cars/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cars')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_cars'
        ordering = ['sort', 'name']
        verbose_name = 'car'
        verbose_name_plural = 'cars'

    def __str__(self):
        return self.name