from django.shortcuts import (render,
                              get_object_or_404)
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models  import BlogPost
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin



class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    # paginate_by = 5


class PostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'image','content']
    def get_success_url(self):
        return reverse('Blog_home')

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)