from django.conf import settings
from django.db import models
from study_groups.models import StudyGroup


class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.CASCADE)
    group = models.ManyToManyField(StudyGroup)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'], name='subject_title')
        ]

    def __str__(self):
        return self.title