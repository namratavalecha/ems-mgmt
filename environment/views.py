from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .serializers import EnvironmentSerializer
from .models import Environment


# Create your views here.

class EnvironmentView(generics.GenericAPIView,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    '''
    View for Workspace using Generic API View
    '''
    authentication_classes = []
    permission_classes = []

    serializer_class = EnvironmentSerializer
    queryset = Environment.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request)


class CreateEnvironmentView(generics.GenericAPIView,
                 mixins.CreateModelMixin):
    '''
    View to create Workspace using Generic API View
    '''
    authentication_classes = []
    permission_classes = []

    serializer_class = EnvironmentSerializer
    queryset = Environment.objects.all()
    lookup_field = 'id'

    def post(self, request):
        return self.create(request)
        

class ListEnvironmentView(generics.ListAPIView):
    serializer_class = EnvironmentSerializer

    def get_queryset(self):
        workspace_id = self.kwargs['workspace_id']
        return Environment.objects.filter(workspace__id=workspace_id)