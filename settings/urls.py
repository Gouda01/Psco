from django.urls import path
from django.contrib.auth.decorators import login_required

from settings import views



app_name = "settings"

urlpatterns = [
    
    # Cash Categories :
    path('cash-categories-list/',login_required(views.cash_categories_view),name='cash-categories-list'),
    path('add-cash-category/',login_required(views.add_cash_category),name='add-cash-category'),
    path('edit-cash-category/',login_required(views.edit_cash_category),name='edit-cash-category'),
    path('delete-cash-category/',login_required(views.delete_cash_category),name='delete-cash-category'),

    
]
