from rest_framework import serializers
from taggit.models import Tag
from . import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'slug'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            'id',
            'title',
            'slug',
            'created_at',
            'updated_at',
        )


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = models.Post
        tags = TagSerializer(many=True)

        fields = (
            'id',
            'slug',
            'title',
            'category',
            'author',
            'image',
            'content',
            'views',
            'tags',
            'created_at',
            'updated_at',
            'recommended',
            'is_published',
        )


class PostCreateSerializer(serializers.ModelSerializer):
    tags_id = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), write_only=True)

    class Meta:
        model = models.Post
        fields = (
            'title',
            'content',
            'category',
            'image',
            'tags_id',
        )

    def create(self, validated_data):
        tags = validated_data.pop('tags_id')
        post = models.Post.objects.create(tags=tags, **validated_data)
        return post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = (
            'post',
            'owner',
            'content',
            'created_at',
            'updated_at'
        )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = (
            'post',
            'content',
        )
