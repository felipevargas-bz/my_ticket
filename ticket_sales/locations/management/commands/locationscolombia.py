from django.core.management.base import BaseCommand
from locations.models import Country, Department, City, Location


class Command(BaseCommand):
    help = "Crea las ciudades de Colombia"

    def handle(self, *args, **options):
        # Crear país
        country = Country.objects.create(name='Colombia')

        # Crear departamentos
        departments = [
            Department(id=1, name='Amazonas', country_id=country.id),
            Department(id=2, name='Antioquia', country_id=country.id),
            Department(id=3, name='Arauca', country_id=country.id),
            Department(id=4, name='Atlántico', country_id=country.id),
            Department(id=5, name='Bolívar', country_id=country.id),
            Department(id=6, name='Boyacá', country_id=country.id),
            Department(id=7, name='Caldas', country_id=country.id),
            Department(id=8, name='Caquetá', country_id=country.id),
            Department(id=9, name='Casanare', country_id=country.id),
            Department(id=10, name='Cauca', country_id=country.id),
        ]
        Department.objects.bulk_create(departments)

        # Crear ciudades
        cities = [
            # Amazonas
            City(id=1, name='Leticia', department_id=1),

            # Antioquia
            City(id=2, name='Medellín', department_id=2),
            City(id=3, name='Bello', department_id=2),
            City(id=4, name='Envigado', department_id=2),
            City(id=5, name='Itagüí', department_id=2),

            # Arauca
            City(id=6, name='Arauca', department_id=3),

            # Atlántico
            City(id=7, name='Barranquilla', department_id=4),
            City(id=8, name='Soledad', department_id=4),
            City(id=9, name='Malambo', department_id=4),
            City(id=10, name='Sabanalarga', department_id=4),

            # Bolívar
            City(id=11, name='Cartagena', department_id=5),
            City(id=12, name='Turbaco', department_id=5),
            City(id=13, name='Magangué', department_id=5),
            City(id=14, name='El Carmen de Bolívar', department_id=5),

            # Boyacá
            City(id=15, name='Tunja', department_id=6),
            City(id=16, name='Duitama', department_id=6),
            City(id=17, name='Sogamoso', department_id=6),
            City(id=18, name='Chiquinquirá', department_id=6),

            # Caldas
            City(id=19, name='Manizales', department_id=7),
            City(id=20, name='Villamaría', department_id=7),
            City(id=21, name='Chinchiná', department_id=7),
            City(id=22, name='La Dorada', department_id=7),

            # Caquetá
            City(id=23, name='Florencia', department_id=8),
            City(id=24, name='San Vicente del Caguán', department_id=8),
            City(id=25, name='Puerto Rico', department_id=8),
            City(id=26, name='Belén de los Andaquíes', department_id=8),

            # Casanare
            City(id=27, name='Yopal', department_id=9),
            City(id=28, name='Aguazul', department_id=9),
            City(id=29, name='Paz de Ariporo', department_id=9),
            City(id=30, name='Tauramena', department_id=9),

            # Cauca
            City(id=31, name='Popayán', department_id=10),
            City(id=32, name='Santander de Quilichao', department_id=10),
            City(id=33, name='Guachené', department_id=10),
            City(id=34, name='Patía', department_id=10),
        ]
        City.objects.bulk_create(cities)
