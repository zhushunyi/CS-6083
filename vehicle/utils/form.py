from vehicle import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from vehicle.utils.bootstrap import BootStrapModelForm


class VehicleInfoFormViewAll(BootStrapModelForm):
    ID = forms.CharField(disabled=True, label="ID")
    Make = forms.IntegerField(disabled=True, label="Make")
    Model = forms.CharField(disabled=True, label="Model")
    MakeYear = forms.DateField(disabled=True, label="Make Date")
    VehicleIdentificationNumber = forms.CharField(disabled=True, label="Vehicle_Identification_Number")
    LicensePlateNumber = forms.CharField(disabled=True, label="License Plate Number")

    VehicleClass = forms.CharField(disabled=True, label="Vehicle Class")
    OfficeInfo = forms.CharField(disabled=True, label="Office Info")

    class Meta:
        model = models.VehicleInfo
        fields = [
            "ID",
            "Make",
            "Model",
            "MakeYear",
            "VehicleIdentificationNumber",
            "LicensePlateNumber",
            "VehicleClass",
            "OfficeInfo",
        ]


class CarIndividualAdd(BootStrapModelForm):
    class Meta:
        model = models.VehicleInfo
        fields = [
            "make",
            "model",
            "make_year",
            "VIN",
            "LPN",
            "vehicle_class",
            "office_info",
        ]

