from django.db import models



# Create your models here.  

# Management
# class Management(models.Model):
#     name = models.CharField(max_length=120)
#     code = models.CharField(max_length=35, unique=True)
#     details = models.TextField(max_length=5000, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     edited_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         permissions = [
#             ("add_settings", "Can add settings"),
#             ("change_settings", "Can change settings"),
#             ("view_settings", "Can view settings"),
#             ("delete_settings", "Can delete settings"),
#         ]

    
#     def __str__(self):
#         return self.name


class CashCategory(models.Model):
    CATEGORY_TYPE_CHOICES = (
        ('income', 'إيراد'),
        ('expense', 'مصروف'),
    )

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=CATEGORY_TYPE_CHOICES)
    details = models.CharField(max_length=1000, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
           