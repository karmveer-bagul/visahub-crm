from django.db import models
from django.conf import settings

# documents/models.py

class Document(models.Model):
    application = models.ForeignKey('applications.VisaApplication', on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

