
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# # Create your views here.
# from .models import *
# from .forms import *
# import csv,datetime,xlwt
# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile
# from django.db.models import Sum
# from xhtml2pdf import pisa
# from io import BytesIO
# import sys
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy
# import numpy as np

def user_login(request):
    if request.method=='POST':
        username=request.POST['uname1']
        print(username)
        password=request.POST['pwd1']
        print(password)
        user=authenticate(username=username,password=password)
        if(user):
            login(request,user)
            return render(request, 'index.html')
    return render(request, 'user_login.html')



    # if request.method == 'POST':
    #     username = request.POST['uname1']
    #     password = request.POST['pwd1']
    #     user=authenticate(username=username, password=password)
    #     if(user):
    #         login(request, user)
    #         return redirect('/userprofile')
    # return render(request, 'login.html')