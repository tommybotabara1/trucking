from django import forms
from django.forms import *
from .models import *
from django.shortcuts import get_object_or_404, render_to_response


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'clientid': NumberInput(attrs={'type': 'hidden', 'value': Client.objects.count() + 1}),
            'clientname': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
        }
        labels = {
            'clientname': "Client Name",
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['clientid'].initial = Client.objects.count() + 1


class HelperForm(ModelForm):
    class Meta:
        model = Helper
        fields = '__all__'
        widgets = {
            'helperid': NumberInput(attrs={'type': 'hidden', 'value': Helper.objects.count() + 1}),
            'helpername': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
        }
        labels = {
            'helpername': "Helper Name",
        }

    def __init__(self, *args, **kwargs):
        super(HelperForm, self).__init__(*args, **kwargs)
        self.fields['helperid'].initial = Helper.objects.count() + 1


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'customerid': NumberInput(attrs={'type': 'hidden', 'value': Customer.objects.count() + 1}),
            'customername': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
        }
        labels = {
            'customername': "Customer Name",
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['customerid'].initial = Customer.objects.count() + 1


class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        widgets = {
            'driverid': NumberInput(attrs={'type': 'hidden', 'value': Driver.objects.count() + 1}),
            'drivername': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'phonenumber': TextInput(attrs={'class': 'form-control', 'maxlength': "10"}),
            'sss': TextInput(attrs={'class': 'form-control', 'maxlength': "20"}),
            'taxid': TextInput(attrs={'class': 'form-control', 'maxlength': "20"}),
        }
        labels = {
            'drivername': "Driver Name",
            'phonenumber': "Phone Number",
            'sss': "SSS",
            'taxid': "Tax ID",
        }

    def __init__(self, *args, **kwargs):
        super(DriverForm, self).__init__(*args, **kwargs)
        self.fields['driverid'].initial = Driver.objects.count() + 1


class UserInformationForm(ModelForm):
    class Meta:
        model = Userinformation
        fields = '__all__'
        widgets = {
            'userid': NumberInput(attrs={'type': 'hidden', 'value': Userinformation.objects.count() + 1}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'role': TextInput(attrs={'class': 'form-control'}),
            'employeeid': TextInput(attrs={'class': 'form-control'}),
            'phonenumber': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'employeeid': "Employee ID",
            'phonenumber': "Phone Number",
        }


class TestTableModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.display_field


class DatabaseOperationForm(ModelForm):
    class Meta:
        model = Table1
        fields = '__all__'
        widgets = {
            'id': NumberInput(attrs={'type': 'hidden', 'value': Table1.objects.count() + 1}),
            'calltime': TimeInput(attrs={'type': 'text', 'class': 'form-control A', "placeholder": "HH:MM:SS", "maxlength": "8"}),
            'date': DateInput(attrs={'type': 'date', 'class': 'form-control A'}),
            'origin': TextInput(attrs={'class': 'form-control A', 'maxlength': "30", 'list': 'destinations'}),
            'destination': TextInput(attrs={'class': 'form-control A', 'maxlength': "30", 'list': 'destinations'}),
            'customer': Select(attrs={'class': 'form-control A'}),
            'client': Select(attrs={'class': 'form-control A'}),
            'remarks': TextInput(attrs={'class': 'form-control A', 'maxlength': "50", "list": "remarks"}),
            'plateno': TextInput(attrs={'class': 'form-control', 'maxlength': "10"}),
            'wbno': TextInput(attrs={'class': 'form-control', 'maxlength': "10"}),
            'driver': Select(attrs={'class': 'form-control'}),
            'helper': Select(attrs={'class': 'form-control'}),
            'trucktype': Select(attrs={'class': 'form-control', 'maxlength': "30"}),
            'qty': TextInput(attrs={'class': 'form-control', 'maxlength': "20"}),
            'driversal': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999",}),
            'helpersal': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999",}),
            'receivedby': TextInput(attrs={'class': 'form-control', 'list': 'receivedBy'}),
            'receivedtime': TimeInput(attrs={'type': 'text', 'class': 'form-control A', "placeholder": "HH:MM:SS", "maxlength": "8"}),
            'totalliq': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "readonly": "true"}),
            'addl': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999",}),
            'addldriversal': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999",}),
            'addlhelpersal': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999",}),
            'billing': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999",}),
            'diesel': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999",}),
            'truckbudget': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999",}),
            'cahelper': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", }),
            'tollfee': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", }),
            'parking': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", }),
            'entryfee': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", }),
            'others': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", }),
            'unliq': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999",  }),
            'revenue': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "readonly": "true"}),
            'billeddate': DateInput(attrs={'type': 'date', 'class': 'form-control', "readonly": "true"}),
        }
        labels = {

            'plateno': "Plate number",
            'calltime': "Call Time",
            'wbno': "WayBill number",
            'trucktype': "Truck Type",
            'qty': "Quantity",
            'truckbudget': "Truck Budget",
            'cahelper': "CA Helper",
            'tollfee': "Toll Fee",
            'entryfee': "Entry Fee",
            'driversal': "Driver Salary",
            'helpersal': "Helper Salary",
            'addl': "Billing Additional",
            'billeddate': "Billed Date",
            'receivedby': "Received By",
            'receivedtime': "Received Time",
            'addldriversal': "Additional Driver Salary",
            'addlhelpersal': "Additional Helper Salary",
            'totalliq': "Total Liquidation",
            'unliq': "Total Unliquidated",
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        driver_values = Driver.objects.all().values_list('driverid', 'drivername')

        driver_choices = [('', '----------')]

        for dic in driver_values:
            driver_choices.append((int(dic[0]), dic[1]))

        helper_values = Helper.objects.all().values_list('helperid', 'helpername')

        helper_choices = [('', '----------')]

        for dic in helper_values:
            helper_choices.append((int(dic[0]), dic[1]))

        customer_values = Customer.objects.all().values_list('customerid', 'customername')

        customer_choices = [('', '----------')]

        for dic in customer_values:
            customer_choices.append((int(dic[0]), dic[1]))

        client_values = Client.objects.all().values_list('clientid', 'clientname')

        client_choices = [('', '----------')]

        for dic in client_values:
            client_choices.append((int(dic[0]), dic[1]))

        self.fields['driver'].choices = driver_choices
        self.fields['customer'].choices = customer_choices
        self.fields['client'].choices = client_choices
        self.fields['helper'].choices = helper_choices


class TariffForm(ModelForm):
    class Meta:
        model = Tariff
        fields = '__all__'
        widgets = {
            'tariffid': NumberInput(attrs={'type': 'hidden', 'value': Tariff.objects.count() + 1}),
            'airdestination': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'airdriver46wheeler': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'airhelper46wheeler': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'airdriver6forwarder': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'airhelper6forwarder': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'airdriver10wheeler': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'airhelper10wheeler': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'seadestination': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'seadriver46wheeler': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'seahelper46wheeler': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'seadriver6forwarder': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'seahelper6forwarder': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'seadriver10wheeler': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'seahelper10wheeler': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
        }
        labels = {
            'airdestination': "Air Destination",
            'airdriver46wheeler': "Air Driver 46 Wheeler",
            'airhelper46wheeler': "Air Helper 46 Wheeler",
            'airdriver6forwarder': "Air Driver 6 Forwarder",
            'airhelper6forwarder': "Air Helper 6 Forwarder",
            'airdriver10wheeler': "Air Driver 10 Wheeler",
            'airhelper10wheeler': "Air Helper 10 Wheeler",
            'seadestination': "Sea Destination",
            'seadriver46wheeler': "Sea Driver 46 Wheeler",
            'seahelper46wheeler': "Sea Helper 46 Wheeler",
            'seadriver6forwarder': "Sea Driver 6 Forwarder",
            'seahelper6forwarder': "Sea Helper 6 Forwarder",
            'seadriver10wheeler': "Sea Driver 10 Wheeler",
            'seahelper10wheeler': "Sea Helper 10 Wheeler",
        }


class TruckBudgetForm(ModelForm):
    class Meta:
        model = TruckBudget
        fields = '__all__'
        widgets = {
            'truckbudgetid': NumberInput(attrs={'type': 'hidden', 'value': TruckBudget.objects.count() + 1}),
            'traveldate': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'amount': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'particulars': Textarea(attrs={'class': 'form-control A', 'maxlength': "50"}),
            'for_field': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'client': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'purchaseorderor': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'liquidated': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'unliquidated': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
        }
        labels = {
            'traveldate': "Travel Date",
            'for_field': "For",
            'purchaseorderor': "Purchase Order OR",
        }


class StatementOfAccountForm(ModelForm):
    class Meta:
        model = StatementOfAccount
        fields = '__all__'
        widgets = {
            'statementofaccountid': NumberInput(attrs={'type': 'hidden', 'value': StatementOfAccount.objects.count() + 1}),
            'month': TextInput(attrs={'class': 'form-control', 'maxlength': "15"}),
            'soano': TextInput(attrs={'class': 'form-control', 'maxlength': "15"}),
            'customer': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'particulars': Textarea(attrs={'class': 'form-control A', 'maxlength': "50"}),
            'invoicedate': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'invoicereceivedate': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'receivedby': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'totalsales': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'arno': TextInput(attrs={'class': 'form-control', 'maxlength': "15"}),
            'paidamount': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'datepaid': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'variancediff': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'accountstitle': TextInput(attrs={'class': 'form-control', 'maxlength': "50"}),
            'remarks': Textarea(attrs={'class': 'form-control A', 'maxlength': "50"}),
        }
        labels = {
            'soano': "SOA No",
            'invoicedate': "Invoice Date",
            'invoicereceivedate': "Invoice Received Date",
            'receivedby': "Received by",
            'totalsales': "Total Sales",
            'arno': "AR No",
            'paidamount': "Paid Amount",
            'datepaid': "Date Paid",
            'variancediff': "Variance Diff",
            'accountstitle': "Accounts Title",
        }


class DirectPayrollForm(ModelForm):
    class Meta:
        model = DirectPayroll
        fields = '__all__'
        widgets = {
            'directpayrollid': NumberInput(attrs={'type': 'hidden', 'value': DirectPayroll.objects.count() + 1}),
            'employeeno': NumberInput(attrs={'class': 'form-control', 'step': "1", "max": "999999999999999", "min": "0"}),
            'name': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'commission': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'othercommadditional': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'othercommadjustment': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'grosspay': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'netpay': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'rate': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999", "min": "0"}),
            'incentives': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'takehomepay': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
        }
        labels = {
            'employeeno': "Employee No",
            'othercommadditional': "Other Commission Additional",
            'othercommadjustment': "Other Commission Adjustment",
            'grosspay': "Gross Pay",
            'netpay': "Net Pay",
            'takehomepay': "Take Home Pay",
        }


class BreakdownForm(ModelForm):
    class Meta:
        model = Breakdown
        fields = '__all__'
        widgets = {
            'breakdownid': NumberInput(attrs={'type': 'hidden', 'value': Breakdown.objects.count() + 1}),
            'breakdowndate': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'platenumber': TextInput(attrs={'class': 'form-control', 'maxlength': "10"}),
            'waybillno': TextInput(attrs={'class': 'form-control', 'maxlength': "10"}),
            'customer': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'client': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'cashadvance': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'totalliq': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'unliquidated': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'salary': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
        }
        labels = {
            'breakdowndate': "Breakdown Date",
            'platenumber': "Plate Number",
            'waybillno': "Way Bill No",
            'cashadvance': "Cash Advance",
            'totalliq': "Total Liquidation",
            'unliquidated': "Total Unliquidated"
        }


class CanteenForm(ModelForm):
    class Meta:
        model = Canteen
        fields = '__all__'
        widgets = {
            'canteenid': NumberInput(attrs={'type': 'hidden', 'value': Canteen.objects.count() + 1}),
            'payrollperiodform': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'payrollperiodto': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'employeename': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'takehomepay': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'canteenname': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'baraks': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'others': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'coopsavings': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'cooploan': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'coopcp': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'cooprice': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'actualsalary': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
        }
        labels = {
            'payrollperiodform': "Payroll Period From",
            'payrollperiodto': "Payroll Period To",
            'employeename': "Employee Name",
            'takehomepay': "Take Home Pay",
            'canteenname': "Canteen Name",
            'coopsavings': "Coop Savings",
            'cooploan': "Coop Loan",
            'coopcp': "Coop CP",
            'cooprice': "Coop Price",
            'actualsalary': "Actual Salary"
        }


class DamagesForm(ModelForm):
    class Meta:
        model = Damages
        fields = '__all__'
        widgets = {
            'damagesid': NumberInput(attrs={'type': 'hidden', 'value': Damages.objects.count() + 1}),
            'employeename': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'typeofdamage': TextInput(attrs={'class': 'form-control', 'maxlength': "30"}),
            'personalcashadv': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'cadate': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'employeename': "Employee Name",
            'typeofdamage': "Type of Damage",
            'personalcashadv': "Personal Cash Adv",
            'cadate': "CA Date",
        }

def bound_form(request, id):
    item = get_object_or_404(Table1, id=id)
    form = DatabaseOperationForm(instance=item)
    return render_to_response('bounded_form.html', {'form': form})


