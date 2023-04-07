from django.urls import path

from . import views

urlpatterns = [

    path('register/', views.RegisterView.as_view(), name='auth_register'),

    path('user/', views.UserListView.as_view()),
    path('user/<str:phone>', views.UserDetailView.as_view()),

    path('apartment/', views.ApartmentListCreateView.as_view()),
    path('apartment/<int:pk>', views.ApartmentDetailView.as_view()),
    path('apartment/search/', views.search),

    path('jobs/', views.JobsListCreateView.as_view()),
    path('jobs/<int:pk>', views.JobsDetailView.as_view()),
    path('jobs/search/', views.job_search),

]
