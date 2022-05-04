"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01 import views as admin_view
from vehicle import views as car_view

print('admin urls', admin.site.urls)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', admin_view.index),
    path('layout/', admin_view.layout),

    # admin
    path('user/individual_user/', admin_view.admin_individual),
    path('user/individual_user/<int:nid>/view_all/', admin_view.admin_individual_view_all),
    path('user/individual_user/<int:nid>/edit/', admin_view.admin_individual_edit),
    path('user/individual_user/add/', admin_view.admin_add_individual),
    path('user/individual_user/<int:nid>/delete/', admin_view.admin_individual_delete),

    # vehicle
    path('vehicle/individual_car/', car_view.car_individual),
    path('vehicle/individual_car/<int:nid>/view_all/', car_view.car_individual_view_all),
    path('vehicle/individual_car/add/', car_view.car_add_individual),
]
