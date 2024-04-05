from django.db import models


class compHead(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    start_day = models.CharField(max_length=15)
    post = models.CharField(max_length=15)

    def __str__(self):
        return self.last_name

