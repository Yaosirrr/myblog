from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from read_statistics.models import ReadNumExpandMethod
=======
from django.db.models.fields import exceptions
>>>>>>> a9735adcc420ed4a62558be10f66d5166a36f84c

# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)
    def __str__(self):
        return self.type_name

class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def get_read_num(self):
        try:
            return self.readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

    def __str__(self):
        return '<Blog: %s>' % self.title

<<<<<<< HEAD
'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING) #一对一的字段，Foreignkey为多对一/一对多
'''
=======
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING) #一对一的字段，Foreignkey为多对一/一对多

>>>>>>> a9735adcc420ed4a62558be10f66d5166a36f84c




















