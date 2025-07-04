from django.db import models



# Create your models here.  

# Management
class Management(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=35, unique=True)
    details = models.TextField(max_length=5000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("add_settings", "Can add settings"),
            ("change_settings", "Can change settings"),
            ("view_settings", "Can view settings"),
            ("delete_settings", "Can delete settings"),
        ]

    
    def __str__(self):
        return self.name
           