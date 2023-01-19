from django.db import models 

class mma(models.Model):

	name = models.CharField(max_length=50)	
	nickname = models.CharField(max_length=50)			
	wins = models.IntegerField()		
	loses = models.IntegerField()			
	ties = models.IntegerField()	
