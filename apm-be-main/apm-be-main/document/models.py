# nama_app/models.py

from django.db import models
from project.models import Project
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from user.models import UserProfile

class ProjectDocument(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    uploader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    upload_date = models.DateField()
    document_file = models.FileField(upload_to='doc/')
    category = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # Default
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Documents'
        db_table = 'apm_document'
        ordering = ['-created_at']
        indexes = [models.Index(fields=['-created_at']), ]
