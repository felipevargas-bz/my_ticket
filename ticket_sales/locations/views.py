from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from locations.models import Location, City, Country, Department
from locations.serializers import (
    LocationSerializer,
    CitySerializer,
    CountrySerializer,
    DepartmentSerializer,
    LocationSerializerCreate,
)
from utils.make_q import make_q_object
from users.permission_classes import IsAdmin, IsClient

# Create your views here.


class LocationView(APIView):
    permission_classes = (IsAuthenticated, (IsAdmin | IsClient))

    def post(self, request):
        data = request.data
        serializer = LocationSerializerCreate(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk):
        data = request.data
        location = Location.objects.get(pk=pk)
        serializer = LocationSerializer(location, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def get(self, request):
        source_data = dict(request.GET)

        if (
            "country" in source_data
            and "city" in source_data
            and "department" in source_data
        ):
            q_object = make_q_object(source_data)
            if q_object:
                locations = Location.objects.filter(q_object)
                serializer = LocationSerializer(locations, many=True)
                rsp = Response(serializer.data, status=200)
            else:
                rsp = Response(status=400)
        else:
            rsp = Response(status=400, data={"error": "country and city are required"})
        return rsp

    def delete(self, request, pk):
        location = Location.objects.get(pk=pk)
        location.delete()
        return Response(status=204)


class CityView(APIView):
    permission_classes = (IsAuthenticated, (IsAdmin | IsClient))

    def post(self, request):
        data = request.data
        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk):
        data = request.data
        city = City.objects.get(pk=pk)
        serializer = CitySerializer(city, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def get(self, request):
        source_data = dict(request.GET)
        q_object = make_q_object(source_data)

        if q_object:
            cities = City.objects.filter(q_object)
        else:
            cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        city = City.objects.get(pk=pk)
        city.delete()
        return Response(status=204)


class CountryView(APIView):
    permission_classes = (IsAuthenticated, (IsAdmin | IsClient))

    def post(self, request):
        data = request.data
        serializer = CountrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk):
        data = request.data
        country = Country.objects.get(pk=pk)
        serializer = CountrySerializer(country, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def get(self, request):
        source_data = dict(request.GET)
        q_object = make_q_object(source_data)

        if q_object:
            countries = Country.objects.filter(q_object)
        else:
            countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        country = Country.objects.get(pk=pk)
        country.delete()
        return Response(status=204)


class DepartmentView(APIView):
    permission_classes = (IsAuthenticated, (IsAdmin | IsClient))

    def post(self, request):
        data = request.data
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, pk):
        data = request.data
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(department, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    def get(self, request):
        source_data = dict(request.GET)
        q_object = make_q_object(source_data)

        if "country" in source_data:
            if q_object:
                departments = Department.objects.filter(q_object)
            else:
                departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        department = Department.objects.get(pk=pk)
        department.delete()
        return Response(status=204)
