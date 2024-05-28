from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from utils.models import BaseModel

User = get_user_model()


class Category(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(BaseModel):
    class PostManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_published=True)

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')

    image = models.ImageField(upload_to="images/%Y/%m/%d")
    content = models.TextField()
    views = models.IntegerField(default=0)

    recommended = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    tags = TaggableManager()
    objects = models.Manager()
    published = PostManager()

    class Meta:
        ordering = ('-created_at',)
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='comments')
    content = models.CharField(max_length=511)

    class Meta:
        ordering = ('-created_at',)
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def __str__(self):
        return f"Comment(pk={self.pk})"
