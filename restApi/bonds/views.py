from django.shortcuts import render
from rest_framework import viewsets

from bonds.models import Bond, User
from bonds.serializers import BondSerializer, UserSerializer


class BondViewSet(viewsets.ModelViewSet):
    serializer_class = BondSerializer
    queryset = Bond.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
