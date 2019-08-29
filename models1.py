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


class Table1(models.Model):
    date = models.DateField()
    plateno = models.CharField(db_column='plateNo', max_length=10)  # Field name made lowercase.
    wbno = models.CharField(db_column='WBNo', max_length=10)  # Field name made lowercase.
    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    driver = models.CharField(max_length=30)
    helper = models.CharField(max_length=30)
    customer = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    trucktype = models.CharField(db_column='truckType', max_length=20)  # Field name made lowercase.
    qty = models.IntegerField()
    remarks = models.CharField(max_length=45)
    diesel = models.CharField(max_length=45)
    truckbudget = models.CharField(db_column='truckBudget', max_length=45)  # Field name made lowercase.
    cahelper = models.CharField(db_column='caHelper', max_length=45)  # Field name made lowercase.
    tollfee = models.CharField(db_column='tollFee', max_length=45)  # Field name made lowercase.
    parking = models.CharField(max_length=45)
    entryfee = models.CharField(db_column='entryFee', max_length=45)  # Field name made lowercase.
    others = models.CharField(max_length=45)
    driversal = models.CharField(db_column='driverSal', max_length=45)  # Field name made lowercase.
    helpersal = models.CharField(db_column='helperSal', max_length=45)  # Field name made lowercase.
    billing = models.CharField(max_length=45)
    addl = models.CharField(db_column='addL', max_length=45)  # Field name made lowercase.
    revenue = models.CharField(max_length=45)
    billeddate = models.DateField(db_column='billedDate')  # Field name made lowercase.
    unliq = models.CharField(max_length=45)

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
