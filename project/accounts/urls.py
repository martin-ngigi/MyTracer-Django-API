from django.urls import path
from .views import UserView, UserDetail

urlpatterns = [
    path('users/', UserView.as_view(), name="UsersView"),
    path('users/', UserDetail.as_view(), name="UsersDetail"),
    path('users/<int:pk>/', UserDetail.as_view(), name="UsersDetail"),
]