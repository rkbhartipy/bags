from email.mime import message
from multiprocessing import context
from urllib import request
from django.shortcuts import render
from .models import advanceFcompany, newFCompany, uplaodingDocument
from admins.models import new_document, new_item
from django.contrib import messages

# my imports
from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponse
import json
from .serializer import advanceFcompanySerializer, uploadingDocumentSerializer, newFCompanySerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, "index.html")
# advanced-f-company-report
def advanced_f_company_report(request):
    advance = advanceFcompany.objects.all()
    context = {"advance":advance}
    return render(request, "user/advanced-f-company-report.html",context)
# document page for the user
def documents_page(request, pk=None, str=None):
    # delete document
    if pk is not None:
        obj=uplaodingDocument.objects.get(pk=pk)
        obj.delete()
        return redirect('/documents-page')

    if str=="sharedoc":
        document_show = uplaodingDocument.objects.all()
        context = {"document_show":document_show, "sharedoc":True}
        return render(request, "user/documents-page.html",context)
        

    document_show = uplaodingDocument.objects.all()
    context = {"document_show":document_show}
    return render(request, "user/documents-page.html",context)

# login the user
def login_user(request):
    return render(request,"user/login.html")

# upload documnets of the user
def upload_document(request, pk=None):

    if pk is not None:
        try:
            data=uplaodingDocument.objects.get(documentNumber=pk)
            if data is not None:
                serializer = uploadingDocumentSerializer(data)
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse({"1"})
        except Exception as e:
            print("exception is :", e)
            return JsonResponse("0", safe=False)


    type = new_document.objects.all()
    item = new_item.objects.all()
    context= {'item':item, 'type':type}
    # post request to save the data
    if request.method =="POST":
        documentNumber = request.POST['documentNumber']
        itemType = request.POST['itemType']
        documentDate = request.POST['documentDate']        
        documentFile = request.POST['documentFile']
        DocumentType = request.POST['DocumentType']

        try:
            print("doc number is :", documentNumber)
            obj=uplaodingDocument.objects.get(documentNumber=documentNumber)
            print("user already exits with this id")
            messages.info(request, "Document already exits with this document id enter another id")
        except Exception as e:
            print("exception is :", e)
            print("save the record")

            upload = uplaodingDocument(documentNumber=documentNumber, itemType=itemType, documentDate=documentDate, documentFile=documentFile, DocumentType=DocumentType)
            upload.save()

    return render(request, "user/upload-document.html", context)

# create f-company recods





@api_view(['GET','POST'])
def create_advanced_f_company(request, pk=None):

    if pk is not None:
        try:
            data=advanceFcompany.objects.get(idComapny=pk)
            if data is not None:
                serializer = advanceFcompanySerializer(data)
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse({"1"})
        except Exception as e:
            print("exception is :", e)
            return JsonResponse("0", safe=False)

    
    if request.method=="POST":
        date = request.POST['date']
        idComapny= request.POST['idComapny']
        name = request.POST['name']
        recevingNumber = request.POST['recevingNumber']
        receivingAmount = request.POST['receivingAmount']
        expenceNumber = request.POST['expenceNumber']
        expenceAmount = request.POST['expenceAmount']
        depositeAmount = request.POST["depositeAmount"]
        paymentAmount = request.POST["paymentAmount"]
        DepPayDate = request.POST["DepPayDate"]
        FCompany = request.POST["FCompany"]
        RecLink = request.POST["RecLink"]
        receiDepPay = request.POST["receiDepPay"]
        NetAmount = request.POST["NetAmount"]
        details = request.POST["details"]
        notes = request.POST["notes"]

        try:
            obj=advanceFcompany.objects.get(idComapny=idComapny)
            print("user already exits with this id")
            messages.info(request, "User already exits with this user id enter another id")
        except Exception as e:
            print("exception is :", e)
            print("save the record")
            advance = advanceFcompany(date=date, idComapny=idComapny,name=name,recevingNumber=recevingNumber, receivingAmount=receivingAmount,expenceAmount=expenceAmount,
            expenceNumber=expenceNumber, depositeAmount=depositeAmount, paymentAmount=paymentAmount,DepPayDate=DepPayDate, FCompany=FCompany,receiDepPay=receiDepPay,details=details,notes=notes,NetAmount=NetAmount,RecLink=RecLink)
            advance.save()

    return render(request,"user/create-advanced-f-company-record.html")



def create_f_company_record(request, fcom=None, pk=None):

    print(fcom, pk)


    if (fcom is not None) and (pk is not None):
        try:
            data=newFCompany.objects.get(FCompany=fcom, depostieAmount=pk)
            if data is not None:
                serializer = newFCompanySerializer(data)
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse({"1"})
        except Exception as e:
            print("exception is :", e)
            return JsonResponse("0", safe=False)


    # netAmount = depostieAmount-paymenetAmount
    if request.method =="POST":
        date = request.POST['date']
        FCompany = request.POST['FCompany']
        depostieAmount= request.POST['depostieAmount']
        paymenetAmount = request.POST['paymenetAmount']
        DepPAyDate = request.POST['DepPAyDate']
        netAmount = request.POST['netAmount']
        fcompany = newFCompany(date=date,FCompany=FCompany,depostieAmount=depostieAmount,paymenetAmount=paymenetAmount,
                               DepPAyDate=DepPAyDate,netAmount=netAmount)
        fcompany.save()
    return render(request,"user/create-f-company-record.html")

def f_company_report(request):
    company = newFCompany.objects.all()
    netAmount = 0
    # for item in netAmount:
    #     netAmount += item.minutes
    #     item.netAmount = netAmount
    context = {"company":company}
    return render(request,"user/f-company-report.html",context)

def delete_doc(request, id):
    print("id is :", id)
    pass

