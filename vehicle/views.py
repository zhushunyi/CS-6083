from django.shortcuts import render, redirect
from vehicle import models
from vehicle.utils.pagination import Pagination
from vehicle.utils.form import VehicleInfoFormViewAll, CarIndividualAdd, CarIndividualEdit


# Create your views here.
def car_individual(request):
    queryset = models.VehicleInfo.objects.all()
    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'car_individual.html', context)


def car_individual_view_all(request, nid):
    row_object = models.VehicleInfo.objects.filter(id=nid).first()
    form = VehicleInfoFormViewAll(instance=row_object)
    return render(request, 'car_view_all.html', {'form': form})


def car_add_individual(request):
    if request.method == 'GET':
        form = CarIndividualAdd()
        return render(request, 'car_add_individual.html', {'form': form})
    form = CarIndividualAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/vehicle/individual_car/')
    return render(request, 'car_add_individual.html', {'form': form})


def car_individual_edit(request, nid):
    row_object = models.VehicleInfo.objects.filter(id=nid).first()

    # get the data from the database for edit
    if request.method == 'GET':
        form = CarIndividualEdit(instance=row_object)
        return render(request, 'vehicle_edit.html', {'form': form})
    form = CarIndividualEdit(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/vehicle/individual_car/')
    return render(request, 'vehicle_edit.html', {'form': form})


def car_individual_delete(request, nid):
    models.VehicleInfo.objects.filter(id=nid).delete()
    return redirect('/vehicle/individual_car/')