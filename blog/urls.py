from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path("", views.index), # FBV방법
    # 글 목록 조회
    path("", views.Index.as_view(), name='list'),
    # 글 작성
    path("write/", views.write, name='write'),
    # 글 수정
    # 글 삭제
    # 코멘트 작성
    # 코멘트 삭제
]