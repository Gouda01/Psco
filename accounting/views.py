from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from decimal import Decimal
from django.db.models.aggregates import Sum

from .models import Cashbox, CashTransaction
from settings.models import CashCategory


# Create your views here.

# Treasury :

@login_required
@permission_required('settings.add_settings', raise_exception=True)
def cash_transactions(request) :

    transactions = CashTransaction.objects.filter(cashbox_id = 1).order_by('-date')
    balance = Cashbox.objects.get(id=1).balance

    income_categories = CashCategory.objects.filter(type='income')
    expense_categories = CashCategory.objects.filter(type='expense')

    total_incomes = CashTransaction.objects.filter(cashbox_id = 1,type='income').aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    total_expenses = CashTransaction.objects.filter(cashbox_id = 1,type='expense').aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    fit_balance = total_incomes - total_expenses

    context = {
        'transactions' : transactions,
        'balance' : balance,
        'income_categories' : income_categories,
        'expense_categories' : expense_categories,
        'total_incomes' : total_incomes,
        'total_expenses' : total_expenses,
        'fit_balance' : fit_balance,
    }

    return render (request,'treasury/cash_transactions.html', context)
    

@login_required
@permission_required('settings.add_settings', raise_exception=True)
def add_income(request):


    if request.method=='POST' :
        category_id = request.POST.get('category_id')
        amount = Decimal(request.POST.get("amount", "0"))
        description = request.POST.get('description')
        receipt = request.POST.get('receipt')
        date = request.POST.get('date')


        CashTransaction.objects.create(
            cashbox_id = 1,
            type = 'income',
            created_by = request.user,
            amount = amount,
            category_id = category_id,
            description = description,
            receipt = receipt,
            date = date,
            
        )

        messages.success(request, 'تم اضافة الايراد بنجاح')
        return redirect("accounting:cash-transactions")
        
        
    else :
        messages.warning(request, 'لم يتم اضافة الايراد .... حاول مرة اخري')
        return redirect("accounting:cash-transactions")


@login_required
@permission_required('settings.add_settings', raise_exception=True)
def add_expense(request):


    if request.method=='POST' :
        category_id = request.POST.get('category_id')
        amount = Decimal(request.POST.get("amount", "0"))
        description = request.POST.get('description')
        receipt = request.POST.get('receipt')
        date = request.POST.get('date')

        balance = Cashbox.objects.get(id=1).balance

        if amount <= balance :

            CashTransaction.objects.create(
                cashbox_id = 1,
                type = 'expense',
                created_by = request.user,
                amount = amount,
                category_id = category_id,
                description = description,
                receipt = receipt,
                date = date,
                
            )

            messages.success(request, 'تم اضافة المصروف بنجاح')
            return redirect("accounting:cash-transactions")
        
        else :
            messages.warning(request, 'المبلغ المنصرف اكبر من الرصيد .... حاول مرة اخري')
            return redirect("accounting:cash-transactions")
        

    else :
        messages.warning(request, 'لم يتم اضافة المصروف .... حاول مرة اخري')
        return redirect("accounting:cash-transactions")