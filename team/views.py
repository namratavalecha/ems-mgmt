from rest_framework import generics
from rest_framework import mixins
from .serializers import TeamSerializer
from .models import Team

# Create your views here.

class TeamView(generics.GenericAPIView,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin):
    '''
    View for Workspace using Generic API View
    '''
    authentication_classes = []
    permission_classes = []

    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.update(request, id)

