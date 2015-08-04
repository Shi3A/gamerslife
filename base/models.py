import time
from django.db import models

from base.managers import PageManager


class Page(models.Model):
    title = models.TextField(verbose_name="Title", blank=False)
    created = models.DateTimeField(verbose_name="Created", blank=False, default=time.time())
    updated = models.DateTimeField(verbose_name="Updated", blank=False, default=time.time())
    is_deleted = models.BooleanField(verbose_name="Deleted", default=False)
    order = models.IntegerField(verbose_name="Order", default=100)

    all_objects = models.Manager()
    objects = PageManager()

    def save(self, *args, **kwargs):
        self.updated = time.time()
        super(Page, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Page{1}: {0}".format(self.title, " deleted" if self.is_deleted else "")

    class Meta:
        ordering = ['order']
        verbose_name = "Page"
        verbose_name_plural = "Pages"
