from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post

class ChirpListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.order_by('-post_date')

class ChirpDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['post_text', 'author']
    success_url = reverse_lazy('home')
        
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.getobject()
        return self.request.user == obj.username

