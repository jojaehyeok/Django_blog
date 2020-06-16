from django.shortcuts import render
from .models import models
from .models import Rankingdata, GJ_risk, JN_risk
from . import views

# Create your views here.
def test_page(request):
    return render(request, 'chart/home.html')

def chart_page(request):
    return render(request, 'chart/chart.html')

def main_page(request):
    return render(request, 'chart/main.html')

# def detail_page(request) : #어떤 지역인지를 매개변수 area로 받습니다.
#     return render(request, 'chart/detail.html')
# def detail_page(request):
#     return render(request, 'chart/detail.html')
     
# Create your views here.
def index(request):
    Rankingdatas = Rankingdata.objects.all()
    context = {'Rankingdatas': Rankingdatas }
        #context에 모든 어린이 정보를 저장
    return render(request, 'chart/home.html', context)
        #context안에 있는 어린이 정보를 chart.html로 전달

# Create your views here.
def GJ_index(request):
    GJ_data = GJ_risk.objects.all()
    context = {'GJ_data': GJ_data }
        #context에 모든 어린이 정보를 저장
    return render(request, 'chart/detail.html', context)
        #context안에 있는 어린이 정보를 chart.html로 전달

def JN_index(request):
    JN_data = JN_risk.objects.all()
    context = {'JN_data': JN_data }
        #context에 모든 어린이 정보를 저장
    return render(request, 'chart/JN.html', context)
        #context안에 있는 어린이 정보를 chart.html로 전달


def search(request):
    br = Rankingdata.objects.all() # 모든 Rankingdatas 테이블의 모든 object들을 br에 저장하라

    b = request.GET.get('b','') # GET request의 인자중에 b 값이 있으면 가져오고, 없으면 빈 문자열 넣기

    if b: # b에 값이 들어있으면 true
        br = br.filter(Cor_name__icontains=b) # 의 title이 contains br의 title에 포함되어 있으면 br에 저장

    return render(request, 'chart/search.html', {'search':br , 'b':b})
    # br에는 Border 테이블에 title 이름이 'Singapore'인 데이터들이 들어있고,
    # b에는 내가 처음에 입력했던 'Singapore'가 들어있다.
        
