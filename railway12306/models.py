# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrator(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jobnumber = models.CharField(db_column='JOBNUMBER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    postision = models.CharField(db_column='POSTISION', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'administrator'


class Deleted(models.Model):
    dingdanhao = models.CharField(db_column='DINGDANHAO', primary_key=True, max_length=100)  # Field name made lowercase.
    passengerid = models.CharField(db_column='PASSENGERID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    passengername = models.CharField(db_column='PASSENGERNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    passengeridnum = models.CharField(db_column='PASSENGERIDNUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    trainid = models.CharField(db_column='TRAINID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    daparturedate = models.CharField(db_column='DAPARTUREDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dapartureplace = models.CharField(db_column='DAPARTUREPLACE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    arrivalplace = models.CharField(db_column='ARRIVALPLACE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    daparturetime = models.CharField(db_column='DAPARTURETIME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    arrivaltime = models.CharField(db_column='ARRIVALTIME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    seattype = models.CharField(db_column='SEATTYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deletetime = models.DateTimeField(db_column='DELETETIME')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'deleted'


class Passenger(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idnumber = models.CharField(db_column='IDNUMBER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'passenger'


class Ticket(models.Model):
    num = models.CharField(db_column='NUM', primary_key=True, max_length=100)  # Field name made lowercase.
    trainid = models.CharField(db_column='TRAINID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dapartureplace = models.CharField(db_column='DAPARTUREPLACE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    arrivalplace = models.CharField(db_column='ARRIVALPLACE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    daparturedate = models.CharField(db_column='DAPARTUREDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    daparturetime = models.CharField(db_column='DAPARTURETIME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    arrivaltime = models.CharField(db_column='ARRIVALTIME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    seattype = models.CharField(db_column='SEATTYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ticket'


class Ticketlist(models.Model):
    dingdanhao = models.CharField(db_column='DINGDANHAO', primary_key=True, max_length=100)  # Field name made lowercase.
    passengerid = models.CharField(db_column='PASSENGERID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    passengername = models.CharField(db_column='PASSENGERNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    passengeridnum = models.CharField(db_column='PASSENGERIDNUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    trainid = models.CharField(db_column='TRAINID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    daparturedate = models.CharField(db_column='DAPARTUREDATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dapartureplace = models.CharField(db_column='DAPARTUREPLACE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    arrivalplace = models.CharField(db_column='ARRIVALPLACE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    daparturetime = models.CharField(db_column='DAPARTURETIME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    arrivaltime = models.CharField(db_column='ARRIVALTIME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    seattype = models.CharField(db_column='SEATTYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CREATETIME')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ticketlist'
