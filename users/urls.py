from django.urls import path
from rest_framework import routers
from .views import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('auth', AuthViewSet, basename='auth')

urlpatterns = router.urls

# urlpatterns = [
#     # path('<str:id>/', views.WorkspaceView.as_view()),
#     # path('create', views.CreateWorkspaceView.as_view()),
# ]