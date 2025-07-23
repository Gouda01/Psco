from django.urls import path
from django.contrib.auth.decorators import login_required

from dashboard import views



app_name = "dashboard"

urlpatterns = [
    
    # Website :
    path('',views.website,name='website'),
    
    #Dashboard :
    path('dashboard/',login_required(views.dashboard),name='dashboard'),
    

    
]
