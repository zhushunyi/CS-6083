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

from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('index/', views.index),
    # path('layout/', views.layout),
    path('admin/individual_user/', views.admin_individual),
    path('admin/individual_user/<int:nid>/view_all/', views.admin_individual_view_all),
    path('admin/individual_user/<int:nid>/edit/', views.admin_individual_edit),
    path('admin/individual_user/add/', views.admin_add_individual),
    path('admin/individual_user/<int:nid>/delete/', views.admin_individual_delete),


    path('admin/corporate_user/', views.admin_corporate),
    path('admin/corporate_user/add/', views.admin_corporate_add),
    path('admin/corporate_user/<int:nid>/view_all/', views.admin_corporate_view_all),
    path('admin/corporate_user/<int:nid>/edit/', views.admin_corporate_edit),
    path('admin/corporate_user/<int:nid>/delete/', views.admin_corporate_delete),

    path('image/code/', views.image_code),


    path('admin/add/', views.admin_add),
    path('admin/login/', views.admin_login),
    path('admin/logout/', views.admin_logout),

    path('admin/office/', views.office_show),
    path('admin/office/add/', views.office_add),
    path('admin/office/<int:nid>/edit/', views.office_edit),
    path('admin/office/<int:nid>/delete/', views.office_delete),

    path('admin/vehicle/', views.vehicle),
    path('admin/vehicle/add/', views.vehicle_add),
    path('admin/vehicle/<int:nid>/edit/', views.vehicle_edit),
    path('admin/vehicle/<int:nid>/delete/', views.vehicle_delete),

    path('admin/order/', views.admin_order),
    path('admin/order/add/', views.admin_order_add),

    path('admin/invoice/', views.admin_invoice),
    path('admin/invoice/add/', views.admin_invoice_add),
    path('admin/invoice/<int:nid>/delete/', views.admin_invoice_delete),

    path('admin/payment/', views.admin_payment),
    path('admin/payment/add/', views.admin_payment_add),
    path('admin/payment/<int:nid>/delete/', views.admin_payment_delete),

    path('user/login/', views.user_login),
    path('user/order/', views.individual),
    path('user/register/', views.user_register),
    path('user/logout/', views.user_logout),
    path('user/invoice/', views.user_invoice),
    path('user/payment/', views.user_payment),
]
