from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'questions',views.QuestionViewSet)

urlpatterns = [
    #path('', views.index, name='index')
    path('', include(router.urls)),
    #path('', include('djoser.urls')),
    #path('', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]