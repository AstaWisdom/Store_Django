from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(blank=False, null=False)
    video = models.FileField(upload_to='video/%y/%m/%d', null=True, blank=True)
    body = RichTextUploadingField()
    body_explain = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, blank=False, null=False)

    def save(self, *args, **kwargs):
        slug = slugify(self.slug)
        has_slug = Post.objects.filter(slug=slug).exists()
        count = 1
        while has_slug:
            count += 1
            slug = slugify(self.slug) + '-' + str(count)
            has_slug = Post.objects.filter(slug=slug).exists()

        self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        if len(self.text) > 100:
            return f"{self.post} // {self.text[0:50]}"
        else:
            return f"{self.post}// {self.text}"

