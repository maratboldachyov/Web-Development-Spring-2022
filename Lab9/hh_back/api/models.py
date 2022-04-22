from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=200, default='')
    city = models.CharField(max_length=20, default='')
    address = models.TextField(max_length=200, default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=200, default='')
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    priority = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'priority': self.priority,
            'active': self.active
        }
