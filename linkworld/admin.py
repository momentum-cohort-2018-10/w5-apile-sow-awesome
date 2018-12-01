from django.contrib import admin
from linkworld.models import Post, Comment, Vote


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'author', 'url', 'text', 'date')


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('content', 'commenter', 'date')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Vote)
