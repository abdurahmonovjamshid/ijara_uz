from django.urls import path

from . import views

urlpatterns = [

    path('register/', views.RegisterView.as_view(), name='auth_register'),

    path('user/', views.UserListView.as_view()),
    path('user/<str:phone>', views.UserDetailView.as_view()),

    path('apartment/', views.ApartmentListCreateView.as_view()),
]
