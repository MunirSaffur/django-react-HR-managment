from rest_framework.serializers import ModelSerializer
from dayoff.models import DayOff, Users

class DayOffSerializer(ModelSerializer):
    class Meta:
        model = DayOff
        fields = '__all__'
        
        
class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'