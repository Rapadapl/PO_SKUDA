from rest_framework import serializers
from .models import Log,Card,User,Level,Reader,SBC

class LogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Log
		fields = ('id','logDatetime','logAction','logResult','logCard','logUser','logLevel','logReader','logSbc')

class CardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Card
		fields = ('id','cardType','cardUser')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','userType','userFIO','userLevel')

class LevelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Level
		fields = ('id','levelDesc','levelReader')

class ReaderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reader
		fields = ('id','readerType','readerStatus','readerSbc')  

class SBCSerializer(serializers.ModelSerializer):
	class Meta:
		model = SBC
		fields = ('id','sbcStatus')  
