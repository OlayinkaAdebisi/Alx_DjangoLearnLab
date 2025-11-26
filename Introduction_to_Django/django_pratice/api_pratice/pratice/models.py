from django.db import models

# Create your models here.
class user(models.Model):
    first_name = (models.CharField(max_length=20))
    last_name = (models.CharField(max_length=20))
    
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.fullname} on {self.blog_post.title}"
   
