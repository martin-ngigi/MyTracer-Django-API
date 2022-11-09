from django.urls import path
from locations import views

urlpatterns = [
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.SingleUser.as_view()),
    path("location/", views.LocationLists.as_view()),
    path("location/<int:pk>/", views.SingleLocation.as_view()),
]