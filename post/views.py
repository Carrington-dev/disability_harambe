from django.shortcuts import render
from . models import *
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# def post_view(request):
#     posts = Post.objects.all()
#     context = {
#         "posts": Post.objects.all(),
#         "title": "title"
#     }
#     return render(request, "post/post_list.html", context)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='post/post_list.html'
    ordering = ["-date_posted"]
    paginate_by = 3
    # title = "News"


    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['title'] = "News"
        
        return context





class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name='post/post_detail.html'
    context_object_name = 'post'



    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        context['texts'] = Text.objects.all()
        context['files'] = File.objects.all()
        context['images'] = Image.objects.all()
        return context




class PostCreateView(LoginRequiredMixin, DetailView):
    model = Post
    fields = ['title', 'content','thumbnail']
    template_name='post/post_form.html'


    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)