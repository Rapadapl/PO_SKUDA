from rest_framework import viewsets
#from rest_framework import views, generics, response, permissions, authentication
from .models import Log, Card, User, Level, Reader, SBC
from rest_framework.decorators import action
from .serializers import LogSerializer, CardSerializer, UserSerializer, \
        LevelSerializer, ReaderSerializer, SBCSerializer
#from .serializers import DbUserSerializer, LoginSerializer
from rest_framework.response import Response
#from django.contrib.auth import login, logout
#from django.conf import settings
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import LoginSerializer, RegistrationSerializer

class LogsViewSet(viewsets.ModelViewSet):
    serializer_class = LogSerializer
    queryset = Log.objects.all()


class CardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    @action(methods=['post'], detail=False, url_path='card-validation', url_name='card_validation')
    def card_validation(self, request, pk=None):
        validation = request.data.get('id')
        validation_result = self.queryset.filter(pk=validation)
        return Response({"result":validation_result.exists()})
    
class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=['post'], detail=False, url_path='level-list', url_name='level_list')
    def find_reader_query(self, request, pk=None):
        finder = request.data.get("level")
        return Response({"result":UserSerializer(self.queryset.filter(userLevels=finder), many=True).data})

class LevelsViewSet(viewsets.ModelViewSet):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()


class ReadersViewSet(viewsets.ModelViewSet):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()

    @action(methods=['post'], detail=False, url_path='level-list', url_name='level_list')
    def find_reader_query(self, request, pk=None):
        finder = request.data.get("level")
        return Response({"result":ReaderSerializer(self.queryset.filter(readerLevel=finder), many=True).data})
    
    @action(methods=['post'],detail=False, url_path='sbc-list',\
            url_name='sbc_list')
        
    def find_sbc_query(self, request, pk=None):
        finder = request.data.get("sbc")
        return Response({"result":ReaderSerializer(self.queryset.filter(readerSbc=finder), many=True).data})
    
    @action(methods=['post'],detail=False, url_path='open-reader',\
            url_name='open-reader')
        
    def open_reader_by_id(self, request, pk=None):
        finder = request.data.get("id")
        return Response({"result":"door_opened", "dest":ReaderSerializer(self.queryset.filter(pk=finder), many=True).data})
    

class SBCsViewSet(viewsets.ModelViewSet):
    serializer_class = SBCSerializer
    queryset = SBC.objects.all()
    
    
    
    
class RegistrationAPIView(APIView):

    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
'''    
class SessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return response.Response(DbUserSerializer(user).data)


class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return response.Response()


class RegisterView(generics.CreateAPIView):
    serializer_class = DbUserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        login(self.request, user)


class UserView(generics.RetrieveAPIView):
    serializer_class = DbUserSerializer
    lookup_field = 'pk'

    def get_object(self, *args, **kwargs):
        return self.request.user
'''