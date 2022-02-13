from django.db import models


class User(models.Model):
    name = models.CharField(blank=True, max_length=100)
    password = models.CharField(blank=True, max_length=100)
    email = models.CharField(blank=True, max_length=100)
    phone_number = models.CharField(blank=True, max_length=100)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Shopcard(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, related_name='shopcards')
    credit = models.CharField(blank=True, max_length=100)
    card_number = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.card_number


class Item(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='items', blank=True)
    card = models.ForeignKey(
        Shopcard, on_delete=models.CASCADE, related_name='items', blank=True, null=True)
    name = models.CharField(blank=True, max_length=100)
    origin_purchasing_time = models.DateField(blank=True)
    origin_price = models.CharField(blank=True, max_length=100)
    condition = models.CharField(blank=True, max_length=100, null=True)
    image = models.TextField(blank=True)
    asking_price = models.CharField(blank=True, max_length=100)
    sold_mark = models.BooleanField(blank=True)

    def __str__(self):
        return self.name
