from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# 创建博客的文章类


# class Article(models.Model):
#     title = models.CharField('标题',max_length=256)
#     content = models.TextField('内容')
#     pub_date = models.DateTimeField('发表时间',auto_now_add=True,editable=True)
#     update_time = models.DateTimeField('更新时间',auto_now_add=True,null=True)
#
#     def __str__(self):
#         return self.title

# 博客具有文章 分类和标签


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=False)
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，
    # 专门用于处理网站用户的注册、登录等流程，
    # User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，
    # 而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似
    author = models.ForeignKey(User, on_delete=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    #  通过内部类指定 一些指定的属性
    class Meta:
        ordering = ['-created_time']



# user = User.objects.filter(is_superuser=True)
# print(user)