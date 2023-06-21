from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Index page GET')
#     # 나머지 요청
#     # 에러, 예외처리
#     return HttpResponse('No!!!')

class Index(View):
    def get(self, request):
        # return HttpResponse('Index page GET class')
        # 데이터베이스에 접근해서 값을 가져와야 합니다.
        # 게시판에 글들을 보여줘야하기 때문에 데이터베이스에서 "값 조회" 기능을 사용해야함
        # MyModel.objects.all()
        post_objs = Post.objects.all()
        context = {
            "posts": post_objs
        }
        # context = 데이터베이스에서 가져온 값
        return render(request, 'blog/board.html', context)

# write
# post - form
# 글 작성 화면
def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('/blog:list')
    else:
        form = PostForm()
        return render(request, 'blog/write.html', {'form': form})

# django.views.generic -> ListView
class List(ListView):
    model = Post
    template_name = 'blog/post_list.html' #템플릿
    context_object_name = 'posts' # 변수 값의 이름


class Write(CreateView):
    model = Post # 모델
    form_class = PostForm # 폼
    success_url = reverse_lazy('blog:list') # 성공시 보내줄 url

class Detail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'