from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from settings.models import CashCategory


# Create your views here.


# Cash Category
@login_required
@permission_required('settings.view_settings', raise_exception=True)
def cash_categories_view (request):
    categories = CashCategory.objects.all()
    
    context = {
        'categories' : categories,
    }
    
    return render (request, 'cash_categories.html', context)


@login_required
@permission_required('settings.add_settings', raise_exception=True)
def add_cash_category(request):

    if request.method=='POST' :
        name = request.POST.get('name')
        type = request.POST.get('type')
        details = request.POST.get('details')
             

        CashCategory.objects.create(
            name = name,
            type = type,
            details = details,
            
        )

        messages.success(request, 'تم اضافة البند بنجاح')
        return redirect("settings:cash-categories-list")
    else :
        messages.warning(request, 'لم يتم اضافة البند .... حاول مرة اخري')
        return redirect("settings:cash-categories-list")


@login_required
@permission_required('settings.change_settings', raise_exception=True)
def edit_cash_category(request):
    
    if request.method=='POST' :
        id = request.POST.get('id')
        cash_category = CashCategory.objects.get(id=id)

        name = request.POST.get('name')
        type = request.POST.get('type')
        details = request.POST.get('details')

        cash_category.name = name
        cash_category.type = type
        cash_category.details = details
        
        cash_category.save()
        
        messages.success(request, 'تم تعديل البند بنجاح')
        return redirect("settings:cash-categories-list")
    else :
        messages.warning(request, 'لم يتم تعديل البند .... حاول مرة اخري')
        return redirect("settings:cash-categories-list")



@login_required
@permission_required('settings.delete_settings', raise_exception=True)
def delete_cash_category(request):
    
    if request.method=='POST' :
        id = request.POST.get('id')
        cash_category = CashCategory.objects.get(id=id)
        cash_category.delete()
        messages.success(request, 'تم حذف البند بنجاح')
        return redirect("settings:cash-categories-list")
    else :
        messages.warning(request, 'لم يتم حذف البند .... حاول مرة اخري')
        return redirect("settings:cash-categories-list")