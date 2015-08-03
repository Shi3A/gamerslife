from django import forms
from post.models import Post


class PostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=512)
    # TODO: add validation
    uploaded_file = forms.ImageField(label="Upload file")

    def create_post(self, filename):
        post = Post()
        post.title = self.title
        post.author = self.request.user
        post.original_file = filename
        post.save()
