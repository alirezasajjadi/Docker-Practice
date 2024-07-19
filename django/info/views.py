from django.shortcuts import render, redirect
from .models import Post


def home(request):
    if request.method == "POST":
        title = request.POST.get("title")    
        body = request.POST.get("body")
        Post.objects.create(title=title, body=body)
        return redirect('home')
    else :
        posts = Post.objects.all()
        return render(request=request, template_name='info/home.html', context={"posts": posts})