# posts/serializers.py

from rest_framework import serializers
from .models import Post, Comment, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_names = serializers.ListField(
        child=serializers.CharField(max_length=30), write_only=True
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'created_at', 'updated_at', 'tags', 'tag_names']

    def validate_tag_names(self, value):
        existing_tags = Tag.objects.values_list('name', flat=True)
        invalid_tags = [name for name in value if name not in existing_tags]
        if invalid_tags:
            raise serializers.ValidationError(f"These tags do not exist: {', '.join(invalid_tags)}")
        return value

    def create(self, validated_data):
        tag_names = validated_data.pop('tag_names', [])
        post = Post.objects.create(**validated_data)
        self._save_tags(post, tag_names)
        return post

    def update(self, instance, validated_data):
        tag_names = validated_data.pop('tag_names', [])
        instance = super().update(instance, validated_data)
        self._save_tags(instance, tag_names)
        return instance

    def _save_tags(self, post, tag_names):
        tags = Tag.objects.filter(name__in=tag_names)
        post.tags.set(tags)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "post", "body", "author", "created_at", "updated_at"]
