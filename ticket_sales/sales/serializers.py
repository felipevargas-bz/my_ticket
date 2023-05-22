from rest_framework import serializers
from sales.models import Ticket, Event, Type
from locations.serializers import LocationSerializer
from users.serializers import UserSerializer


class EventSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class TypeSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class TicketSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'location', 'description')


class TypeSerializer(serializers.ModelSerializer):
    event = EventSerializer()

    class Meta:
        model = Type
        fields = ('id', 'name', 'price', 'event', 'max_tickets', 'available_tickets', 'currency')


class TypeSerializerWE(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'name', 'price', 'max_tickets', 'available_tickets', 'currency')


class TicketSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    type = TypeSerializerWE()
    client = UserSerializer()

    class Meta:
        model = Ticket
        fields = ('id', 'client', 'amount', 'event', 'type', 'paid', 'paid_status_code', 'paid_status_message',
                  'paid_date', 'paid_time')
