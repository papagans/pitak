from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import register_view, UserDetailView, UserListView, CarCreateView, CarListView, MarkCreateView, \
    MarkListView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name='user_create'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('list/user/', UserListView.as_view(), name='user_list'),
    path('list/car/', CarListView.as_view(), name='car_list'),
    path('car/add/', CarCreateView.as_view(), name='car_add'),
    path('mark/add/', MarkCreateView.as_view(), name='mark_add'),
    path('list/mark/', MarkListView.as_view(), name='mark_list'),
]