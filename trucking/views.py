import xlrd, json
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import JsonResponse
from .forms import *
from datetime import datetime
from django.contrib import messages
from django.db.models import Sum
from datetime import date



def index(request):
    return render(request, 'index.html',)


def testing(request):
    users_list = Userinformation.objects.all()

    return render(request, 'testingDataTable.html', {'users_list': users_list})


def database_operations(request):
    if request.method == "GET":
        try:
            latest = Table1.objects.latest('date')
            latest_date = latest.date
            clients = Client.objects.all().order_by('clientname')
            list = Table1.objects.filter(date__year=latest_date.year, date__month=latest_date.month)[:50]
        except:
            latest = datetime.now()
            latest_date = latest.date
            clients = Client.objects.all().order_by('clientname')
            list = Table1.objects.filter(date__year=latest.year, date__month=latest.month)

        dates = Table1.objects.dates('date', 'month')

        customers = Customer.objects.all().order_by('customername')

        years = []

        for date in dates:
            if not date.year in years:
                years.append(date.year)


        if len(dates) != 0:
            context = {
                'list': list,
                'clients': clients,
                'customers': customers,
                'latest_date': latest_date,
                'dates': dates,
                'month': latest_date.month,
                'year': latest_date.year,
                'years': years
            }
        else:
            context = {
                'list': list,
                'clients': clients,
                'customers': customers,
                'latest_date': latest_date,
                'dates': dates,
                'month': 0,
                'year': 0,
                'years': years
            }

        return render(request, 'databaseOperations.html', context)

    csv_file = request.FILES['file']

    book = xlrd.open_workbook(file_contents=csv_file.read())
    sheet = book.sheet_by_index(0)

    for r in range(1,sheet.nrows):
        x = str(int(sheet.cell(r, 0).value)).lstrip("0")
        if int(x) > 2359:
            x = 0
        x = str(x).zfill(4)
        time = x[:2] + ':' + x[2:] + ":00"

        x = int(sheet.cell(r, 1).value)
        date = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + x - 2).date()

        plateno = str(sheet.cell(r, 2).value)
        wbno = str(sheet.cell(r, 3).value).replace('.0', '')
        origin = str(sheet.cell(r, 4).value)
        destination = str(sheet.cell(r, 5).value)

        driver = str(sheet.cell(r, 6).value)
        if not Driver.objects.filter(drivername=driver).exists():
            id = Driver.objects.count() + 1
            newDriver = Driver(
                driverid=id,
                drivername=driver
            )
            newDriver.save()
            driver = newDriver
        else:
            existingDriver = Driver.objects.get(drivername=driver)
            driver = existingDriver

        helper = str(sheet.cell(r, 7).value)
        if helper == '':
            helper = None
        else:
            if not Helper.objects.filter(helpername=helper).exists():
                id = Helper.objects.count() + 1
                newHelper = Helper(
                    helperid=id,
                    helpername=helper
                )
                newHelper.save()
                helper = newHelper
            else:
                existingHelper = Helper.objects.get(helpername=helper)
                helper = existingHelper

        client = str(sheet.cell(r, 8).value)
        if not Client.objects.filter(clientname=client).exists():
            id = Client.objects.count() + 1
            newClient = Client(
                clientid=id,
                clientname=client
            )
            newClient.save()
            client = newClient
        else:
            existingClient = Client.objects.get(clientname=client)
            client = existingClient

        customer = str(sheet.cell(r, 9).value)
        if not Customer.objects.filter(customername=customer).exists():
            id = Customer.objects.count() + 1
            newCustomer = Customer(
                customerid=id,
                customername=customer
            )
            newCustomer.save()
            customer = newCustomer
        else:
            existingCustomer = Customer.objects.get(customername=customer)
            customer = existingCustomer

        trucktype = str(sheet.cell(r, 10).value)
        qty = str(sheet.cell(r, 11).value)
        remarks = str(sheet.cell(r, 12).value)

        diesel = sheet.cell(r, 13).value
        truckbudget = sheet.cell(r, 14).value
        cahelper = sheet.cell(r, 15).value
        entryfee = sheet.cell(r, 16).value
        parking = sheet.cell(r, 17).value
        tollfee = sheet.cell(r, 18).value
        others = sheet.cell(r, 19).value
        liq = sheet.cell(r, 20).value
        unliq = sheet.cell(r, 21).value
        driversal = sheet.cell(r, 22).value
        helpersal = sheet.cell(r, 23).value
        driveraddl = sheet.cell(r, 24).value
        helperaddl = sheet.cell(r, 25).value
        billing = sheet.cell(r, 26).value
        addl = sheet.cell(r, 27).value
        revenue = sheet.cell(r, 28).value

        if diesel == '':
            diesel = None
        if truckbudget == '':
            truckbudget = None
        if cahelper == '':
            cahelper = None
        if entryfee == '':
            entryfee = None
        if parking == '':
            parking = None
        if tollfee == '':
            tollfee = None
        if others == '':
            others = None
        if liq == '':
            liq = None
        if unliq == '':
            unliq = None
        if driversal == '':
            driversal = None
        if helpersal == '':
            helpersal = None
        if driveraddl == '':
            driveraddl = None
        if helperaddl == '':
            helperaddl = None
        if billing == '':
            billing = None
        if addl == '':
            addl = None
        if revenue == '':
            revenue = None

        if sheet.cell(r, 29).value != '' and sheet.cell(r, 29).value != "N/A":
            x = int(sheet.cell(r, 29).value)
            billeddate = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + x - 2).date()
        else:
            billeddate = None

        receivedby = sheet.cell(r, 30).value

        if receivedby == '':
            receivedby = None

        if sheet.cell(r, 31).value != '':
            x = str(int(sheet.cell(r, 31).value)).lstrip("0")
            if int(x) > 2359:
                x = 0
            x = str(x).zfill(4)
            receivedtime = x[:2] + ':' + x[2:] + ":00"
        else:
            receivedtime = None

        newOperation = Table1(
            date=date,
            calltime=time,
            plateno=plateno,
            wbno=wbno,
            origin=origin,
            destination=destination,
            driver=driver,
            helper=helper,
            customer=customer,
            client=client,
            trucktype=trucktype,
            qty=qty,
            remarks=remarks,
            diesel=diesel,
            truckbudget=truckbudget,
            cahelper=cahelper,
            tollfee=tollfee,
            parking=parking,
            entryfee=entryfee,
            others=others,
            totalliq=liq,
            unliq=unliq,
            driversal=driversal,
            addldriversal=driveraddl,
            helpersal=helpersal,
            addlhelpersal=helperaddl,
            billing=billing,
            addl=addl,
            revenue=revenue,
            billeddate=billeddate,
            receivedby=receivedby,
            receivedtime=receivedtime
        )

        newOperation.save()

    latest = Table1.objects.latest('date')
    latest_date = latest.date
    clients = Client.objects.all().order_by('clientname')
    customers = Customer.objects.all().order_by('customername')
    list = Table1.objects.filter(date__year=latest_date.year, date__month=latest_date.month)

    dates = Table1.objects.dates('date', 'month')

    years = []

    for date in dates:
        if not date.year in years:
            years.append(date.year)

    context = {
        'list': list,
        'clients': clients,
        'customers': customers,
        'latest_date': latest_date,
        'dates': dates,
        'month': latest_date.month,
        'year': latest_date.year,
        'years': years
    }

    messages.success(request, 'Import successful (' + str(sheet.nrows - 1) + ' rows)')
    return render(request, 'databaseOperations.html', context)


def database_operations_year_month(request, year, month, day):
    if request.method == "GET":
        latest = Table1.objects.latest('date')
        latest_date = latest.date
        clients = Client.objects.all().order_by('clientname')
        customers = Customer.objects.all().order_by('customername')
        if day == 0:
            list = Table1.objects.filter(date__year=year, date__month=month)
        else:
            list = Table1.objects.filter(date__year=year, date__month=month, date__day=day)

        dates = Table1.objects.dates('date', 'month')

        years = []

        for date in dates:
            if not date.year in years:
                years.append(date.year)

        context = {
            'list': list,
            'clients': clients,
            'customers': customers,
            'latest_date': latest_date,
            'dates': dates,
            'month': month,
            'year': year,
            'day': day,
            'years': years
        }

        return render(request, 'databaseOperations.html', context)


def new_database_operation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DatabaseOperationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newDatabaseOperation = form.save()
            # redirect to a new URL:
            #return redirect('edit_database_operation', id=Table1.objects.last().id, phase="B")
            return redirect('database_operations')
        else:
            return HttpResponse(form.errors)
    else:
        form = DatabaseOperationForm()
        driver_form = DriverForm()
        customer_form = CustomerForm()
        client_form = ClientForm()
        helper_form = HelperForm()
        extra = -1
        persons = Table1.objects.values_list('receivedby').order_by('receivedby')
        receivedBy = []
        for person in persons:
            if person[0] not in receivedBy and person[0] is not None:
                receivedBy.append(person[0])

        words = Table1.objects.values_list('remarks').order_by('remarks')
        remarks = []
        for word in words:
            if word[0] not in remarks and word[0] is not None:
                remarks.append(word[0])

        return render(request, 'forms/databaseOperationForm.html', {'form': form,
                                                              'extra': extra,
                                                              'driver_form': driver_form,
                                                              'customer_form': customer_form,
                                                              'client_form': client_form,
                                                              'helper_form': helper_form,
                                                              'receivedBy': receivedBy,
                                                              'remarks': remarks,
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

        persons = Table1.objects.values_list('receivedby').order_by('receivedby')
        receivedBy = []
        for person in persons:
            if person[0] not in receivedBy and person[0] is not None:
                receivedBy.append(person[0])

        words = Table1.objects.values_list('remarks').order_by('remarks')
        remarks = []
        for word in words:
            if word[0] not in remarks and word[0] is not None:
                remarks.append(word[0])

    return render(request, 'forms/databaseOperationForm.html', {'form': form,
                                                          'extra': extra,
                                                          'driver_form': driver_form,
                                                          'customer_form': customer_form,
                                                          'client_form': client_form,
                                                          'receivedBy': receivedBy,
                                                          'remarks': remarks,
                                                          'phase': phase})


def delete_database_operation(request, id):
    latest = Table1.objects.latest('date')
    latest_date = latest.date
    list = Table1.objects.filter(date__year=latest_date.year, date__month=latest_date.month)

    Table1.objects.get(id=id).delete()
    extra = "Database Operation " + str(id) + " Deleted"

    return render(request, 'databaseOperations.html', {'list': list, 'extra': extra})


def dbo_statement_of_account(request):
    billingFromDate = request.POST.get("billingFromDate")
    billingToDate = request.POST.get("billingToDate")
    client = Client.objects.get(clientid=request.POST.get("client"))
    customer = request.POST.get("customer")
    plateNumber = request.POST.get("plateNumber")
    wayBillNumber = request.POST.get("wayBillNumber")
    truckType = request.POST.get("truckType")

    billingFromDate = datetime.strptime(billingFromDate, '%Y-%m-%d').date()
    billingToDate = datetime.strptime(billingToDate, '%Y-%m-%d').date()

    list = Table1.objects.filter(date__gte=billingFromDate, date__lte=billingToDate, client=client, billeddate__isnull=True)

    if customer != '':
        customer = Customer.objects.get(customerid=request.POST.get("customer"))
        list = list.filter(customer=customer)
    else:
        customer = None

    if plateNumber != '':
        list = list.filter(plateno=plateNumber)
    else:
        plateNumber = None

    if wayBillNumber != '':
        list = list.filter(wbno=wayBillNumber)
    else:
        wayBillNumber = None

    if truckType != '':
        list = list.filter(trucktype=truckType)
    else:
        truckType = None

    subtotal = list.aggregate(Sum('billing'))
    addltotal = list.aggregate(Sum('addl'))

    if subtotal['billing__sum'] is not None:
        if addltotal['addl__sum'] is not None:
            grandtotal = subtotal['billing__sum'] + addltotal['addl__sum']
        else:
            grandtotal = subtotal['billing__sum']
    else:
        grandtotal = None

    clients = Client.objects.all().order_by('clientname')
    customers = Customer.objects.all().order_by('customername')

    context = {
        "billedFromDate": billingFromDate,
        "billingToDate": billingToDate,
        "client": client,
        "customer": customer,
        "plateNumber": plateNumber,
        "wayBillNumber": wayBillNumber,
        "truckType": truckType,
        "list": list,
        "clients": clients,
        "customers": customers,
        "subtotal": subtotal,
        "addltotal": addltotal,
        "grandtotal": grandtotal,
    }

    return render(request, 'generateStatementOfAccount.html', context)


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


def add_new_helper(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HelperForm(request.POST)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            newHelperForm = form.save()
            # redirect to a new URL:
            newHelper = Helper.objects.last()
            response = [{
                "response": 'New Helper Added',
                "helperName": newHelper.helpername,
                "helperID": newHelper.helperid
            }]
            return JsonResponse(response, safe=False)
        else:
            return HttpResponse(form.errors)
    else:
        form = DatabaseOperationForm()
        helper_form = HelperForm()

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


def get_dbo(request):
    draw = request.GET.get('draw')
    start = request.GET.get('start')
    length = request.GET.get('length')
    search = request.GET.get('search')

    print(length)

    list = Table1.objects.all()

    data = []
    for operation in list:
        try:
            date = operation.date.strftime("%d-%b-%y")
        except:
            date = ''
        try:
            calltime = operation.calltime.strftime("%-H%M")
        except:
            calltime = ''
        try:
            billeddate = operation.billeddate.strftime("%d-%b-%y")
        except:
            billeddate = ''
        try:
            receivedtime = operation.receivedtime.strftime("%-H%M")
        except:
            receivedtime = ''

        data.append([
            operation.id,
            date,
            calltime,
            operation.plateno or '',
            operation.wbno or '',
            operation.origin or '',
            operation.destination or '',
            operation.driver.drivername or '',
            operation.helper.helpername or '',
            operation.client.clientname or '',
            operation.customer.customername or '',
            operation.trucktype or '',
            operation.qty or '',
            operation.remarks or '',
            operation.diesel or '',
            operation.truckbudget or '',
            operation.cahelper or '',
            operation.entryfee or '',
            operation.parking or '',
            operation.tollfee or '',
            operation.others or '',
            operation.totalliq or '',
            operation.unliq or '',
            operation.driversal or '',
            operation.helpersal or '',
            operation.addldriversal or '',
            operation.addlhelpersal or '',
            operation.billing or '',
            operation.addl or '',
            operation.revenue or '',
            billeddate,
            operation.receivedby or '',
            receivedtime,
        ])

    json_test = json.dumps({
        "draw": draw,
        "recordsTotal": Table1.objects.all().count(),
        "recordsFiltered": list.count(),
        "data": data
    })

    return HttpResponse(json_test, content_type="application/json")


def update_billing_dates(request):
    dboIDs = request.GET.getlist('dboIDs[]')

    for id in dboIDs:
        row = Table1.objects.get(id=id)
        row.billeddate = date.today()
        row.save()

    return JsonResponse([], safe=False)


def get_client(request):
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')

    clientsObjects = []

    dbo = Table1.objects.filter(billeddate__isnull=True, receivedby__isnull=False, date__gte=startDate, date__lte=endDate)

    for record in dbo:
        if not record.client in clientsObjects:
            clientsObjects.append(record.client)

    clients = []

    for client in clientsObjects:
        clients.append({
            "id": client.clientid,
            "name": client.clientname,
        })

    return JsonResponse(clients, safe=False)


def get_customer(request):
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')
    client = Client.objects.get(clientid=request.GET.get('client'))

    customersObjects = []

    dbo = Table1.objects.filter(billeddate__isnull=True, receivedby__isnull=False, date__gte=startDate, date__lte=endDate, client=client)

    for record in dbo:
        if not record.customer in customersObjects:
            customersObjects.append(record.customer)

    customers = []

    for customer in customersObjects:
        customers.append({
            "id": customer.customerid,
            "name": customer.customername,
        })

    return JsonResponse(customers, safe=False)


def get_plate_number(request):
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')
    client = Client.objects.get(clientid=request.GET.get('client'))

    plateNumbers = []

    dbo = Table1.objects.filter(billeddate__isnull=True, receivedby__isnull=False, date__gte=startDate, date__lte=endDate, client=client)

    for record in dbo:
        if not record.plateno in plateNumbers:
            plateNumbers.append(record.plateno)

    return JsonResponse(plateNumbers, safe=False)


def get_way_bill_number(request):
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')
    client = Client.objects.get(clientid=request.GET.get('client'))

    wayBillNumbers = []

    dbo = Table1.objects.filter(billeddate__isnull=True, receivedby__isnull=False, date__gte=startDate, date__lte=endDate, client=client)

    for record in dbo:
        if not record.wbno in wayBillNumbers:
            wayBillNumbers.append(record.wbno)

    return JsonResponse(wayBillNumbers, safe=False)


def get_truck_type(request):
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')
    client = Client.objects.get(clientid=request.GET.get('client'))

    truckTypes = []

    dbo = Table1.objects.filter(billeddate__isnull=True, receivedby__isnull=False, date__gte=startDate, date__lte=endDate, client=client)

    for record in dbo:
        if not record.trucktype in truckTypes:
            truckTypes.append(record.trucktype)

    return JsonResponse(truckTypes, safe=False)


