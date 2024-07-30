# REST APIs Kata

In this kata we are adding APIs for querying and updating the database model.

1. Create model serializers
2. Create model view sets
3. URL Routing for the `posts` application
4. Include posts application url routes into the project routes


Pre-requisites:

* [Blog Models](kata-blog-models.md)

## Create Model Serializers


```python
# posts/serializers.py

from rest_framework import serializers
from .models import Post, Comment, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'created_at', 'updated_at', 'tags']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'body', 'author', 'created_at', 'updated_at']
```

## Create Model View Sets


```python
# posts/views.py

from rest_framework import viewsets
from .models import Post, Comment, Tag
from .serializers import PostSerializer, CommentSerializer, TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
```

## URL Routing for the `posts` application


```python
# posts/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, TagViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

```

## Include posts application url routes into the project routes

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
]
```
