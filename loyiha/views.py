from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from  rest_framework.decorators import api_view
from django.http import HttpRequest
@api_view(['GET'])
def student_list(request: HttpRequest):
    if request.method == 'GET':
        studentds = Talabalar.objects.filter(eng_yaxshi)
        serializer = TalabalarSerializer(studentds, many = True)
        return Response(serializer.data)





class TalabalarViewSet(viewsets.ModelViewSet):
    queryset = Talabalar.objects.all()
    serializer_class = TalabalarSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['ismi','familiyasi']
    search_fields = ['ismi','familiyasi']
    ordering_fields = ['ismi']
    ordering = ['-id']


class LoyihaViewSet(viewsets.ModelViewSet):
    queryset = Loyiha.objects.all()
    serializer_class = LoyihaSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]

# class Eng_yaxshiViewSet(viewsets.ModelViewSet):
#     queryset = Eng_yaxshi.objects.all()
#     serializer_class = Eng_yaxshiSerializer
#     # authentication_classes = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated, DjangoModelPermissions]
#     filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
#     filterset_fields = ['darajasi']
#     search_fields = ['loyihasi']
#     ordering_fields = ['loyihasi']
#     ordering = ['-id']

    
   




# Create your views here.
