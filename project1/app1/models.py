from django.db import models

# Create your models here.
class details(models.Model):
    user_id = models.IntegerField(max_length=50,primary_key=True)
    user_role_id = models.IntegerField(max_length=50, primary_key=True)
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

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
