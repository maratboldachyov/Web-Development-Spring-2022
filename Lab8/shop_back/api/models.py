from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def JSON_Format(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.TextField()
    count = models.IntegerField(default=0)
    is_Active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def JSON_Format(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_Active': self.is_Active
        }
