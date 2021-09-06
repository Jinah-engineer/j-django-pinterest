# Routing - 특정 주소를 들어갔을 때, view 를 돌려줘야 한다
# 특정 주소를 만들어주는 작업 = urls.py
# 제일 먼저 요청을 받는 파일 !!!
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
    path('accounts/', include('accountapp.urls')),  # accountapps.urls.py 의 파일을 참조하여 안에서 다시 분기를 하는
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

