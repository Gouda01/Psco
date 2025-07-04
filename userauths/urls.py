from django.urls import path
from django.contrib.auth.decorators import login_required

from userauths import views


app_name = "userauths"

urlpatterns = [
    
    # Login :
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/', views.LogoutView.as_view(), name="logout"),


    # Users :
    path('users/',login_required(views.show_users),name='users'),
 
    # path('add-employer/',login_required(views.add_employer),name='add-employer'),
    # path('save-employer/',login_required(views.save_employer),name='save-employer'),
    # path('edit-employer/<int:pk>',login_required(views.edit_employer),name='edit-employer'),
    # path('update-employer/<int:pk>',login_required(views.update_employer),name='update-employer'),
    # path('employer-details/<int:pk>/',login_required(views.employer_details),name='employer-details'),
    # path('active-employer/',login_required(views.active_employer),name='active-employer'),
    # path('deactive-employer/',login_required(views.deactive_employer),name='deactive-employer'),
    
    
]
