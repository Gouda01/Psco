from django.urls import path
from django.contrib.auth.decorators import login_required

from accounting import views



app_name = "accounting"

urlpatterns = [
    
    #Treasury :
    path('cash-transactions/',login_required(views.cash_transactions),name='cash-transactions'),
    

    
]
