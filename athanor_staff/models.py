from django.db import models


class StaffCategory(models.Model):
    key = models.CharField(max_length=255, null=False, blank=False, unique=True)
    order = models.PositiveSmallIntegerField(default=0, unique=True)

    def __str__(self):
        return self.key


class StaffEntry(models.Model):
    character = models.OneToOneField('objects.ObjectDB', related_name='+', on_delete=models.CASCADE, primary_key=True)
    category = models.ForeignKey(StaffCategory, related_name='staffers', on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=0)
    position = models.CharField(max_length=255, null=True, blank=True)
    duty = models.CharField(max_length=255, default="On", null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    vacation = models.DateTimeField(null=True)

    def __str__(self):
        return self.character.key
