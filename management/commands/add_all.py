from django.core.management.base import BaseCommand
from arm.models import Transport, Route, NumCar


def add_all():
    transports = ['трамвай', 'троллейбус']
    for t in transports:
        transport = Transport()
        try:
            transport.name = t
            transport.save()
        except Exception as e:
            pass

    routes = ['1', '2', '2а', '3', '4', '5', '5а', '6', '7', '8', '9', '10', '11', '15', '16']
    for r in routes:
        route = Route()
        try:
            route.name = r
            route.save()
        except Exception as e:
            pass

    num_cars = ['631', '66-40', '428', '790']
    for n in num_cars:
        num_car = NumCar()
        try:
            num_car.name = n
            num_car.save()
        except Exception as e:
            pass


class Command(BaseCommand):

    def handle(self, *args, **options):
        add_all()