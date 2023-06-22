from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse

# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Index page GET')
#     # 나머지 요청
#     # 에러, 예외처리
#     return HttpResponse('No!!!')

# 일반 뷰로 만든것
### Post
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

class Update(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:list')
    # initial 기능
    def get_initial(self):
        initial = super().get_initial() # UpdateView에서 제공하는 initial(딕셔너리 형태)
        post = self.get_object() # pk 기반으로 객체를 가져옴
        initial['title'] = post.title
        initial['content'] = post.content
        return initial

    def get_success_url(self):
        post = self.get_object() # pk 기반으로 현재 객체 가져오기
        return reverse('blog:detail', kwargs={'pk': post.pk})


class Delete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')


### Comment
class CommentWrite(View):
    # def get(self, request):
    #     pass
    def post(self, request, post_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            # 사용자에게 댓글 내용을 받아옴
            content = form.cleaned_data['content']
            # 해당 아이디에 해당하는 글 불러옴
            post = Post.objects.get(pk=post_id)
            # 댓글 객체 생성
            comment = Comment.objects.Create(post=post, content=content) # 데이터베이스에 직접 접근하여 create한 것이므로 변수 save를 해줄 필요가 없음
            return redirect('blog:list', pk=post_id)