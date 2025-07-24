from django.contrib import admin

from .models import Cashbox, CashTransaction


# Register your models here.
admin.site.register(Cashbox)
admin.site.register(CashTransaction)