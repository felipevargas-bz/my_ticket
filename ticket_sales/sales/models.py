from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.ForeignKey("locations.Location", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class Ticket(models.Model):
    client = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    amount = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    type = models.ForeignKey("Type", on_delete=models.CASCADE)

    paid = models.BooleanField(default=False)
    paid_status_code = models.IntegerField(default=1)
    paid_status_message = models.CharField(max_length=200, default="Pendiente")
    paid_date = models.DateField(null=True, blank=True)
    paid_time = models.TimeField(null=True, blank=True)


class Type(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    max_tickets = models.IntegerField()
    currency = models.CharField(max_length=10, default="COP")

    @property
    def available_tickets(self):
        tickets = Ticket.objects.filter(type=self)
        return self.max_tickets - tickets.count()

    def __str__(self):
        return self.name
