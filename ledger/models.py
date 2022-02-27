import datetime

from django.db import models
from django.utils import timezone

from django.contrib import admin

# Create your models here.

class Category(models.Model):
    name = models.CharField("category name", max_length=32)
    is_out = models.BooleanField("is out")
    craetion_datetime = models.DateTimeField("creation datetime", auto_now_add=True)
    update_datetime = models.DateTimeField("update datetime", auto_now=True)

class Source(models.Model):
    name = models.CharField("source name", max_length=32)
    balance = models.PositiveIntegerField("balance")
    creation_datetime = models.DateTimeField("creation datetime", auto_now_add=True)
    update_datetime = models.DateTimeField("update datetime", auto_now=True)

class PaymentType(models.Model):
    name = models.CharField("payment type name", max_length=32)
    creation_datetime = models.DateTimeField("creation datetime", auto_now_add=True)
    update_datetime = models.DateTimeField("update datetime", auto_now=True)

class Transaction(models.Model):
    transaction_date = models.DateField("transaction date")
    amount = models.PositiveIntegerField("amount")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.CharField("description", max_length=256)
    source = models.ForeignKey(Source, on_delete=models.PROTECT)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT, null=True)
    is_creadit = models.BooleanField("is creadit")
