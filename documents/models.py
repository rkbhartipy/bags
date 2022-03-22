import numbers
from operator import mod
from xml.dom.minidom import DocumentType
from django.db import models

import documents
from datetime import datetime

# Create your models here.
class uplaodingDocument(models.Model):
    documentNumber = models.BigIntegerField()
    DocumentType = models.CharField(max_length=200)
    itemType = models.CharField(max_length=200)
    documentDate = models.DateField(default=datetime.today)
    documentFile= models.FileField(upload_to="static")
    def __str__(self):
        return self.DocumentType

class newFCompany(models.Model):
    date = models.DateField(default=datetime.today)
    FCompany =models.CharField(max_length=200)
    depostieAmount = models.IntegerField()
    paymenetAmount = models.IntegerField()
    DepPAyDate = models.DateField()
    netAmount = models.IntegerField()
    def __str__(self):
        return self.FCompany
    
class advanceFcompany(models.Model):
    date = models.DateField(default=datetime.today)
    idComapny = models.BigIntegerField()
    name =models.CharField(max_length=200)
    recevingNumber = models.BigIntegerField()
    receivingAmount = models.BigIntegerField()
    expenceNumber= models.BigIntegerField()
    expenceAmount =models.BigIntegerField()
    depositeAmount = models.BigIntegerField()
    paymentAmount = models.BigIntegerField()
    DepPayDate = models.DateField()
    FCompany =models.CharField(max_length=200)
    RecLink = models.CharField(max_length=200)
    NetAmount = models.BigIntegerField()
    receiDepPay = models.BigIntegerField()
    details = models.TextField()
    notes = models.TextField()
    def __str__(self):
        return self.FCompany