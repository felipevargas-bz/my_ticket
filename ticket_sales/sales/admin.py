from django.contrib import admin
from sales.models import Event, Ticket, Sale, Type

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)


class TypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Type, TypeAdmin)


class TicketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ticket, TicketAdmin)


class SaleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sale, SaleAdmin)
