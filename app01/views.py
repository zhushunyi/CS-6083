from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import AdminIndividualFormViewAll, AdminIndividualEdit, AdminIndividualAdd, AdminCorporateAdd, \
    AdminCorporateViewAll, AdminCorporateEdit, AdminAdd, AdminLogin, OfficeAdd, OfficeEdit, VehicleAdd, VehicleEdit, \
    OrderAdd, InvoiceAdd, PaymentAdd, UserLogin

from app01.utils.code import check_code
from io import BytesIO


# Create your views here.


def admin_individual(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["id"] = search_data

    queryset = models.IndividualInfo.objects.filter(**data_dict)

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
        return redirect('/admin/individual_user/')
    return render(request, 'admin_edit.html', {'form': form})


def admin_add_individual(request):
    if request.method == 'GET':
        form = AdminIndividualAdd()
        return render(request, 'admin_add_individual.html', {'form': form})
    form = AdminIndividualAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/individual_user/')
    return render(request, 'admin_add_individual.html', {'form': form})


def admin_individual_delete(request, nid):
    models.IndividualInfo.objects.filter(id=nid).delete()
    return redirect('/admin/individual_user/')


def admin_corporate(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["employ_id"] = search_data

    queryset = models.CorporationUser.objects.filter(**data_dict)
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
        return redirect('/admin/corporate_user/')
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
        return redirect('/admin/corporate_user/')
    return render(request, 'admin_corporate_edit.html', {'form': form})


def admin_corporate_delete(request, nid):
    models.CorporationUser.objects.filter(id=nid).delete()
    return redirect('/admin/corporate_user/')


def admin_add(request):
    if request.method == 'GET':
        form = AdminAdd()
        return render(request, 'admin_add.html', {'form': form})

    form = AdminAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/login/')
    return render(request, 'admin_add.html', {'form': form})


def admin_login(request):
    if request.method == 'GET':
        form = AdminLogin()
        return render(request, 'admin_login.html', {'form': form})
    form = AdminLogin(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "Wrong Code")
            return render(request, 'admin_login.html', {'form': form})

        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "Wrong Username or Password")
            return render(request, 'admin_login.html', {'form': form})
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/admin/individual_user/")
    return render(request, 'admin_login.html', {'form': form})


def image_code(request):
    img, code_string = check_code()
    request.session['image_code'] = code_string
    # request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def admin_logout(request):
    request.session.clear()
    return redirect('/admin/login/')


def office_show(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["id"] = search_data

    queryset = models.Office.objects.filter(**data_dict)

    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'admin_office.html', context)


def office_add(request):
    if request.method == 'GET':
        form = OfficeAdd()
        return render(request, 'office_add.html', {'form': form})

    form = OfficeAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/office/')
    return render(request, 'office_add.html', {'form': form})


def office_edit(request, nid):
    row_object = models.Office.objects.filter(id=nid).first()

    # get the data from the database for edit
    if request.method == 'GET':
        form = OfficeEdit(instance=row_object)
        return render(request, 'office_edit.html', {'form': form})
    form = OfficeEdit(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/office/')
    return render(request, 'office_edit.html', {'form': form})


def office_delete(request, nid):
    models.Office.objects.filter(id=nid).delete()
    return redirect('/admin/office/')


def vehicle(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["id"] = search_data

    queryset = models.Vehicle.objects.filter(**data_dict)
    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'admin_vehicle.html', context)


def vehicle_add(request):
    if request.method == 'GET':
        form = VehicleAdd()
        return render(request, 'vehicle_add.html', {'form': form})

    form = VehicleAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/vehicle/')
    return render(request, 'vehicle_add.html', {'form': form})


def vehicle_edit(request, nid):
    row_object = models.Vehicle.objects.filter(id=nid).first()

    if request.method == 'GET':
        form = VehicleEdit(instance=row_object)
        return render(request, 'vehicle_edit.html', {'form': form})
    form = VehicleEdit(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/vehicle/')
    return render(request, 'vehicle_edit.html', {'form': form})


def vehicle_delete(request, nid):
    models.Vehicle.objects.filter(id=nid).delete()
    return redirect('/admin/vehicle/')


def individual(request):
    return render(request, 'individual.html')


def admin_order(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["id"] = search_data

    queryset = models.Order.objects.filter(**data_dict)
    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'admin_order.html', context)


def admin_order_add(request):
    if request.method == 'GET':
        form = OrderAdd()
        return render(request, 'admin_order_add.html', {'form': form})

    form = OrderAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/order/')
    return render(request, 'admin_order_add.html', {'form': form})


def admin_invoice(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["id"] = search_data

    queryset = models.Invoice.objects.filter(**data_dict)
    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'admin_invoice.html', context)


def admin_invoice_add(request):
    if request.method == 'GET':
        form = InvoiceAdd()
        return render(request, 'admin_invoice_add.html', {'form': form})

    form = InvoiceAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/invoice/')
    return render(request, 'admin_invoice_add.html', {'form': form})


def admin_invoice_delete(request, nid):
    models.Invoice.objects.filter(id=nid).delete()
    return redirect('/admin/invoice/')


def admin_payment(request):
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["id"] = search_data

    queryset = models.Payment.objects.filter(**data_dict)
    page_object = Pagination(request, queryset, page_size=5)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'admin_payment.html', context)


def admin_payment_add(request):
    if request.method == 'GET':
        form = PaymentAdd()
        return render(request, 'admin_payment_add.html', {'form': form})

    form = PaymentAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/payment/')
    return render(request, 'admin_payment_add.html', {'form': form})


def admin_payment_delete(request, nid):
    models.Payment.objects.filter(id=nid).delete()
    return redirect('/admin/payment/')


def user_login(request):
    if request.method == 'GET':
        form = UserLogin()
        return render(request, 'individual_login.html', {'form': form})
    form = UserLogin(data=request.POST)

    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "Wrong Code")
            return render(request, 'admin_login.html', {'form': form})

        # print(form.cleaned_data['username'])
        admin_object = models.IndividualInfo.objects.filter(username=form.cleaned_data['username']).first()
        # print(admin_object)
        if not admin_object:
            form.add_error("password", "Wrong Username or Password")
            return render(request, 'individual_login.html', {'form': form})
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/user/individual/")
    return render(request, 'individual_login.html', {'form': form})


def user_logout(request):
    request.session.clear()
    return redirect('/user/login/')