from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import DeleteView, FormView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm

# Page restriction (mixins)
from django.contrib.auth.mixins import LoginRequiredMixin
# for registering (and simultaneously loging in) a new user - with FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Login Authentication. This should be in the main/base app
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)


# Create your views here.
class IndexView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'index.html'
    # context_object_name = 'posts'  # customizing the django 'object_list' (now 'tasks') used in the html file
    
    # # get only the individual user's data
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["object_list"] = context["object_list"].filter(user=self.request.user)
    #     return context


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'

    # def get_queryset(self, pk):
    #     queryset = super(PostDetailView, self).get_queryset(id=self.pk)
    #     # print(queryset)
    #     post = Post.objects.all()
    #     comments = Comment.objects.filter(post=post)
    #     return queryset

    # def get_context_data(self, **kwargs):
    #     context = super(PostDetailView, self).get_context_data(**kwargs)
    #     if self.request.method == "POST":
    #         comment_form = CommentForm(self.request.POST or None)
    #         if comment_form.is_valid():
    #             comment = comment_form.save(commit=False)
    #             comment.post = post
    #             comment.save()
    #     else:
    #         comment_form = CommentForm()
    #         context['post'] = post.objects.all()
    #         context['comments'] = comments.objects.all()
    #         context['comment_form'] = comment_form()        
    #         template_name = 'post_detail.html'

    #     return render(self.request, template_name, context)


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = '__all__'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('home')
    template_name = 'post_confirm_delete.html'
