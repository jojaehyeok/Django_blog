from django.db import models


class CorFeatures(models.Model):
    date = models.DateField(db_column='Date', primary_key=True)  # Field name made lowercase.
    cor_code = models.ForeignKey('Corporates', models.DO_NOTHING, db_column='Cor_code')  # Field name made lowercase.
    perform_fund_situation = models.IntegerField(db_column='Perform_Fund_Situation', blank=True, null=True)  # Field name made lowercase.       
    outlook_dom_demand = models.IntegerField(db_column='Outlook_Dom_Demand', blank=True, null=True)  # Field name made lowercase.
    delay_money_recovery = models.IntegerField(db_column='Delay_Money_Recovery', blank=True, null=True)  # Field name made lowercase.
    difficulty_financing = models.IntegerField(db_column='Difficulty_Financing', blank=True, null=True)  # Field name made lowercase.
    perform_oper_profit = models.IntegerField(db_column='Perform_Oper_Profit', blank=True, null=True)  # Field name made lowercase.
    competition_corporates = models.IntegerField(db_column='Competition_Corporates', blank=True, null=True)  # Field name made lowercase.       
    outlook_business = models.IntegerField(db_column='Outlook_Business', blank=True, null=True)  # Field name made lowercase.
    difficulty_manpower = models.IntegerField(db_column='Difficulty_Manpower', blank=True, null=True)  # Field name made lowercase.
    rise_labor_costs = models.IntegerField(db_column='Rise_Labor_Costs', blank=True, null=True)  # Field name made lowercase.
    outlook_export = models.IntegerField(db_column='Outlook_Export', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cor_features'
        unique_together = (('date', 'cor_code'),)
    
class Corporates(models.Model):
    cor_code = models.IntegerField(db_column='Cor_code', primary_key=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'corporates'

class CorRisk(models.Model):
    risk_bankruptcy = models.FloatField(db_column='Risk_Bankruptcy', blank=True, null=True)  # Field name made lowercase.
    cor_code = models.IntegerField(db_column='Cor_code', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cor_risk'
        unique_together = (('cor_code', 'date'),)

 
# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
        #context에 모든 어린이 정보를 저장
    return render(request, 'chart/home.html', context)
        #context안에 있는 어린이 정보를 index.html로 전달
