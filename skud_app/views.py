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
#from rest_framework.permissions import IsAuthenticated
import requests as req

import _datetime

import pymssql 
 
class LogsViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = LogSerializer
    queryset = Log.objects.all()


class CardsViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    
    def create(self, request, *args, **kwargs):
        
        #conn = pymssql.connect("RAPADAPL-DESKTO", "User1", "123456789", "DemoBase")
        userOBJ = User.objects.all().filter(pk=request.data.get('cardUser')).values_list('id')[0]
        userID = userOBJ[0]
        #userFIO = userOBJ[1]
        
        cardType  = request.data.get("cardType")
        cardID = request.data.get("id")
        
        #cursor = conn.cursor()
        #
        #queryString = "INSERT INTO [dbo].[_InfoRg39027] ([_Fld39028RRef],[_Fld39029],[_Fld39030],[_Fld543]) VALUES("+ str(userID)+"," + " ' " + str(cardID)+ " ' " + ","+ " ' " + str(cardType) + " ' " +","+ str(0)+")"
        #print(queryString)               
        #cursor.execute(queryString)
        #conn.commit()
 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)    

    @action(methods=['post'], detail=False, url_path='card-validation', url_name='card_validation')
    def card_validation(self, request, pk=None):
        validation = request.data.get('id')
        validation_result = self.queryset.filter(pk=validation)
        
        y = int(_datetime.datetime.now(tz=None).strftime("%Y")) + 2000
        d = _datetime.datetime.now(tz=None).strftime("-%m-%d")
        t = _datetime.datetime.now(tz=None).strftime("%H:%M:%S")
        yd = str(y) + str(d) + " 00:00:00"
        dt = "2001-01-01 " + str(t)
        #print(yd)
        #print(dt)
        #conn = pymssql.connect("RAPADAPL-DESKTO", "User1", "123456789", "DemoBase")
        ans = ""
        if (request.data.get("readerID") == "0"):
            ans = "0xA499D07B7C508EC5448338A081408450"
        elif (request.data.get("readerID") == "1"):
            ans = "0x88ED61195DFB87A04E368B51E80EA847"
            
        cardID = request.data.get("id")
        #cursor = conn.cursor()
        if (validation_result.exists()):
            userID = User.objects.all().filter(pk=self.queryset.filter(pk=request.data.get("id")).values_list('cardUser')[0][0]).values_list('id')[0][0]
            queryString = "INSERT INTO [dbo].[_InfoRg39022] ([_Fld39032],[_Fld39023],[_Fld39024RRef],[_Fld39025RRef],[_Fld39026],[_Fld543]) VALUES("+ " ' " +str(yd)+" ' " + "," + " ' " + str(dt)+ " ' " + "," +  str(ans) +","+ str(userID)+","+ " ' "+str(cardID)+" ' " +","  +str(0)+ ")"      
            
            
            
            #print(queryString)
            #cursor.execute(queryString)
            #conn.commit()
            
            
            
            resp = req.post("http://127.0.0.1:8000/api/readers/open-reader/", json={"id":request.data.get("readerID")}, headers={'Content-Type':'application/json'} )
            print(resp.json())
        return Response({"result":validation_result.exists()})
    
class UsersViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    
    @action(methods=['post'], detail=False, url_path='level-list', url_name='level_list')
    def find_reader_query(self, request, pk=None):
        finder = request.data.get("level")
        return Response({"result":UserSerializer(self.queryset.filter(userLevels=finder), many=True).data})

class LevelsViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    serializer_class = LevelSerializer
    queryset = Level.objects.all()


class ReadersViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
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
        '''
        DO SMTH
        '''
        return Response({"result":"door_opened", "dest":ReaderSerializer(self.queryset.filter(pk=finder), many=True).data})
    

class SBCsViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
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
                #'token': serializer.data.get('token', None),
                'result':"Регистрация завершена"
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