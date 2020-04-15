from django.contrib import admin
from .models import BlogType, Blog, ReadNum

# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id','title','blog_type','author','get_read_num','created_time','last_updated_time')

'''
@admin.register(ReadNum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('read_num','blog')
'''
=======
    list_display = ('title','blog_type','author','get_read_num','created_time','last_updated_time')

@admin.register(ReadNum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('read_num','blog')
>>>>>>> a9735adcc420ed4a62558be10f66d5166a36f84c
