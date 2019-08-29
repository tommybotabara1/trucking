# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Client(models.Model):
    clientid = models.IntegerField(db_column='clientID', primary_key=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='clientName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'


class Customer(models.Model):
    customerid = models.IntegerField(db_column='customerID', primary_key=True)  # Field name made lowercase.
    customername = models.CharField(db_column='customerName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Driver(models.Model):
    driverid = models.IntegerField(db_column='driverID', primary_key=True)  # Field name made lowercase.
    drivername = models.CharField(db_column='driverName', max_length=30)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=10)  # Field name made lowercase.
    sss = models.CharField(db_column='SSS', max_length=20)  # Field name made lowercase.
    taxid = models.CharField(db_column='taxID', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'driver'


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
    trucktype = models.CharField(db_column='truckType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qty = models.FloatField(blank=True, null=True)
    driversal = models.FloatField(db_column='driverSal', blank=True, null=True)  # Field name made lowercase.
    helpersal = models.FloatField(db_column='helperSal', blank=True, null=True)  # Field name made lowercase.
    billing = models.FloatField(blank=True, null=True)
    receivedby = models.CharField(db_column='receivedBy', max_length=45, blank=True, null=True)  # Field name made lowercase.
    receiveddatetime = models.DateTimeField(db_column='receivedDateTime', blank=True, null=True)  # Field name made lowercase.
    entryfee = models.FloatField(db_column='entryFee', blank=True, null=True)  # Field name made lowercase.
    parking = models.FloatField(blank=True, null=True)
    tollfee = models.FloatField(db_column='tollFee', blank=True, null=True)  # Field name made lowercase.
    others = models.FloatField(blank=True, null=True)
    totalliq = models.FloatField(db_column='totalLiq', blank=True, null=True)  # Field name made lowercase.
    truckbudget = models.FloatField(db_column='truckBudget', blank=True, null=True)  # Field name made lowercase.
    unliq = models.FloatField(blank=True, null=True)
    addldriversal = models.FloatField(db_column='addLDriverSal', blank=True, null=True)  # Field name made lowercase.
    cahelper = models.FloatField(db_column='caHelper', blank=True, null=True)  # Field name made lowercase.
    addl = models.FloatField(db_column='addL', blank=True, null=True)  # Field name made lowercase.
    diesel = models.FloatField(blank=True, null=True)
    revenue = models.FloatField(blank=True, null=True)
    billeddate = models.DateField(db_column='billedDate', blank=True, null=True)  # Field name made lowercase.
    phase = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table1'


class Userinformation(models.Model):
    userid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    role = models.CharField(max_length=45, blank=True, null=True)
    employeeid = models.IntegerField(db_column='employeeID', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userinformation'
