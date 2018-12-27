from django.shortcuts import render
import datetime

# Create your views here.
def welcome(request):
    insert_date=datetime.datetime.now()
    return render(request,'testapp/home.html',{'insert_date':insert_date})

