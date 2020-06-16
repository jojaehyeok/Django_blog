from django.db import models

# Create your models here.
class Rankingdata(models.Model):
    Rank_risk = models.IntegerField()
    Cor_name = models.IntegerField()
    area = models.CharField(max_length=15)
    Cor_Risk = models.FloatField()

    def __str__(self):
        return self.Cor_name

class Chartdata(models.Model):
    first_quarter_risk = models.FloatField()
    second_quarter_risk = models.FloatField()
    third_quarter_risk = models.FloatField()
    quarter_risk = models.FloatField()

class GJ_risk(models.Model):
    Risk = models.FloatField()
    Cor_code = models.IntegerField()
    ODD = models.IntegerField()
    PFS = models.IntegerField()
    DMR = models.IntegerField()
    ETC = models.IntegerField()

    def __str__(self):
        return self.Cor_code


class JN_risk(models.Model):
    Risk = models.FloatField()
    Cor_code = models.IntegerField()
    ODD = models.IntegerField()
    PFS = models.IntegerField()
    DMR = models.IntegerField()
    ETC = models.IntegerField()

    def __str__(self):
        return self.Cor_code