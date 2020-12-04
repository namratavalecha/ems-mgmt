from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .serializers import ProjectSerializer
from .models import Project


# Create your views here.

class ProjectView(generics.GenericAPIView,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    '''
    View for Workspace using Generic API View
    '''
    authentication_classes = []
    permission_classes = []

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request)

    def patch(self, request, id=None):
        return self.partial_update(request, id)


class CreateProjectView(generics.GenericAPIView,
                 mixins.CreateModelMixin):
    '''
    View to create Workspace using Generic API View
    '''
    authentication_classes = []
    permission_classes = []

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = 'id'

    def post(self, request):
        return self.create(request)
        

class ListProjectView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        environment_id = self.kwargs['env_id']
        return Project.objects.filter(environment__id=environment_id)
