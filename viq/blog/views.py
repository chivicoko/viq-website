from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
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


class CreatePostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = '__all__'


class PostDelete(DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('home')
    template_name = 'post_confirm_delete.html'
