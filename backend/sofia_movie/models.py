from django.db import models
from django.utils.text import slugify
# Create your models here.


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    embedded_link = models.URLField(null=True)
    movie_duration = models.TimeField()
    country_short = models.CharField(max_length=2)
    thumbnail = models.URLField()
    # need to remove null in production
    download_link = models.URLField(null=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True)
    status = models.BooleanField(default=True)
    upload_datetime = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
