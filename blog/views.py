from django.views import generic
from .models import Post

# Create your views here.class PostList(generic.ListView):
class PostList(generic.ListView):
    model = Post