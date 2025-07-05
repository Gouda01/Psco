from django.urls import path
from django.contrib.auth.decorators import login_required

from dashboard import views



app_name = "dashboard"

urlpatterns = [
    
    # Website :
    path('',login_required(views.website),name='website'),
    
    #Dashboard :
    # path('managements-list/',login_required(views.managements_view),name='managements-list'),
    

    
]
