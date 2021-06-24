from django.db import models
from accounts.models import User
import datetime, os, json
# Create your models here.

def getPath(instance, filename):
    date = datetime.datetime.now()
    return f"uploads/{instance.user.username}/{date.year}/{date.month}/{date.day}/{date.minute}/{date.second}/{filename}"


class Folder(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False
    )
    name = models.CharField(
        max_length=200,
        default="untitledFolder"
    )
    public = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.user} / {self.id}"

class File(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False
    )
    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        null=True
    )
    file = models.FileField(
        upload_to=getPath
    )
    public = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.id} / {os.path.basename(self.file.name)}"