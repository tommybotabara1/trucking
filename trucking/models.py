# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


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


class Table1(models.Model):
    calltime = models.TimeField(db_column='callTime', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    origin = models.CharField(max_length=30, blank=True, null=True)
    destination = models.CharField(max_length=30, blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client', blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer', blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    plateno = models.CharField(db_column='plateNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wbno = models.CharField(db_column='WBNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    driver = models.ForeignKey(Driver, models.DO_NOTHING, db_column='driver', blank=True, null=True)
    helper = models.CharField(max_length=30, blank=True, null=True)
    trucktype = models.CharField(db_column='truckType', max_length=20, blank=True,
                                 null=True, choices=TRUCK_TYPE_CHOICES)  # Field name made lowercase.
    qty = models.FloatField(blank=True, null=True)
    driversal = models.FloatField(db_column='driverSal', blank=True, null=True)  # Field name made lowercase.
    helpersal = models.FloatField(db_column='helperSal', blank=True, null=True)  # Field name made lowercase.
    billing = models.FloatField(blank=True, null=True)
    receivedby = models.CharField(db_column='receivedBy', max_length=45, blank=True,
                                  null=True)  # Field name made lowercase.
    receiveddatetime = models.DateTimeField(db_column='receivedDateTime', blank=True,
                                            null=True)  # Field name made lowercase.
    entryfee = models.FloatField(db_column='entryFee', blank=True, null=True)  # Field name made lowercase.
    parking = models.FloatField(blank=True, null=True)
    tollfee = models.FloatField(db_column='tollFee', blank=True, null=True)  # Field name made lowercase.
    others = models.FloatField(blank=True, null=True)
    totalliq = models.FloatField(db_column='totalLiq', blank=True, null=True)  # Field name made lowercase.
    truckbudget = models.FloatField(db_column='truckBudget', blank=True, null=True)  # Field name made lowe
    unliq = models.FloatField(blank=True, null=True)
    addldriversal = models.FloatField(db_column='addLDriverSal', blank=True, null=True)  # Field name made lowercase.# rcase.
    cahelper = models.FloatField(db_column='caHelper', blank=True, null=True)  # Field name made lowercase.
    addl = models.FloatField(db_column='addL', blank=True, null=True)  # Field name made lowercase.
    diesel = models.FloatField(blank=True, null=True)
    revenue = models.FloatField(blank=True, null=True)
    billeddate = models.DateField(db_column='billedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table1'


class SplitAmounts(models.Model):
    splitamountid = models.AutoField(db_column='splitAmountID', primary_key=True)  # Field name made lowercase.
    dboid = models.ForeignKey('Table1', models.DO_NOTHING, db_column='dboID')  # Field name made lowercase.
    type = models.CharField(max_length=45)
    amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'split_amounts'


class Userinformation(models.Model):
    userid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    role = models.CharField(max_length=45, blank=True, null=True)
    employeeid = models.IntegerField(db_column='employeeID', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userinformation'