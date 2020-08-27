from django.shortcuts import render
from rest_framework import viewsets

from .serializers import users
from .models import users


class HeroViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all().order_by('name')
    serializer_class = users
