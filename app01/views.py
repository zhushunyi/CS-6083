from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import AdminIndividualFormViewAll, AdminIndividualEdit, AdminIndividualAdd, AdminCorporateAdd,\
    AdminCorporateViewAll, AdminCorporateEdit


# Create your views here.

def index(request):
    return HttpResponse("欢迎使用")


def layout(request):
    return render(request, 'layout.html')


def admin_individual(request):
    queryset = models.IndividualInfo.objects.all()
    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'admin_individual.html', context)


def admin_individual_view_all(request, nid):
    row_object = models.IndividualInfo.objects.filter(id=nid).first()
    form = AdminIndividualFormViewAll(instance=row_object)
    return render(request, 'admin_view_all.html', {'form': form})


def admin_individual_edit(request, nid):
    row_object = models.IndividualInfo.objects.filter(id=nid).first()

    # get the data from the database for edit
    if request.method == 'GET':
        form = AdminIndividualEdit(instance=row_object)
        return render(request, 'admin_edit.html', {'form': form})
    form = AdminIndividualEdit(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/individual_user/')
    return render(request, 'admin_edit.html', {'form': form})


def admin_add_individual(request):
    if request.method == 'GET':
        form = AdminIndividualAdd()
        return render(request, 'admin_add_individual.html', {'form': form})
    form = AdminIndividualAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/individual_user/')
    return render(request, 'admin_add_individual.html', {'form': form})


def admin_individual_delete(request, nid):
    models.IndividualInfo.objects.filter(id=nid).delete()
    return redirect('/user/individual_user/')


def admin_corporate(request):
    queryset = models.CorporationUser.objects.all()
    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'admin_corporate.html', context)


def admin_corporate_add(request):
    if request.method == 'GET':
        form = AdminCorporateAdd()
        return render(request, 'admin_add_corporate.html', {'form': form})
    form = AdminCorporateAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/corporate_user/')
    return render(request, 'admin_add_corporate.html', {'form': form})


def admin_corporate_view_all(request, nid):
    row_object = models.CorporationUser.objects.filter(id=nid).first()
    form = AdminCorporateViewAll(instance=row_object)
    return render(request, 'admin_corporate_view_all.html', {'form': form})


def admin_corporate_edit(request, nid):
    row_object = models.CorporationUser.objects.filter(id=nid).first()

    # get the data from the database for edit
    if request.method == 'GET':
        form = AdminCorporateEdit(instance=row_object)
        return render(request, 'admin_corporate_edit.html', {'form': form})

    form = AdminCorporateEdit(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/corporate_user/')
    return render(request, 'admin_corporate_edit.html', {'form': form})


def admin_corporate_delete(request, nid):
    models.CorporationUser.objects.filter(id=nid).delete()
    return redirect('/user/corporate_user/')
  
