from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'addresses',views.AddressViewSet,basename='address')
router.register(r'users',views.UserViewSet,basename='user')

urlpatterns = [
    path('', include(router.urls)),
]