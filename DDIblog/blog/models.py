from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['-time']

    def get_absolute_url(self):
        return "/blog/%i" % self.id


class Comment(models.Model):
    path = models.CharField(max_length=200, unique=True)
    post_id = models.ForeignKey(Post)
    author_id = models.ForeignKey(User)
    content = models.TextField('Комментарий')
    pub_date = models.DateTimeField('Дата комментария', auto_now_add=True)

    def get_offset(self):
        path_list = self.path.split(' ')
        level = len(path_list) - 1
        if level > 5:
            level = 5
        return level

    def get_col(self):
        path_list = self.path.split(' ')
        level = len(path_list) - 1
        if level > 5:
            level = 5
        return 12 - level

    class Meta:
        db_table = "comments"
        ordering = ['path']