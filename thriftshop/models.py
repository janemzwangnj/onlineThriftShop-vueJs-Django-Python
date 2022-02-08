from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Shopcard(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='shopcards')
    credit = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)

    def __str__(self):
        return self.card_number


class Item(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='items')
    card_number = models.ForeignKey(
        Shopcard, on_delete=models.CASCADE, related_name='items', blank=True, null=True)
    name = models.CharField(max_length=100)
    origin_purchasing_time = models.DateField()
    origin_price = models.CharField(max_length=100)
    condition = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=100, blank=True)
    asking_price = models.CharField(max_length=100)
    sold_mark = models.BooleanField()

    def __str__(self):
        return self.name
