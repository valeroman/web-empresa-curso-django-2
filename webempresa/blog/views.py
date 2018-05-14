from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    post = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':post})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)    # El get permite recoger un unico registro filtrando por el id
    return render(request, "blog/category.html", {'category':category}) 