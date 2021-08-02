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
from .permissions import IsOwnerOrReadOnly
from rest_framework import status
from django.http import QueryDict

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    """ def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user

        return super(UserViewSet, self).get_object() """

class AddressViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    #permission_classes = (IsOwnerOrReadOnly,)

    #queryset = Address.objects.all()logout 
    #queryset = Address.objects.filter(owner=self.request.user)
    serializer_class = AddressSerializer

    def get_queryset(self):
        #queryset = Address.objects.all()
        queryset = Address.objects.filter(user=self.request.user)
        ad_id = self.request.query_params.get('ad_id')
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

    """ def destroy(self, request, *args, **kwargs):
        q = QueryDict(self.request.query_params.items())
        for ads_ids in q.values():
            instance = Address.objects.filter(id=ads_ids)
            instance.delete()
        #instance = self.get_object()
        #self.perform_destroy(instance)
        return Response(data='Delete successful',status=status.HTTP_204_NO_CONTENT) """