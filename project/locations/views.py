from django.shortcuts import render
from rest_framework import generics
from locations.models import User,Location
from locations.serializers import UserLocationSerializer, LocationSerializer
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView

# Create your views here.

# SERACH BY EMAIL OR PHONE.(can GET, POST,SEARCH)
class UserList(generics.ListCreateAPIView):
        # eg: http://127.0.0.1:8000/user-by-email-or-phone?search=martinwainaina001@gmail.com
    queryset = User.objects.all()
    serializer_class = UserLocationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['email','password',]

# SERACH BY date OR time.(can GET, POST,SEARCH)
class LocationLists(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['date','time',]

# Get user by id
class SingleUser(RetrieveAPIView):
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    serializer_class = UserLocationSerializer

# Get location by id
class SingleLocation(RetrieveAPIView):
    def get_queryset(self):
        queryset = Location.objects.all()
        return queryset
    serializer_class = LocationSerializer
