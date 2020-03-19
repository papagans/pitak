from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView, DetailView, ListView, DeleteView, FormView, CreateView
from accounts.models import Car, Profile, Role, Mark, ServiceType, Role, Country, City
from accounts.forms import UserCreationForm
from django.shortcuts import redirect, get_object_or_404
from django.utils.http import urlencode
from django.db.models import Q
from django.contrib.auth.mixins import PermissionRequiredMixin

def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            try:
                photo = request.FILES['photo']
            except:
                photo = None

            profile = Profile(
                user=user,
                # role=form.cleaned_data['role'],
                phone_number=form.cleaned_data['phone_number'],
                photo=photo,
                servicetype=form.cleaned_data['servicetype'],
                car=form.cleaned_data['car'],
                mark=form.cleaned_data['mark'],
                city=form.cleaned_data['city'],
                country=form.cleaned_data['country'],
                role=form.cleaned_data['role'],
            )
            user.set_password(form.cleaned_data['password'])
            # passport.save()
            profile.save()
            role = form.cleaned_data['role']
            role = Role.objects.filter(pk=role.pk)
            profile.save()
            # profile.role.save(role)
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:user_detail', kwargs={"pk": user.pk}))
    else:
        form = UserCreationForm()
    return render(request, 'user_create.html', context={'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
# Create your views here.


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'user'


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'car'


class CarCreateView(CreateView):
    model = Car
    template_name = 'car_add.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('accounts:car_list')


class MarkListView(ListView):
    model = Car
    template_name = 'mark_list.html'
    context_object_name = 'cars'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(MarkListView, self).get_context_data(*args, **kwargs)
    #
    #     context['cars'] = Car.objects.all()
    #
    #     return context


class MarkCreateView(CreateView):
    model = Mark
    template_name = 'mark_add.html'
    fields = ['name', 'car']

    def get_success_url(self):
        return reverse('accounts:mark_list')