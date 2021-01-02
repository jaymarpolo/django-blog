from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import *
from .forms import *


class HomeView(generic.ListView):
    model = Post
    template_name = 'post/home.html'
    ordering = ['-date']


class CategoryView(generic.ListView):
    model = Category
    template_name = 'post/home.html'


def likes(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post:detail', args=[str(pk)]))


class DetailPostView(generic.DetailView):
    model = Post
    template_name = 'post/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class CreatePostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/create.html'


class AddCommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/comment.html'
    success_url = reverse_lazy('post:home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/update.html'


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('post:home')


class CreateCategoryView(generic.CreateView):
    model = Category
    fields = '__all__'
    template_name = 'post/add-category.html'


def category(request, cat):
    categories = Post.objects.filter(category=cat)
    context = {'cat': cat, 'categories': categories}
    return render(request, 'post/category.html', context)
    

def categoryList(request):
    cat_menu = Category.objects.all()
    return render(request, 'post/list-category.html', {'cat_menu': cat_menu})
