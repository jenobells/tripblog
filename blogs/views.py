from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Blog


# Create your views here.
def home(request):
    blog = Blog.objects.all()
    return render(request, 'blogs/blogs.html', {'blogs':blog})

def blogs_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "GET":
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.posted_by = request.user
            blog.save()
            return redirect('/', pk=job.pk)
    else:
        form = JobForm(instance=job)
    return render(request, 'blogs/blogs_detail.html', {'form': form})
