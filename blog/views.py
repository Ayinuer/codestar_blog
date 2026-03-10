from django.views import generic
from .models import Post

class PostList(ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 6