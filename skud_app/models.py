from django.db import models
import jwt
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core import validators
        
class Log(models.Model):
  logDatetime = models.DateTimeField()
  logAction = models.CharField(max_length=255)
  logResult = models.CharField(max_length=255)
  logCard = models.ForeignKey('Card',related_name='cards',on_delete=models.CASCADE)
  logUser = models.ForeignKey('User',related_name='users',on_delete=models.CASCADE)
  logLevel = models.ForeignKey('Level',related_name='levels',on_delete=models.CASCADE)
  logReader = models.ForeignKey('Reader',related_name='readers',on_delete=models.CASCADE)
  logSbc = models.ForeignKey('SBC',related_name='SBCs',on_delete=models.CASCADE)
  def __str__(self):
        return self.id

class Card(models.Model):
  id = models.CharField(max_length=255, primary_key=True, unique=True)
  cardType = models.CharField(max_length=255)
  cardUser = models.ForeignKey('User', related_name='Сard_users', on_delete=models.CASCADE)
  def __str__(self):
        return self.id

    
class Level(models.Model):
  id = models.CharField(max_length=255, primary_key=True, unique=True)
  levelDesc = models.CharField(max_length=255)
  #levelReader = models.ForeignKey('Reader',related_name='Level_readers',on_delete=models.CASCADE)
  def __str__(self):
        return self.levelDesc
    
class User(models.Model):
  id = models.CharField(max_length=255, primary_key=True, unique=True)
  userType = models.CharField(max_length=255)
  userFIO = models.CharField(max_length=255)
  #userLevel = models.ForeignKey('Level', related_name='User_levels', on_delete=models.CASCADE)
  userLevels = models.ManyToManyField(Level)
  def __str__(self):
        return self.userFIO
    
class Reader(models.Model):
  id = models.CharField(max_length=255, primary_key=True, unique=True)
  readerType = models.CharField(max_length=255)
  readerStatus = models.CharField(max_length=255) 
  readerSbc = models.ForeignKey('SBC',related_name='Reared_SBCs',on_delete=models.CASCADE)
  readerLevel = models.ForeignKey('Level',related_name='Reader_levels',on_delete=models.CASCADE)
  def __str__(self):
        return self.readerType
    
class SBC(models.Model):
  id = models.CharField(max_length=255, primary_key=True, unique=True)
  sbcStatus = models.CharField(max_length=255) 
  def __str__(self):
        return self.id

'''
class DbUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        now = timezone.now()
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            joined_at=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(**{'{}__iexact'.format(self.model.USERNAME_FIELD): username})

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)
'''
class DbUserManager(BaseUserManager):
    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Указанное имя пользователя должно быть установлено')

        if not email:
            raise ValueError('Данный адрес электронной почты должен быть установлен')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)




class DbUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True,blank=False, validators=[validators.validate_email])
    username = models.CharField( max_length=255, blank=False, unique=True)
    is_staff = models.BooleanField( default=False)
    is_active = models.BooleanField( default=True)
    joined_at = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = DbUserManager()

    def __str__(self):
        return self.username
    

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):

        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')