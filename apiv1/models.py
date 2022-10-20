from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return 'ID: %s - NAME: %s' % (self.id, self.name)

class DataTag(models.Model):
    tag_name = models.CharField(blank=False, null=False, max_length = 100, primary_key=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'TAG NAME: %s' % (self.tag_name)


class DataTS(models.Model):
    tag    = models.ForeignKey(DataTag, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)