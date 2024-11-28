from django.urls import path
from .views import *

urlpatterns=[
    path('',HomeView.as_view(),name="index"),
    path('post/<int:pk>/',DetailView.as_view(),name="detail"),
    path('post/create',createPost,name="create"),
]