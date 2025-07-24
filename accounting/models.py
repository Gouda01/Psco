# treasury/models.py
from django.db import models, transaction
from django.contrib.auth import get_user_model

from settings.models import CashCategory

User = get_user_model()


class Cashbox(models.Model):
    name = models.CharField(max_length=100, default="الخزينة الرئيسية")
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.branch.name}"


class CashTransaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'إيراد'),
        ('expense', 'مصروف'),
    )

    cashbox = models.ForeignKey(Cashbox, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    category = models.ForeignKey(CashCategory, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_type_display()} - {self.amount}"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.pk:
                # تعديل: نطرح القيمة القديمة من الرصيد
                old = CashTransaction.objects.get(pk=self.pk)
                if old.type == 'income':
                    self.cashbox.balance -= old.amount
                elif old.type == 'expense':
                    self.cashbox.balance += old.amount

            super().save(*args, **kwargs)

            # إضافة القيمة الجديدة للرصد
            if self.type == 'income':
                self.cashbox.balance += self.amount
            elif self.type == 'expense':
                self.cashbox.balance -= self.amount

            self.cashbox.save()

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            if self.type == 'income':
                self.cashbox.balance -= self.amount
            elif self.type == 'expense':
                self.cashbox.balance += self.amount
            self.cashbox.save()
            super().delete(*args, **kwargs)
