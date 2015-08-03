from django.db import models

from base.models import Page
from user.models import User


class Post(Page):
    author = models.ForeignKey(User, verbose_name="Author")
    original_file = models.CharField(verbose_name="Uploaded file", blank=False, null=False, max_length=512)
    converted_file = models.CharField(verbose_name="Converted file", blank=True, null=True, max_length=512)

    def get_file(self):
        if self.converted_file:
            return self.converted_file
        return self.original_file

    def save(self, *args, **kwargs):
        if not self.converted_file:
            # TODO: send signal to convert
            pass
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
