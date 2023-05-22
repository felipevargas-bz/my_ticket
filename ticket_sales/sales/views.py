from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from sales.models import Ticket, Event, Type
from sales.serializers import (TicketSerializerCreate, EventSerializerCreate, TypeSerializerCreate,
                               EventSerializer, TypeSerializer, TicketSerializer)
from utils.make_q import make_q_object
from users.permission_classes import IsAdmin, IsClient

# Create your views here.


class EventView(APIView):
    permission_classes = (IsAuthenticated, (IsAdmin | IsClient))

    def post(self, request):
        data = request.data
        serializer = EventSerializerCreate(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk):
        data = request.data
        event = Event.objects.get(pk=pk)
        serializer = EventSerializerCreate(event, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def get(self, request):
        source_data = dict(request.GET)

        if 'location' in source_data:
            q_object = make_q_object(source_data)

            if q_object:
                events = Event.objects.filter(q_object)
                serializer = EventSerializer(events, many=True)
                rsp = Response(serializer.data, status=200)
            else:
                rsp = Response(status=400)
        else:
            rsp = Response(status=400, data={'error': 'location is required'})
        return rsp

    def delete(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(status=204)


class TypeView(APIView):
    permission_classes = (IsAuthenticated, (IsAdmin | IsClient))

    def post(self, request):
        data = request.data
        serializer = TypeSerializerCreate(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk):
        data = request.data
        type = Type.objects.get(pk=pk)
        serializer = TypeSerializerCreate(type, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def get(self, request):
        source_data = dict(request.GET)

        if 'event' in source_data:
            q_object = make_q_object(source_data)

            if q_object:
                types = Type.objects.filter(q_object)
                serializer = TypeSerializer(types, many=True)
                rsp = Response(serializer.data, status=200)
            else:
                rsp = Response(status=400)
                return rsp

        else:
            rsp = Response(status=400, data={'error': 'event parameter is required exaple: ?event=1 (event id)'})

        return rsp

    def delete(self, request, pk):
        type = Type.objects.get(pk=pk)
        type.delete()
        return Response(status=204)


class TicketView(APIView):
    permission_classes = (IsAuthenticated, (IsAdmin | IsClient))

    def post(self, request):
        data = request.data
        serializer = TicketSerializerCreate(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk):
        data = request.data
        ticket = Ticket.objects.get(pk=pk)
        serializer = TicketSerializerCreate(ticket, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def get(self, request):
        user = request.user
        tickets = Ticket.objects.filter(client=user)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        ticket.delete()
        return Response(status=204)
