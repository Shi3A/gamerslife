from django.db import models


class PageManager(models.Manager):
    def get_queryset(self):
        return super(PageManager, self).get_queryset().filter(is_deleted=False)
