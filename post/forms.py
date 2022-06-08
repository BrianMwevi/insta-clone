from django.forms import ModelForm
from post.models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'captions')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
