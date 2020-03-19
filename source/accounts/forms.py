from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from accounts.models import Car, Profile, Role, Mark, ServiceType, Role, Country, City
from django import forms
from django.forms import ModelForm


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    phone_number = forms.IntegerField(label='Номер телефона', required=False)
    photo = forms.ImageField(label='Фото', required=False)
    role = forms.ModelChoiceField(label='Роль', queryset=Role.objects.all(), required=False)
    car = forms.ModelChoiceField(label='Модель транспорта', queryset=Car.objects.all(), required=False)
    mark = forms.ModelChoiceField(label='Марка транспорта', queryset=Mark.objects.all(), required=False)
    city = forms.ModelChoiceField(label='Город', queryset=City.objects.all(), required=False)
    country = forms.ModelChoiceField(label='Страна', queryset=Country.objects.all())
    servicetype = forms.ModelChoiceField(label='Тип услуги', queryset=ServiceType.objects.all(), required=False)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            try:
                return getattr(self.instance.profile, field_name)
            except Profile.DoesNotExist:
                return None
        return super().get_initial_for_field(field, field_name)

    # def get_initial_for_passport(self, field, field_name):
    #     if field_name in self.Meta.profile_fields:
    #         try:
    #             return getattr(self.instance.profile, field_name)
    #         except Profile.DoesNotExist:
    #             return None
    #     return super().get_initial_for_field(field, field_name)

    # def save_role(self, commit=True):
    #     try:
    #         role = self.instance.role
    #     except Role.DoesNotExist:
    #         role = Profile.objects.create(role=self.instance)
    #     for field in self.Meta.passport_fields:
    #         setattr(role, field, self.cleaned_data[field])
    #     if commit:
    #         role.save()

    def save_profile(self, commit=True):
        try:
            profile = self.instance.profile
        except Profile.DoesNotExist:
            profile = Profile.objects.create(profile=self.instance)
        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data[field])
        if not profile.photo:
            profile.photo = None
        if commit:
            profile.save()

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name']
        profile_fields = ['phone_number', 'photo', 'role', 'car', 'mark', 'city', 'country',
                          'servicetype']
