from rest_framework.viewsets import ModelViewSet

from HappinessAPP.models import Teams, Members
from HappinessAPP.serializers import TeamSerializer, MemberSerializer


class TeamsViewSet(ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer


class MembersViewSet(ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
