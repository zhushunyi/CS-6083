import dateutil.utils
from django.db import models
from datetime import datetime
from random import random, randint

# Create your models here.
# for database


class AdminInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class IndividualInfo(models.Model):
    username = models.CharField(verbose_name="username", max_length=32,
                                default=(datetime.strftime(datetime.now(), '%Y%m%d%H%M')) + str(randint(1000, 9999)))
    password = models.CharField(verbose_name="password", max_length=64,
                                default=(datetime.strftime(datetime.now(), '%Y%m%d%H%M')) + str(randint(1000, 9999)))
    street = models.CharField(verbose_name="street", max_length=64)
    city = models.CharField(verbose_name="city", max_length=32)
    zipcode = models.CharField(verbose_name="zipcode", max_length=10)
    email = models.CharField(verbose_name="e-mail address", max_length=32)
    phone = models.CharField(verbose_name="phone number", max_length=32)
    FirstName = models.CharField(verbose_name="first name", max_length=32)
    MiddleName = models.CharField(verbose_name="middle name", max_length=32)
    LastName = models.CharField(verbose_name="last name", max_length=32)
    InsuranceCompany = models.CharField(verbose_name="insurance company", max_length=32)
    InsuranceNumber = models.CharField(verbose_name="insurance number", max_length=10)
    rate = models.DecimalField(verbose_name="Coupon Rate", max_digits=10, decimal_places=2, default=0)
    StartDate = models.DateField(verbose_name="Start Date")
    EndDate = models.DateField(verbose_name="End Date")


class CorporationUser(models.Model):
    street = models.CharField(verbose_name="street", max_length=64)
    city = models.CharField(verbose_name="city", max_length=32)
    zipcode = models.CharField(verbose_name="zipcode", max_length=10)
    email = models.CharField(verbose_name="e-mail address", max_length=32)
    phone = models.CharField(verbose_name="phone number", max_length=32)
    employ_id = models.CharField(verbose_name="employ id", max_length=10)
    corporation_choices = (
        (1, "D&G Tax Law"),
        (2, "The Acrobatic Accountants LLC"),
        (3, "Cafe Msica"),
        (4, "Artisan Recording"),
        (5, "New York Man"),
        (6, "Dreamlike Moustaches"),
        (7, "Swift River Sports"),
        (8, "The Big Apple Cocktail Company"),
        (9, "Pouring Palaces"),
        (10, "Schmalzy Pet"),
    )
    corporation_name = models.SmallIntegerField(verbose_name="corporation name", choices=corporation_choices)
    rate = models.DecimalField(verbose_name="Coupon Rate", max_digits=10, decimal_places=2, default=0)


class Admin(models.Model):
    username = models.CharField(verbose_name="user name", max_length=32)
    password = models.CharField(verbose_name="password", max_length=64)


class Office(models.Model):
    name = models.CharField(verbose_name="office name", max_length=64)
    street = models.CharField(verbose_name="street", max_length=64)
    city = models.CharField(verbose_name="city",max_length=32)
    zipcode = models.CharField(verbose_name="zipcode", max_length=10)
    phone = models.CharField(verbose_name="phone number", max_length=10)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    Vclass_choice = (
        (1, "small"),
        (2, "mid-size"),
        (3, "luxury"),
        (4, "SUV"),
        (5, "premium"),
        (6, "special"),
        (7, "van"),
    )
    Vclass = models.SmallIntegerField(verbose_name="Class", choices=Vclass_choice)
    make_choices = (
        (1, "Mercedes-Benz"),
        (2, "Audi"),
        (3, "GMC"),
        (4, "Nissan"),
        (5, "Avalon"),
        (6, "Blazer"),
        (7, "Cayenne Coupe"),
    )
    make = models.SmallIntegerField(verbose_name="Make", choices=make_choices)
    year = models.DateField(verbose_name="Year")
    VIN = models.CharField(verbose_name="VIN", max_length=10)
    LPN = models.CharField(verbose_name="LPN", max_length=10)
    daily_rate = models.DecimalField(verbose_name="Daily Rate", max_digits=10, decimal_places=2, default=0)
    extra_rate = models.DecimalField(verbose_name="Extra Rate", max_digits=10, decimal_places=2, default=0)
    limit = models.DecimalField(verbose_name="Limit", max_digits=10, decimal_places=2, default=0)
    office = models.ForeignKey(to="Office", to_field="id", on_delete=models.CASCADE)


class Order(models.Model):
    StartDate = models.DateField(verbose_name="Start Date")
    EndDate = models.DateField(verbose_name="End Date")
    point_choices = (
        (1, "Washington"),
        (2, "Idaho"),
        (3, "Oregon"),
        (4, "Montana"),
        (5, "California"),
        (6, "Nevada"),
        (7, "Utah"),
        (8, "Arizona"),
        (9, "Wyoming"),
        (10, "Colorado"),
        (11, "New Mexcio"),
        (12, "North Dakota"),
    )
    StartPoint = models.SmallIntegerField(verbose_name="Start Point", choices=point_choices)
    EndPoint = models.SmallIntegerField(verbose_name="End Point", choices=point_choices)
    UserId = models.ForeignKey(to="IndividualInfo", to_field="id", on_delete=models.CASCADE)
    VehicleId = models.ForeignKey(to="Vehicle", to_field="id", on_delete=models.CASCADE)
    distance = models.IntegerField(verbose_name="Distance")
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.distance = abs(500 * (self.EndPoint - self.StartPoint))
        delta = self.EndDate - self.StartDate
        # temp = Order.objects.get(id=self.id)
        # print(self.UserId)
        # print(self.VehicleId)
        vid = self.VehicleId
        uid = self.UserId
        daily = vid.daily_rate
        extra = vid.extra_rate
        lim = vid.limit
        coupon_rate = uid.rate
        if self.distance > lim * delta.days:
            self.price = delta.days * daily + extra * (self.distance - lim * delta.days)
        else:
            self.price = delta.days * daily
        self.price = self.price * (1 - coupon_rate)
        super(Order, self).save(*args, **kwargs)

