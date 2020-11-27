from django.urls import path
from team import views

urlpatterns = [
    path('<int:id>/', views.TeamView.as_view()),
]