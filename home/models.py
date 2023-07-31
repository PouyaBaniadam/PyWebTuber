from django.db import models


class YouTubeData(models.Model):
    file = models.FileField(upload_to="Videos")
    link = models.URLField(max_length=50)
    file_size = models.FloatField()
    downloaded = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.link
