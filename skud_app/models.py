from django.db import models
        
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