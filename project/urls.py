from django.urls import path
from project import views

urlpatterns = [
    path('<int:id>/', views.ProjectView.as_view()),
    path('create', views.CreateProjectView.as_view()),
    path('all/<str:env_id>/', views.ListProjectView.as_view()),
]