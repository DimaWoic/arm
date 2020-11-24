from django.contrib import admin
from .models import Transport, Record, Route, NumCar, PhoneNumbers, Company, CompanyUnit

admin.site.register(Transport)
admin.site.register(Record)
admin.site.register(Route)
admin.site.register(NumCar)
admin.site.register(PhoneNumbers)
admin.site.register(Company)
admin.site.register(CompanyUnit)
