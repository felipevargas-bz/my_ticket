from rest_framework import serializers
from locations.models import Location, City, Country, Department


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Department
        fields = ("id", "name", "country")


class CitySerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = City
        fields = ("id", "name", "department")


class LocationSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Location
        fields = ("id", "name", "address", "city")


class LocationSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name", "address", "city", "country", "department")
