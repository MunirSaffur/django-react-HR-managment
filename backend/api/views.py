from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from dayoff.models import DayOff, Users
from .serializers import DayOffSerializer, UsersSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
@api_view(['GET'])
def getApi(request):
    urls = ['one', 'tow']
    
    return Response(urls)
 
@api_view(['GET'])
def getUsers(request):
    users = Users.objects.all()
    admin_team = [item.name for item in request.user.team.all()]
    
    for user in users:
        if user.name in admin_team:
            user.editable = True
            
    serializer = UsersSerializer(users,many=True)
    return Response(serializer.data)   


@swagger_auto_schema(methods=['GET','POST'], operation_summary="Retrieve some data", operation_description="Retrieve data with authentication required.", security=[{"Bearer Token": []}])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def getDaysOff(request):
    if request.method == 'GET':
        user = request.user
        dayoff = user.dayoff_set.all()
        serializer = DayOffSerializer(dayoff,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DayOffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['GET'], operation_summary="Retrieve some data", operation_description="Retrieve data with authentication required.", security=[{"Bearer Token": []}])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getDayOff(request, pk):
    dayoff = DayOff.objects.get(id=pk)
    serializer = DayOffSerializer(dayoff,many=False)
    return Response(serializer.data)

@swagger_auto_schema(methods=['DELETE'], operation_summary="Retrieve some data", operation_description="Retrieve data with authentication required.", security=[{"Bearer Token": []}])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def deleteDayOff(request, pk):
    try:
        dayoff = DayOff.objects.get(id=pk)
    except DayOff.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        dayoff.delete()
        
    return Response("Izin basaliyla silindi")

@swagger_auto_schema(methods=['PUT'], operation_summary="Retrieve some data", operation_description="Retrieve data with authentication required.", security=[{"Bearer Token": []}])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def updateDayOff(request, pk):
    try:
        instance = DayOff.objects.get(id=pk)
    except DayOff.DoesNotExist:
        return Response({"message": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DayOffSerializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
