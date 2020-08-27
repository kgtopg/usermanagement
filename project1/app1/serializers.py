from rest_framework import serializers
from .models import users


class users(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = ('user_id', 'user_role_id', 'user_full_name', 'user_email',
                  'user_password', 'user_dob','user_gender',' user_photo',
                  'user_reg_date','user_status','created_date','timestamp' )