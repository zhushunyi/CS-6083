from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import AdminIndividualFormViewAll, AdminIndividualEdit, AdminIndividualAdd


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
