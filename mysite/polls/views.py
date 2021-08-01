from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import QuestionSerializer
from .models import Question
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] # permission class changed
    authentication_classes = [TokenAuthentication]
    queryset = Question.objects.all().order_by('pub_date')
    serializer_class = QuestionSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")