from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField


class Car(models.Model):
    name = models.CharField(max_length=20, verbose_name='Модель транспорта')

    def __str__(self):
        return self.name


class Mark(models.Model):
    name = models.CharField(max_length=20, verbose_name='Модель транспорта')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='mark', verbose_name='Марка транспорта',
                             default=None)

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    name = models.CharField(null=True, blank=True,max_length=200, verbose_name='Тип услуги')

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(null=True, blank=True,max_length=50, verbose_name='Роль')

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30, verbose_name='Страна')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='Город')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country', verbose_name='Страна',
                            default=None)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
    phone_number = PhoneField(null=True, blank=True, verbose_name='Номер телеофона')
    photo = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Фото')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role', verbose_name='Роль',
                               default=None)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='profile_country', verbose_name='Страна')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city', verbose_name='Город')
    servicetype = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='servicetype',
                                    verbose_name='Тип услуги')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car', verbose_name='Танспорт')
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='mark', verbose_name='Модель', default=None)

    def __str__(self):
        return self.user.get_full_name()
# class Driver(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
#     phone_number = PhoneField(null=True, blank=True, verbose_name='Номер телеофона')
#     photo = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Фото')
#     role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role', verbose_name='Роль',
#                                default=None)