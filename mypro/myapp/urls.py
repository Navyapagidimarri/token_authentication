from django.urls import path,include
from .views import UserListView
urlpatterns = [
     path('users/',UserListView.as_view(),name="user-list-view"),
     
]
