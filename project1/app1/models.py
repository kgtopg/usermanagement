from django.db import models

# Create your models here.
class users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_role_id = models.IntegerField()
    user_full_name = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_dob = models.DateField()
    user_gender = models.CharField(max_length=100, blank=True)
    user_photo = models.ImageField()
    user_reg_date = models.DateTimeField()
    user_status = models.CharField(max_length=100)
    created_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
