from django.contrib import admin

# Register your models here.
from django.contrib import admin
from mysite.models import Post,Product
admin.site.register(Post)
admin.site.register(Product)