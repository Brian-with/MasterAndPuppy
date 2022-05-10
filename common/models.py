from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    age = models.IntegerField()

    class Meta:
        db_table = 'Owners'

class Dog(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    age = models.IntegerField()

    class Meta:
        db_table = 'Dogs'

