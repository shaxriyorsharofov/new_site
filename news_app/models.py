from django.db import models
from django.utils import timezone
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)
        # return super(PublishedManager, self).get_queryset().filter(status='Published')


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class News(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = "PB", 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    objects = models.Manager
    published = PublishedManager

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    text = models.TextField()

    def __str__(self):
        return self.name
    