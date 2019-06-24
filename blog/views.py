from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from blog.models import Blog, Author, Tag, Comment

def index(request):
    """View function for home page of site."""
    num_blogs = Blog.objects.all().count()
    num_authors = Author.objects.count()
    context = {
        'num_blogs': num_blogs,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.ListView):
    model = Blog
    paginate_by = 5
    template_name ='blog/author_detail.html'
    
    def get_queryset(self):
        id = self.kwargs['pk']
        author=get_object_or_404(Author, pk = id)
        return Blog.objects.filter(author=author)
        
    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['name'] = get_object_or_404(Author, pk = self.kwargs['pk'])
        return context

class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})