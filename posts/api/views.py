from rest_framework import viewsets
from ..models import Post
from .serializers import PostSerialier

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerialier
