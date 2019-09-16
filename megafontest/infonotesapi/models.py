from django.db import models

from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    def __str__(self):
        return "{} - {}".format(self.title, self.slug)
