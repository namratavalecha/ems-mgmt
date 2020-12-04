from django.urls import path
from rest_framework import routers
from .views import AuthViewSet, GetWorkspaceEmployee

router = routers.DefaultRouter(trailing_slash=False)
router.register('auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('workspace/<str:workspace_id>/', GetWorkspaceEmployee.as_view()),
]

urlpatterns += router.urls