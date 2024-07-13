from django.contrib import admin
from .models import User



class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")

    from .models import Category

class CategoryAdmin(admin.ModelAdmin):
        list_display = ("id", "Name")

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "date_published")


from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "date_posted")
