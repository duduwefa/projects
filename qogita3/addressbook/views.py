from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Address
from django.template import loader
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import AddressSerializer
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user

        return super(UserViewSet, self).get_object()

class AddressViewSet(viewsets.ModelViewSet):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        queryset = Address.objects.all()
        ad_id = self.request.query_params.get('id')
        street_name = self.request.query_params.get('street_name')
        house_number = self.request.query_params.get('house_number')
        zip_code = self.request.query_params.get('zip_code')
        user_id = self.request.query_params.get('user_id')
        if street_name is not None:
            queryset = queryset.filter(street_name__startswith=street_name)
        if ad_id is not None:
            queryset = queryset.filter(id=ad_id)
        if house_number is not None:
            queryset = queryset.filter(house_number__startswith=house_number)
        if zip_code is not None:
            queryset = queryset.filter(zip_code__startswith=zip_code)
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
        return queryset