from django.db import models

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length = 40, blank = False)
    desription = models.TextField(max_length = 500, blank = False)
    url = models.CharField(max_length = 40, blank = False)

class Comment(models.Model):
    post = models.ForeignKey(Movie ,on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
