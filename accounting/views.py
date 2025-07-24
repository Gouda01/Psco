from django.shortcuts import render

from .models import Cashbox, CashTransaction


# Create your views here.

# Treasury :
def cash_transactions(request) :

    transactions = CashTransaction.objects.filter(cashbox_id = 1)

    context = {
        'transactions' : transactions,
    }

    return render (request,'treasury/cash_transactions.html', context)
    