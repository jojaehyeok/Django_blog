from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=10)
    introdution = models.TextField()
    area = models.CharField(max_length=20)
    party_nuber = models.IntegerField(default=0)
    
    def __str__(self):
        return self_name

class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length = 15)
    

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE) #Poll 모델의 id를 이용
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    votes = models.IntegerField(default = 0)


class Product(models.Model):
    name = models.CharField(max_length=50)
    alergy = models.CharField(max_length=50)
    nutrition1= models.IntegerField(default=0)
    nutrition2= models.IntegerField(default=0)
    nutrition3= models.IntegerField(default=0)
    nutrition4= models.IntegerField(default=0)
    nutrition5= models.IntegerField(default=0)
    nutrition6= models.IntegerField(default=0)
    img_thumb= models.CharField(max_length=50)

