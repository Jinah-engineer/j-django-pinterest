from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # django 에서 기본으로 제공하는 (ctrl + b)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Check if authenticated
# Check request valid
# Collect data from DB
# Render response
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm

"""
    Account
        1. Sign Up
        2. View info
        3. Change info
        4. Quit
"""
"""
    Class Based View (CBV)
    Function Based View (FBV)
"""
# def = define
# request 를 넣어서 response 에 답해준다
from django.urls import reverse, reverse_lazy

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST": # request 요청이 post 일 경우

        # request 중 POST request 에서 'hello_world_input' 이라는 name 의 input 을  가져온다
        temp = request.POST.get('hello_world_input')

        # models.py 에서 나온 HelloWorld 객체
        new_hello_world = HelloWorld()
        new_hello_world.text = temp # 변수의 text value
        new_hello_world.save()

        # data 전송이 종료되면 다시 GET 요청으로 돌아가게 한다
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else: # get 요청일 경우에
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


"""
    HTTP Protocol (request / response)
    : additional Data 를 처리하는 방식
    - GET -- inquiry (조회). 주소 안에 parameter 를 넣어서 처리해준다
    - POST -- create, update. 서버 내에 정보를 만들거나 수정할 때. 추가적으로 body 응답 내부에 있는 몸통에 data 를 넣어서 보낸다. 
    
"""

# 회원가입
class AccountCreateView(CreateView):
    model = User
    # User model 을 만드는 데 필요한 form
    form_class = UserCreationForm
    # 계정을 만드는 데 성공했다면 어느 경로로 보내줄 지
    success_url = reverse_lazy('accountapp:hello_world') # reverser_lazy 는 class base view 에서 사용
    # 어느 html file 을 이용해서 볼 지
    template_name = 'accountapp/create.html'

# 회원정보
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/user_detail.html'

# 계정정보 수정
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

# 계정 삭제
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'