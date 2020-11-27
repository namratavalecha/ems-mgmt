from django.urls import path
from environment import views

urlpatterns = [
    path('<int:id>/', views.EnvironmentView.as_view()),
    path('create', views.CreateEnvironmentView.as_view()),
    path('all/<str:workspace_id>/', views.ListEnvironmentView.as_view()),
]