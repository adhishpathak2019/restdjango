import django_filters
from rest_framework import filters
from django.shortcuts import render
from .serializers import UserSerializer, UserListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import viewsets
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.db.models import Count, Q
from django.contrib.auth.models import User

# Create your views here.

class UserCreate(APIView):
    
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields = ('username','email',)
    ordering_fields = ('username',)



class UserDetailView(APIView):
	pass
