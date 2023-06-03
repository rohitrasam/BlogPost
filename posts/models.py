from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STATUS = ((0, 'Draft'), (1, "Published"))
class Post(models.Model):


    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    content = models.TextField(default="")
    creation_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ('-published_date',)

    def __str__(self):
        return f"{self.title}"