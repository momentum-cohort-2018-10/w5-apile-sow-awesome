from linkworld.models import Post, Comment
from django.forms import ModelForm


class PostForm(ModelForm):

    class Meta:

        model = Post
        fields = ('author', 'title', 'url', 'text',)


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('content', 'commenter', )
