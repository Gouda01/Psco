from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from settings.models import Management


# Create your views here.

def home (request) :
    return render (request, 'home.html')


# Managements
@login_required
@permission_required('settings.view_settings', raise_exception=True)
def managements_view (request):
    managements = Management.objects.all()
    
    context = {
        'managements' : managements,
    }
    
    return render (request, 'managements.html', context)


@login_required
@permission_required('settings.add_settings', raise_exception=True)
def add_management(request):

    if request.method=='POST' :
        name = request.POST.get('name')
        code = request.POST.get('code')
        details = request.POST.get('details')
             

        Management.objects.create(
            name = name,
            code = code,
            details = details,
            
        )

        messages.success(request, 'Management Added Successfuly')
        return redirect("settings:managements-list")
    else :
        messages.warning(request, 'Management Didnt Add .... Try again')
        return redirect("settings:managements-list")


@login_required
@permission_required('settings.change_settings', raise_exception=True)
def edit_management(request):
    
    id = request.POST.get('id')
    management = Management.objects.get(id=id)

    name = request.POST.get('name')
    code = request.POST.get('code')
    details = request.POST.get('details')

    management.name = name
    management.code = code
    management.details = details
    
    management.save()
    
    messages.success(request, 'Management Edited Successfuly')
    return redirect("settings:managements-list")


@login_required
@permission_required('settings.delete_settings', raise_exception=True)
def delete_management(request):
    
    id = request.POST.get('id')
    management = Management.objects.get(id=id)
    management.delete()
    messages.error(request, 'Management Deleted Successfuly')
    return redirect("settings:managements-list")