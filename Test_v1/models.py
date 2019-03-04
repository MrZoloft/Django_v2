from django.db import models

# Create your models here.
# 新建一个人 的类 继承model


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete='True')
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

#  QuerySet 是可以用pickle序列化到硬盘再读取出来的
# import pickle
# query = pickle.load(s)
# qs = Mymodel.objects.all()
# qs.query = query
# QuerySet 重复的问题，使用 .distinct() 去重
#
#    qs1 = Pathway.objects.filter(label__name='x')
# qs2 = Pathway.objects.filter(reaction__name='A + B >> C')
# qs3 = Pathway.objects.filter(inputer__name='WeizhongTu')
#
# # 合并到一起
# qs = qs1 | qs2 | qs3
# 这个时候就有可能出现重复的
# # 去重方法
# qs = qs.distinct()
#

# from_db_value 函数用于转化数据库中的字符到 Python的变量
# to_python 函数用于转化数据库中的字符到 Python的变量，
# get_prep_value 用于将Python变量处理后(此处为压缩）保存到数据库，使用和Django自带的 Field 一样
class CompressedTextField(models.TextField):

    def from_db_value(self,value,expression,connection,context):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def to_python(self, value):
        if not value:
            return value
        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def get_prep_value(self, value):
        if not value:
            return value
        try:
            value.decode('base64')
            return value
        except Exception:
            try:
                return value.encode('utf-8').encode('bz2').encode('base64')
            except Exception:
                return value

