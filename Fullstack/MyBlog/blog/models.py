from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    title = models.CharField(max_length=128)
    text = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)
    posted_at = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.posted_at = timezone.now()
        self.save()
        
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.title
    
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
        
    def get_absolute_url(self):
        return reverse("post_list")
    
        
    def __str__(self):
        return self.text
    
    
