from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .serializers import WorkspaceSerializer
from .models import Workspace


class WorkspaceView(generics.GenericAPIView,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin):
    '''
    View for Workspace using Generic API View
    '''
    authentication_classes = []
    permission_classes = []

    serializer_class = WorkspaceSerializer
    queryset = Workspace.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.update(request, id)


class CreateWorkspaceView(generics.GenericAPIView,
                 mixins.CreateModelMixin):
    '''
    View to create Workspace using Generic API View
    '''
    authentication_classes = []
    permission_classes = []

    serializer_class = WorkspaceSerializer
    queryset = Workspace.objects.all()
    lookup_field = 'id'

    def post(self, request, format=None):
        return self.create(request)