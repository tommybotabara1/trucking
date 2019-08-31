from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import JsonResponse
from .forms import *
from datetime import datetime

def index(request):
    return render(request, 'index.html',)

def testing(request):
    users_list = Userinformation.objects.all()

    return render(request, 'testingDataTable.html', {'users_list': users_list})


def database_operations(request):
    list = Table1.objects.all()
    return render(request, 'databaseOperations.html', {'list': list})


def new_database_operation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DatabaseOperationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('edit_database_operation', id=Table1.objects.last().id, phase="B")
        else:
            return HttpResponse(form.errors)
    else:
        form = DatabaseOperationForm()
        driver_form = DriverForm()
        customer_form = CustomerForm()
        client_form = ClientForm()
        extra = -1
        return render(request, 'databaseOperationForm.html', {'form': form,
                                                              'extra': extra,
                                                              'driver_form': driver_form,
                                                              'customer_form': customer_form,
                                                              'client_form': client_form,
                                                              })


def edit_database_operation(request, id, phase):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        a = Table1.objects.get(id=id)
        form = DatabaseOperationForm(request.POST, instance=a)
        form.data = form.data.copy()
        date = form.data['receiveddatetime']
        if date != '':
            form.data['receiveddatetime'] = datetime.strptime(date, "%Y-%m-%dT%H:%M")

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            newDatabaseOperation = form.save()
            # redirect to a new URL:
            list = Table1.objects.all()
            return render(request, 'databaseOperations.html', {'list': list})
        else:
            return HttpResponse(form.errors)
    else:
        a = Table1.objects.get(id=id)
        form = DatabaseOperationForm(instance=a)
        extra = id
        phase = phase

        driver_form = DriverForm()
        customer_form = CustomerForm()
        client_form = ClientForm()

    return render(request, 'databaseOperationForm.html', {'form': form,
                                                          'extra': extra,
                                                          'driver_form': driver_form,
                                                          'customer_form': customer_form,
                                                          'client_form': client_form,
                                                          'phase': phase})


def delete_database_operation(request, id):
    list = Table1.objects.all()

    Table1.objects.get(id=id).delete()
    extra = "Database Operation " + str(id) + " Deleted"

    return render(request, 'databaseOperations.html', {'list': list, 'extra': extra})


def users(request):
    users_list = Userinformation.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserInformationForm(request.POST)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            userInformation = form.save()

            # redirect to a new URL:
            return HttpResponse('user created')
    else:
        form = UserInformationForm()

    return render(request, 'users.html', {'form': form, 'users_list': users_list})


def add_new_driver(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DriverForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDriverForm = form.save()
            # redirect to a new URL:
            newDriver = Driver.objects.last()
            response = [{
                "response": 'New Driver Added',
                "driverName": newDriver.drivername,
                "driverID": newDriver.driverid
            }]
            return JsonResponse(response, safe=False)
        else:
            return HttpResponse(form.errors)
    else:
        form = DatabaseOperationForm()
        driver_form = DriverForm()

    return JsonResponse(['not'], safe=False)


def add_new_customer(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newCustomerForm = form.save()
            # redirect to a new URL:
            newCustomer = Customer.objects.last()
            response = [{
                "response": 'New Customer Added',
                "customerName": newCustomer.customername,
                "customerID": newCustomer.customerid
            }]
            return JsonResponse(response, safe=False)
        else:
            return HttpResponse(form.errors)
    else:
        form = DatabaseOperationForm()
        customer_form = CustomerForm()

    return JsonResponse(['not'], safe=False)


def add_new_client(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClientForm(request.POST)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newClientForm = form.save()
            # redirect to a new URL:
            newClient = Client.objects.last()
            response = [{
                "response": 'New Client Added',
                "clientName": newClient.clientname,
                "clientID": newClient.clientid
            }]
            return JsonResponse(response, safe=False)
        else:
            return HttpResponse(form.errors)
    else:
        form = DatabaseOperationForm()
        client_form = ClientForm()

    return JsonResponse(['not'], safe=False)


def add_new_split_amount(request):
    amounts = request.GET.getlist('amounts[]')
    remarks = request.GET.getlist('remarks[]')
    dboID = Table1.objects.get(id=request.GET.get('dboID'))
    type = request.GET.get('type')

    SplitAmounts.objects.filter(dboid=dboID, type=type).delete()

    for x in range(0, len(amounts)):
        splitAmount = SplitAmounts(dboid=dboID, type=type, amount=amounts[x], remarks=remarks[0])
        splitAmount.save()

    return JsonResponse([], safe=False)


def get_split_amount(request):
    dboID = request.GET.get('dboID')
    type = request.GET.get('type')

    amounts = []

    splitAmounts = SplitAmounts.objects.filter(dboid=dboID, type=type)

    for splitAmount in splitAmounts:
        amounts.append({
            'splitAmountID': splitAmount.splitamountid,
            'amount': splitAmount.amount,
            'remarks': splitAmount.remarks,
        })

    return JsonResponse(amounts, safe=False)


def get_split_amount_total(request):
    dboID = request.GET.get('dboID')
    type = request.GET.get('type')

    splitAmounts = SplitAmounts.objects.filter(dboid=dboID, type=type)

    total = 0
    for splitAmount in splitAmounts:
        total += splitAmount.amount

    return JsonResponse(total, safe=False)


def delete_split_amount(request):
    splitAmountID = request.GET.get('splitAmountID')

    SplitAmounts.objects.filter(splitamountid=splitAmountID).delete()

    return JsonResponse([], safe=False)
