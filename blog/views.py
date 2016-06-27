from django.shortcuts import render
from django.utils import timezone
from .models import Post    # .은 현재 디렉토리 도는 현재 어플리케이션을 의미합니다.

# Create your views here.
def post_list(request):
    # published_date 와 lte 사이에 밑줄(_) 이 2개입니다. 필드 이름('published_date')과 연산자의 필터('lte')를 밑줄 2개를 사용해 구분합니다.
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html',{'posts': posts})
