from django.contrib import admin
from accounts.models import Profile, ServiceType, Country, Car, Role, Mark, City

admin.site.register(Profile)
admin.site.register(ServiceType)
admin.site.register(Country)
admin.site.register(Car)
admin.site.register(Role)
admin.site.register(Mark)
admin.site.register(City)
# Register your models here.
