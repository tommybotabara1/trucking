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
            'calltime': TimeInput(attrs={'type': 'time', 'class': 'form-control A'}),
            'date': DateInput(attrs={'type': 'date', 'class': 'form-control A'}),
            'origin': TextInput(attrs={'class': 'form-control A', 'maxlength': "30", 'list': 'destinations'}),
            'destination': TextInput(attrs={'class': 'form-control A', 'maxlength': "30", 'list': 'destinations'}),
            'client': Select(attrs={'class': 'form-control A'}),
            'customer': Select(attrs={'class': 'form-control A'}),
            'remarks': Textarea(attrs={'class': 'form-control A', 'maxlength': "50"}),
            'plateno': TextInput(attrs={'class': 'form-control', 'maxlength': "10"}),
            'wbno': TextInput(attrs={'class': 'form-control', 'maxlength': "10"}),
            'driver': Select(attrs={'class': 'form-control'}),
            'helper': TextInput(attrs={'class': 'form-control'}),
            'trucktype': Select(attrs={'class': 'form-control', 'maxlength': "30"}),
            'qty': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'driversal': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'helpersal': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'receivedby': TextInput(attrs={'class': 'form-control'}),
            'receiveddatetime': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'totalliq': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0", "readonly": "true"}),
            'addl': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'addldriversal': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'billing': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'diesel': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'truckbudget': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'cahelper': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0"}),
            'tollfee': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0", "readonly": "true"}),
            'parking': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0", "readonly": "true"}),
            'entryfee': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0", "readonly": "true"}),
            'others': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0", "readonly": "true"}),
            'unliq': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0", "readonly": "true"}),
            'revenue': NumberInput(attrs={'class': 'form-control', 'step': ".01", "placeholder": "0.00", "max": "999999999999999", "min": "0", "readonly": "true"}),
            'billeddate': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {

            'plateno': "Plate number",
            'calltime': "Call Time",
            'wbno': "WayBill number",
            'trucktype': "Truck Type",
            'qty': "Quantity",
            'truckbudget': "Truck Budget",
            'cahelper': "Additional Helper Salary",
            'tollfee': "Toll Fee",
            'entryfee': "Entry Fee",
            'driversal': "Driver Salary",
            'helpersal': "Helper Salary",
            'addl': "Billing Additional",
            'billeddate': "Billed Date",
            'receivedby': "Received By",
            'receiveddatetime': "Received Time",
            'addldriversal': "Additional Driver Salary",
            'totalliq': "Total Liquidation",
            'unliq': "Total Unliquidated",
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        driver_values = Driver.objects.all().values_list('driverid', 'drivername')

        driver_choices = [('', '----------')]

        for dic in driver_values:
            driver_choices.append((int(dic[0]), dic[1]))

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


def bound_form(request, id):
    item = get_object_or_404(Table1, id=id)
    form = DatabaseOperationForm(instance=item)
    return render_to_response('bounded_form.html', {'form': form})


