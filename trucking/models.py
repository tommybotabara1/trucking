# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Breakdown(models.Model):
    breakdownid = models.AutoField(db_column='breakdownID', primary_key=True)  # Field name made lowercase.
    breakdowndate = models.DateField(db_column='breakdownDate', blank=True, null=True)  # Field name made lowercase.
    platenumber = models.CharField(db_column='plateNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    waybillno = models.CharField(db_column='wayBillNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customer = models.CharField(max_length=30, blank=True, null=True)
    client = models.CharField(max_length=30, blank=True, null=True)
    cashadvance = models.FloatField(db_column='cashAdvance', blank=True, null=True)  # Field name made lowercase.
    totalliq = models.FloatField(db_column='totalLiq', blank=True, null=True)  # Field name made lowercase.
    unliquidated = models.FloatField(blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'breakdown'


class Canteen(models.Model):
    canteenid = models.AutoField(db_column='canteenID', primary_key=True)  # Field name made lowercase.
    payrollperiodform = models.DateField(db_column='payRollPeriodForm', blank=True, null=True)  # Field name made lowercase.
    payrollperiodto = models.DateField(db_column='payRollPeriodTo', blank=True, null=True)  # Field name made lowercase.
    employeename = models.CharField(db_column='employeeName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    takehomepay = models.FloatField(db_column='takeHomePay', blank=True, null=True)  # Field name made lowercase.
    canteenname = models.CharField(db_column='canteenName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    baraks = models.CharField(max_length=30, blank=True, null=True)
    others = models.CharField(max_length=30, blank=True, null=True)
    coopsavings = models.FloatField(db_column='coopSavings', blank=True, null=True)  # Field name made lowercase.
    cooploan = models.FloatField(db_column='coopLoan', blank=True, null=True)  # Field name made lowercase.
    coopcp = models.FloatField(db_column='coopCP', blank=True, null=True)  # Field name made lowercase.
    cooprice = models.FloatField(db_column='coopRice', blank=True, null=True)  # Field name made lowercase.
    actualsalary = models.FloatField(db_column='actualSalary', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'canteen'


class Client(models.Model):
    clientid = models.IntegerField(primary_key=True)
    clientname = models.CharField(db_column='clientName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'


class Customer(models.Model):
    customerid = models.IntegerField(primary_key=True)
    customername = models.CharField(db_column='customerName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Damages(models.Model):
    damagesid = models.AutoField(db_column='damagesID', primary_key=True)  # Field name made lowercase.
    employeename = models.CharField(db_column='employeeName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    typeofdamage = models.CharField(db_column='typeOfDamage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    personalcashadv = models.FloatField(db_column='personalCashAdv', blank=True, null=True)  # Field name made lowercase.
    cadate = models.DateField(db_column='caDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'damages'


class DirectPayroll(models.Model):
    directpayrollid = models.AutoField(db_column='directPayrollID', primary_key=True)  # Field name made lowercase.
    employeeno = models.IntegerField(db_column='employeeNo', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=30, blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)
    othercommadditional = models.FloatField(db_column='otherCommAdditional', blank=True, null=True)  # Field name made lowercase.
    othercommadjustment = models.FloatField(db_column='otherCommAdjustment', blank=True, null=True)  # Field name made lowercase.
    grosspay = models.FloatField(db_column='grossPay', blank=True, null=True)  # Field name made lowercase.
    netpay = models.FloatField(db_column='netPay', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(blank=True, null=True)
    incentives = models.FloatField(blank=True, null=True)
    takehomepay = models.FloatField(db_column='takeHomePay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'direct_payroll'


class Driver(models.Model):
    driverid = models.IntegerField(primary_key=True)
    drivername = models.CharField(db_column='driverName', max_length=30)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=10)  # Field name made lowercase.
    sss = models.CharField(db_column='SSS', max_length=20)  # Field name made lowercase.
    taxid = models.CharField(db_column='taxID', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'driver'


TRUCK_TYPE_CHOICES = (
    ('4W', '4W'),
    ('10W', '10W'),
    ('FWD', 'FWD'),
    ('6W', '6W'),
)


class Helper(models.Model):
    helperid = models.IntegerField(db_column='helperID', primary_key=True)  # Field name made lowercase.
    helpername = models.CharField(db_column='helperName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'helper'


class StatementOfAccount(models.Model):
    statementofaccountid = models.AutoField(db_column='statementOfAccountID', primary_key=True)  # Field name made lowercase.
    month = models.CharField(max_length=15, blank=True, null=True)
    soano = models.CharField(db_column='soaNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    customer = models.CharField(max_length=30, blank=True, null=True)
    particulars = models.CharField(max_length=50, blank=True, null=True)
    invoicedate = models.DateField(db_column='invoiceDate', blank=True, null=True)  # Field name made lowercase.
    invoicereceivedate = models.DateField(db_column='invoiceReceiveDate', blank=True, null=True)  # Field name made lowercase.
    receivedby = models.CharField(db_column='receivedBy', max_length=30, blank=True, null=True)  # Field name made lowercase.
    totalsales = models.FloatField(db_column='totalSales', blank=True, null=True)  # Field name made lowercase.
    arno = models.CharField(db_column='arNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    paidamount = models.FloatField(db_column='paidAmount', blank=True, null=True)  # Field name made lowercase.
    datepaid = models.DateField(db_column='datePaid', blank=True, null=True)  # Field name made lowercase.
    variancediff = models.FloatField(db_column='varianceDiff', blank=True, null=True)  # Field name made lowercase.
    accountstitle = models.CharField(db_column='accountsTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statement_of_account'


class Table1(models.Model):
    date = models.DateField(blank=True, null=True)
    calltime = models.TimeField(db_column='callTime', blank=True, null=True)  # Field name made lowercase.
    plateno = models.CharField(db_column='plateNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wbno = models.CharField(db_column='WBNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    origin = models.CharField(max_length=30, blank=True, null=True)
    destination = models.CharField(max_length=30, blank=True, null=True)
    driver = models.ForeignKey(Driver, models.DO_NOTHING, db_column='driver', blank=True, null=True)
    helper = models.ForeignKey(Helper, models.DO_NOTHING, db_column='helper', blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client', blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer', blank=True, null=True)
    trucktype = models.CharField(db_column='truckType', max_length=20, blank=True,
                                 null=True, choices=TRUCK_TYPE_CHOICES)  # Field name made lowercase.
    qty = models.CharField(blank=True, null=True, max_length=20)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    diesel = models.FloatField(blank=True, null=True)
    truckbudget = models.FloatField(db_column='truckBudget', blank=True, null=True)  # Field name made lowe
    cahelper = models.FloatField(db_column='caHelper', blank=True, null=True)  # Field name made lowercase.
    tollfee = models.FloatField(db_column='tollFee', blank=True, null=True)  # Field name made lowercase.
    parking = models.FloatField(blank=True, null=True)
    entryfee = models.FloatField(db_column='entryFee', blank=True, null=True)  # Field name made lowercase.
    others = models.FloatField(blank=True, null=True)
    totalliq = models.FloatField(db_column='totalLiq', blank=True, null=True)  # Field name made lowercase.
    unliq = models.FloatField(blank=True, null=True)
    driversal = models.FloatField(db_column='driverSal', blank=True, null=True)  # Field name made lowercase.
    addldriversal = models.FloatField(db_column='addLDriverSal', blank=True, null=True)  # Field name made lowercase.# rcase.
    helpersal = models.FloatField(db_column='helperSal', blank=True, null=True)  # Field name made lowercase.
    addlhelpersal = models.FloatField(db_column='addLHelperSal', blank=True, null=True)  # Field name made lowercase.
    billing = models.FloatField(blank=True, null=True)
    addl = models.FloatField(db_column='addL', blank=True, null=True)  # Field name made lowercase.
    revenue = models.FloatField(blank=True, null=True)
    billeddate = models.DateField(db_column='billedDate', blank=True, null=True)  # Field name made lowercase.
    receivedby = models.CharField(db_column='receivedBy', max_length=45, blank=True,
                                  null=True)  # Field name made lowercase.
    receivedtime = models.TimeField(db_column='receivedTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table1'


class SplitAmounts(models.Model):
    splitamountid = models.AutoField(db_column='splitAmountID', primary_key=True)  # Field name made lowercase.
    dboid = models.ForeignKey('Table1', models.CASCADE, db_column='dboID')  # Field name made lowercase.
    type = models.CharField(max_length=45)
    amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'split_amounts'


class Tariff(models.Model):
    tariffid = models.AutoField(db_column='tariffID', primary_key=True)  # Field name made lowercase.
    airdestination = models.FloatField(db_column='airDestination', blank=True, null=True)  # Field name made lowercase.
    airdriver46wheeler = models.FloatField(db_column='airDriver46Wheeler', blank=True, null=True)  # Field name made lowercase.
    airhelper46wheeler = models.FloatField(db_column='airHelper46Wheeler', blank=True, null=True)  # Field name made lowercase.
    airdriver6forwarder = models.FloatField(db_column='airDriver6Forwarder', blank=True, null=True)  # Field name made lowercase.
    airhelper6forwarder = models.FloatField(db_column='airHelper6Forwarder', blank=True, null=True)  # Field name made lowercase.
    airdriver10wheeler = models.FloatField(db_column='airDriver10Wheeler', blank=True, null=True)  # Field name made lowercase.
    airhelper10wheeler = models.FloatField(db_column='airHelper10Wheeler', blank=True, null=True)  # Field name made lowercase.
    seadestination = models.FloatField(db_column='seaDestination', blank=True, null=True)  # Field name made lowercase.
    seadriver46wheeler = models.FloatField(db_column='seaDriver46Wheeler', blank=True, null=True)  # Field name made lowercase.
    seahelper46wheeler = models.FloatField(db_column='seaHelper46Wheeler', blank=True, null=True)  # Field name made lowercase.
    seadriver6forwarder = models.FloatField(db_column='seaDriver6Forwarder', blank=True, null=True)  # Field name made lowercase.
    seahelper6forwarder = models.FloatField(db_column='seaHelper6Forwarder', blank=True, null=True)  # Field name made lowercase.
    seadriver10wheeler = models.FloatField(db_column='seaDriver10Wheeler', blank=True, null=True)  # Field name made lowercase.
    seahelper10wheeler = models.FloatField(db_column='seaHelper10Wheeler', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tariff'


class TruckBudget(models.Model):
    truckbudgetid = models.AutoField(db_column='truckBudgetID', primary_key=True)  # Field name made lowercase.
    traveldate = models.DateField(db_column='travelDate', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=30, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    particulars = models.CharField(max_length=50, blank=True, null=True)
    for_field = models.CharField(db_column='for', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    client = models.CharField(max_length=30, blank=True, null=True)
    purchaseorderor = models.CharField(db_column='purchaseOrderOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    liquidated = models.FloatField(blank=True, null=True)
    unliquidated = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'truck_budget'


class Userinformation(models.Model):
    userid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    role = models.CharField(max_length=45, blank=True, null=True)
    employeeid = models.IntegerField(db_column='employeeID', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userinformation'


PARTICULAR_CHOICES = (
    ('Diesel', 'Diesel'),
    ('Truck Parts / Supplies', 'Truck Parts / Supplies'),
    ('Payroll', 'Payroll'),
    ('Toll', 'Toll'),
    ('Cash on Hand', 'Cash on Hand'),
)

class Payables(models.Model):
    payableid = models.AutoField(db_column='payableID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    invoiceno = models.CharField(db_column='invoiceNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    documentdate = models.DateField(db_column='documentDate', blank=True, null=True)  # Field name made lowercase.
    supplier = models.CharField(max_length=45, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    particulars = models.CharField(max_length=45, blank=True, null=True)
    checkvoucherno = models.CharField(db_column='checkVoucherNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    checkvoucherdate = models.DateField(db_column='checkVoucherDate', blank=True, null=True)  # Field name made lowercase.
    checkno = models.IntegerField(db_column='checkNo', blank=True, null=True)  # Field name made lowercase.
    checkdate = models.DateField(db_column='checkDate', blank=True, null=True)  # Field name made lowercase.
    checkreleaseddate = models.DateField(db_column='checkReleasedDate', blank=True, null=True)  # Field name made lowercase.
    cleareddate = models.DateField(db_column='clearedDate', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payables'


class Liquidation(models.Model):
    liquidationid = models.AutoField(db_column='liquidationID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    truckid = models.CharField(db_column='truckID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    amountreceived = models.FloatField(db_column='amountReceived', blank=True, null=True)  # Field name made lowercase.
    liquidation = models.FloatField(blank=True, null=True)
    particulars = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liquidation'


class BillingStatementOr(models.Model):
    billingstatementorid = models.AutoField(db_column='billingStatementORID', primary_key=True)  # Field name made lowercase.
    month = models.DateField(blank=True, null=True)
    invoiceno = models.IntegerField(db_column='invoiceNo', blank=True, null=True)  # Field name made lowercase.
    customer = models.CharField(max_length=45, blank=True, null=True)
    particulars = models.CharField(max_length=45, blank=True, null=True)
    invoicedate = models.DateField(db_column='invoiceDate', blank=True, null=True)  # Field name made lowercase.
    invoicereceiveddate = models.DateField(db_column='invoiceReceivedDate', blank=True, null=True)  # Field name made lowercase.
    receivedby = models.CharField(db_column='receivedBy', max_length=45, blank=True, null=True)  # Field name made lowercase.
    totalsales = models.FloatField(db_column='totalSales', blank=True, null=True)  # Field name made lowercase.
    taxablesales = models.FloatField(db_column='taxableSales', blank=True, null=True)  # Field name made lowercase.
    vat = models.FloatField(blank=True, null=True)
    creditabletax = models.FloatField(db_column='creditableTax', blank=True, null=True)  # Field name made lowercase.
    orno = models.IntegerField(db_column='orNo', blank=True, null=True)  # Field name made lowercase.
    paidamount = models.FloatField(db_column='paidAmount', blank=True, null=True)  # Field name made lowercase.
    datepaid = models.DateField(db_column='datePaid', blank=True, null=True)  # Field name made lowercase.
    variancediff = models.FloatField(db_column='varianceDiff', blank=True, null=True)  # Field name made lowercase.
    acctstitle = models.CharField(db_column='acctsTitle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_statement_or'


class BillingStatementAr(models.Model):
    billingstatementarid = models.AutoField(db_column='billingStatementARID', primary_key=True)  # Field name made lowercase.
    month = models.DateField(blank=True, null=True)
    soano = models.CharField(db_column='soaNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customer = models.CharField(max_length=45, blank=True, null=True)
    particulars = models.CharField(max_length=45, blank=True, null=True)
    invoicedate = models.DateField(db_column='invoiceDate', blank=True, null=True)  # Field name made lowercase.
    invoicereceiveddate = models.DateField(db_column='invoiceReceivedDate', blank=True, null=True)  # Field name made lowercase.
    receivedby = models.CharField(db_column='receivedBy', max_length=45, blank=True, null=True)  # Field name made lowercase.
    totalsales = models.FloatField(db_column='totalSales', blank=True, null=True)  # Field name made lowercase.
    arno = models.CharField(db_column='arNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paidamount = models.FloatField(db_column='paidAmount', blank=True, null=True)  # Field name made lowercase.
    datepaid = models.DateField(db_column='datePaid', blank=True, null=True)  # Field name made lowercase.
    variancediff = models.FloatField(db_column='varianceDiff', blank=True, null=True)  # Field name made lowercase.
    acctstitle = models.CharField(db_column='acctsTitle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_statement_ar'


class CashMonitoring(models.Model):
    cashmonitoringid = models.AutoField(db_column='cashMonitoringID', primary_key=True)  # Field name made lowercase.
    client = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    checkno = models.CharField(db_column='checkNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    checkvoucherno = models.CharField(db_column='checkVoucherNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    deposit = models.FloatField(blank=True, null=True)
    withdrawal = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_monitoring'


class CashOnHand(models.Model):
    cashonhandid = models.AutoField(db_column='cashOnHandID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    truckid = models.CharField(db_column='truckID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    received = models.FloatField(blank=True, null=True)
    truckbudget = models.FloatField(db_column='truckBudget', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_on_hand'