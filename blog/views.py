from django.shortcuts import render

from blog.models import Post


def test_view(request):
    allpost = Post.objects.all
    return render(request, 'main.html', {'allpost': allpost})
