from rest_framework import viewsets
from .models import Log, Card, User, Level, Reader, SBC
from rest_framework.decorators import action
from .serializers import LogSerializer, CardSerializer, UserSerializer, \
LevelSerializer, ReaderSerializer, SBCSerializer
from rest_framework.response import Response

		
class LogsViewSet(viewsets.ModelViewSet):
    serializer_class = LogSerializer
    queryset = Log.objects.all()

class CardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    
    @action(methods=['post'],detail=False, url_path='card-validation',\
            url_name='card_validation')
    
    def card_validation(self, request, pk=None):
            validation = request.data.get('id')
            validation_result = Card.objects.filter(pk=validation)
            return Response({"result":validation_result.exists()})
    
class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
     
    @action(methods=['post'],detail=False, url_path='level-list',\
            url_name='level_list')
        
    def find_reader_query(self, request, pk=None):
        finder = request.data.get("level")
        result = Reader.objects.all()
        return Response({"result":ReaderSerializer(result.filter(readerLevel=finder), many=True).data})
    
class LevelsViewSet(viewsets.ModelViewSet):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    

    
class ReadersViewSet(viewsets.ModelViewSet):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()
    
    @action(methods=['post'],detail=False, url_path='level-list',\
            url_name='level_list')
        
    def find_reader_query(self, request, pk=None):
        finder = request.data.get("level")
        result = Reader.objects.all()
        #print(result.filter(readerLevel="3"))
        return Response({"result":ReaderSerializer(result.filter(readerLevel=finder), many=True).data})
    
    @action(methods=['post'],detail=False, url_path='sbc-list',\
            url_name='sbc_list')
        
    def find_sbc_query(self, request, pk=None):
        finder = request.data.get("sbc")
        result = Reader.objects.all()
        #print(result.filter(readerLevel="3"))
        return Response({"result":ReaderSerializer(result.filter(readerSbc=finder), many=True).data})
    

class SBCsViewSet(viewsets.ModelViewSet):
    serializer_class = SBCSerializer
    queryset = SBC.objects.all()
    
    
    