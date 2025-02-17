from django.shortcuts import render
from django.views import View
from .models import Blog, Tags, Comments

class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        tags = Tags.objects.all()
        context = {
            'blogs': blogs,
            'tags' : tags
        }
        return render(request, 'blogs.html', context)

class BlogDetailView(View):
    def get(self, request, id):
        blog = Blog.objects.get(id=id)
        comments = Comment.objects.filter(blog=blog)
        context = {
            'blog' : blog,
            'comments' : comments
        }
        return render(request, 'blog_detail.html', context)
# Create your views here.
