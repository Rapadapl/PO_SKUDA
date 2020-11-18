from rest_framework import serializers
from .models import Log,Card,User,Level,Reader,SBC, DbUser
from django.contrib.auth import authenticate
#from .validators import validate_username

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
		fields = ('id','userType','userFIO','userLevels')

class LevelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Level
		fields = ('id','levelDesc',)

class ReaderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reader
		fields = ('id','readerType','readerStatus','readerSbc', 'readerLevel')  

class SBCSerializer(serializers.ModelSerializer):
	class Meta:
		model = SBC
		fields = ('id','sbcStatus')  
        
        
class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = DbUser
        fields = ('email', 'username', 'password', 'token',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)       
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    # Ignore these fields if they are included in the request.
    username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'Нужен email чтобы войти.'
            )

        if password is None:
            raise serializers.ValidationError(
                'Нужен пароль чтобы войти'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Логин или пароль введены неверно.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'Этого пользователя удалили.'
            )

        return {
            'token': user.token,
        }        

'''
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}



class DbUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DbUser
        fields = (
            'id',
            'last_login',
            'email',
            'name',
            'is_active',
            'joined_at',
            'password'
        )
        read_only_fields = ('last_login', 'is_active', 'joined_at')
        extra_kwargs = {
            'password': {'required': True, 'write_only': True},
            'name': {'required': True}
        }

    @staticmethod
    def validate_email(value):
        return validate_username(value)

    def create(self, validated_data):
        return DbUser.objects.create_user(
                    validated_data.pop('email'),
                    validated_data.pop('password'),
                    **validated_data
                )
 '''