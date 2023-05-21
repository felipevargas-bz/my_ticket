from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class Sale(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


class Type(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    max_tickets = models.IntegerField()
    tickets_available = models.IntegerField()

    def __str__(self):
        return self.name


class Ticket(models.Model):
    client = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    amount = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
