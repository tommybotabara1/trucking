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
        return render(request, 'forms/databaseOperationForm.html', {'form': form,
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

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            newDatabaseOperation = form.save()
            # redirect to a new URL:
            list = Table1.objects.all()
            return redirect('database_operations')
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

    return render(request, 'forms/databaseOperationForm.html', {'form': form,
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


def tariff(request):
    list = Tariff.objects.all()
    return render(request, 'tariff.html', {'list': list})


def new_tariff(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TariffForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('tariff')
        else:
            return HttpResponse(form.errors)
    else:
        form = TariffForm()
        extra = -1
        return render(request, 'forms/tariffForm.html', {'form': form,
                                                                    'extra': extra
                                                                    })


def edit_tariff(request, id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        a = Tariff.objects.get(tariffid=id)
        form = TariffForm(request.POST, instance=a)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('tariff')
        else:
            return HttpResponse(form.errors)
    else:
        a = Tariff.objects.get(tariffid=id)
        form = TariffForm(instance=a)
        extra = id

    return render(request, 'forms/tariffForm.html', {'form': form,
                                                          'extra': extra,})


def delete_tariff(request, id):
    list = Tariff.objects.all()

    Tariff.objects.get(tariffid=id).delete()
    extra = "Tariff " + str(id) + " Deleted"

    return render(request, 'tariff.html', {'list': list, 'extra': extra})


def truck_budget(request):
    list = TruckBudget.objects.all()
    return render(request, 'truckBudget.html', {'list': list})


def new_truck_budget(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TruckBudgetForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('truck_budget')
        else:
            return HttpResponse(form.errors)
    else:
        form = TruckBudgetForm()
        extra = -1
        return render(request, 'forms/truckBudgetForm.html', {'form': form,
                                                                    'extra': extra
                                                                    })


def edit_truck_budget(request, id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        a = TruckBudget.objects.get(truckbudgetid=id)
        form = TruckBudgetForm(request.POST, instance=a)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('truck_budget')
        else:
            return HttpResponse(form.errors)
    else:
        a = TruckBudget.objects.get(truckbudgetid=id)
        form = TruckBudgetForm(instance=a)
        extra = id

    return render(request, 'forms/truckBudgetForm.html', {'form': form,
                                                          'extra': extra,})


def delete_truck_budget(request, id):
    list = TruckBudget.objects.all()

    TruckBudget.objects.get(truckbudgetid=id).delete()
    extra = "Truck Budget " + str(id) + " Deleted"

    return render(request, 'truckBudget.html', {'list': list, 'extra': extra})


def statement_of_account(request):
    list = StatementOfAccount.objects.all()
    return render(request, 'statementOfAccount.html', {'list': list})


def new_statement_of_account(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StatementOfAccountForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('statement_of_account')
        else:
            return HttpResponse(form.errors)
    else:
        form = StatementOfAccountForm()
        extra = -1
        return render(request, 'forms/statementOfAccountForm.html', {'form': form,
                                                                    'extra': extra
                                                                    })


def edit_statement_of_account(request, id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        a = StatementOfAccount.objects.get(statementofaccountid=id)
        form = StatementOfAccountForm(request.POST, instance=a)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('statement_of_account')
        else:
            return HttpResponse(form.errors)
    else:
        a = StatementOfAccount.objects.get(statementofaccountid=id)
        form = StatementOfAccountForm(instance=a)
        extra = id

    return render(request, 'forms/statementOfAccountForm.html', {'form': form,
                                                          'extra': extra,})


def delete_statement_of_account(request, id):
    list = StatementOfAccount.objects.all()

    StatementOfAccount.objects.get(statementofaccountid=id).delete()
    extra = "Statement of Account " + str(id) + " Deleted"

    return render(request, 'statementOfAccount.html', {'list': list, 'extra': extra})


def direct_payroll(request):
    list = DirectPayroll.objects.all()
    return render(request, 'directPayroll.html', {'list': list})


def new_direct_payroll(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DirectPayrollForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('direct_payroll')
        else:
            return HttpResponse(form.errors)
    else:
        form = DirectPayrollForm()
        extra = -1
        return render(request, 'forms/directPayrollForm.html', {'form': form,
                                                                    'extra': extra
                                                                    })


def edit_direct_payroll(request, id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        a = DirectPayroll.objects.get(directpayrollid=id)
        form = DirectPayrollForm(request.POST, instance=a)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('direct_payroll')
        else:
            return HttpResponse(form.errors)
    else:
        a = DirectPayroll.objects.get(directpayrollid=id)
        form = DirectPayrollForm(instance=a)
        extra = id

    return render(request, 'forms/directPayrollForm.html', {'form': form,
                                                          'extra': extra,})


def delete_direct_payroll(request, id):
    list = DirectPayroll.objects.all()

    DirectPayroll.objects.get(directpayrollid=id).delete()
    extra = "Direct Payroll " + str(id) + " Deleted"

    return render(request, 'directPayroll.html', {'list': list, 'extra': extra})


def breakdown(request):
    list = Breakdown.objects.all()
    return render(request, 'breakdown.html', {'list': list})


def new_breakdown(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BreakdownForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('breakdown')
        else:
            return HttpResponse(form.errors)
    else:
        form = BreakdownForm()
        extra = -1
        return render(request, 'forms/breakdownForm.html', {'form': form,
                                                                    'extra': extra
                                                                    })


def edit_breakdown(request, id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        a = Breakdown.objects.get(breakdownid=id)
        form = BreakdownForm(request.POST, instance=a)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('breakdown')
        else:
            return HttpResponse(form.errors)
    else:
        a = Breakdown.objects.get(breakdownid=id)
        form = BreakdownForm(instance=a)
        extra = id

    return render(request, 'forms/breakdownForm.html', {'form': form,
                                                          'extra': extra,})


def delete_breakdown(request, id):
    list = Breakdown.objects.all()

    Breakdown.objects.get(breakdownid=id).delete()
    extra = "Breakdown " + str(id) + " Deleted"

    return render(request, 'breakdown.html', {'list': list, 'extra': extra})


def canteen(request):
    list = Canteen.objects.all()
    return render(request, 'canteen.html', {'list': list})


def new_canteen(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CanteenForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('canteen')
        else:
            return HttpResponse(form.errors)
    else:
        form = CanteenForm()
        extra = -1
        return render(request, 'forms/canteenForm.html', {'form': form,
                                                                    'extra': extra
                                                                    })


def edit_canteen(request, id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        a = Canteen.objects.get(canteenid=id)
        form = CanteenForm(request.POST, instance=a)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('canteen')
        else:
            return HttpResponse(form.errors)
    else:
        a = Canteen.objects.get(canteenid=id)
        form = CanteenForm(instance=a)
        extra = id

    return render(request, 'forms/canteenForm.html', {'form': form,
                                                          'extra': extra,})


def delete_canteen(request, id):
    list = Canteen.objects.all()

    Canteen.objects.get(canteenid=id).delete()
    extra = "Canteen " + str(id) + " Deleted"

    return render(request, 'canteen.html', {'list': list, 'extra': extra})


def damages(request):
    list = Damages.objects.all()
    return render(request, 'damages.html', {'list': list})


def new_damages(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DamagesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('damages')
        else:
            return HttpResponse(form.errors)
    else:
        form = DamagesForm()
        extra = -1
        return render(request, 'forms/damagesForm.html', {'form': form,
                                                                    'extra': extra
                                                                    })


def edit_damages(request, id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        a = Damages.objects.get(damagesid=id)
        form = DamagesForm(request.POST, instance=a)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            return redirect('damages')
        else:
            return HttpResponse(form.errors)
    else:
        a = Damages.objects.get(damagesid=id)
        form = DamagesForm(instance=a)
        extra = id

    return render(request, 'forms/damagesForm.html', {'form': form,
                                                          'extra': extra,})


def delete_damages(request, id):
    list = Damages.objects.all()

    Damages.objects.get(damagesid=id).delete()
    extra = "Damages " + str(id) + " Deleted"

    return render(request, 'damages.html', {'list': list, 'extra': extra})


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
