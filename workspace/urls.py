from django.urls import path
from workspace import views

urlpatterns = [
    path('<str:id>/', views.WorkspaceView.as_view()),
    path('create', views.CreateWorkspaceView.as_view()),
]