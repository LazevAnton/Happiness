from rest_framework.serializers import ModelSerializer

from HappinessAPP.models import Teams, Members


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Teams
        fields = ['id', 'team_name']


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'
