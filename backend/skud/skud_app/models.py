from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  def __str__(self):
        return self.title
class Article(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  body = models.TextField()
  author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)
  def __str__(self):
        return self.title
        
class Log(models.Model):
  #logID = models.CharField(max_length=255)
  logDatetime = models.DateTimeField()
  logAction = models.CharField(max_length=255)
  logResult = models.CharField(max_length=255)
  logCard = models.ForeignKey('Card',related_name='cards',on_delete=models.CASCADE)
  logUser = models.ForeignKey('User',related_name='users',on_delete=models.CASCADE)
  logLevel = models.ForeignKey('Level',related_name='levels',on_delete=models.CASCADE)
  logReader = models.ForeignKey('Reader',related_name='readers',on_delete=models.CASCADE)
  logSbc = models.ForeignKey('SBC',related_name='SBCs',on_delete=models.CASCADE)


class Card(models.Model):
  cardID = models.CharField(max_length=255)
  cardType = models.CharField(max_length=255)
  cardUser = models.ForeignKey('User', related_name='Сard_users', on_delete=models.CASCADE)
class User(models.Model):
  userID = models.CharField(max_length=255)
  userType = models.IntegerField()
  userLevel = models.ForeignKey('Level', related_name='User_levels', on_delete=models.CASCADE)
class Level(models.Model):
  levelID = models.CharField(max_length=255)
  levelDesc = models.CharField(max_length=255)
  levelReader = models.ForeignKey('Reader',related_name='Level_readers',on_delete=models.CASCADE)
class Reader(models.Model):
  readerID = models.CharField(max_length=255)
  readerType = models.CharField(max_length=255)
  readerStatus = models.CharField(max_length=255) 
  readerSbc = models.ForeignKey('SBC',related_name='Reared_SBCs',on_delete=models.CASCADE)
class SBC(models.Model):
  sbcID = models.CharField(max_length=255)
  sbcStatus = models.CharField(max_length=255) 
