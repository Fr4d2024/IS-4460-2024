from django.contrib import admin

from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    pass    

admin.site.register(Post) 
# Register your models here.