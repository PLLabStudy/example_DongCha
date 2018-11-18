from django.shortcuts import render



# Create your views here.
def donghyun(request):
    a ="안녕하세요 인덱스 페이지입니다."
    send_varilbe ={
        'a': a,
        'b': "할수이따아아앙"
    
    }
    return render(request, "index.html", send_varilbe)




