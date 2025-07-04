from django.urls import path
from django.contrib.auth.decorators import login_required

from settings import views



app_name = "settings"

urlpatterns = [
    
    # Managements :
    path('managements-list/',login_required(views.managements_view),name='managements-list'),
    path('add-management/',login_required(views.add_management),name='add-management'),
    path('edit-management/',login_required(views.edit_management),name='edit-management'),
    path('delete-management/',login_required(views.delete_management),name='delete-management'),

    
]
