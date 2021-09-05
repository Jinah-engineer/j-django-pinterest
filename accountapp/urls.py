from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

# accountapp : hello_world/

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    # 로그인
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    # 로그아웃
    path('logout/', LogoutView.as_view(), name='logout'),

    # 회원가입
    path('create/', AccountCreateView.as_view(), name='create'),

    # 회원정보 상세
    # 특정 유저의 정보 - primary key 가 필요하다 - 몇 번 user 객체에 접근할 것인지 명시해주어야 한다
    path('user_detail/<int:pk>', AccountDetailView.as_view(), name='user_detail'),

    # 정보 수정
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),

    # 정보 삭제
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
