from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

class Tag(models.Model):
    caption = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinValueValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)


