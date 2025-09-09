from django.db import models

# Create your models here.
class Transcription(models.Model):
    text = models.TextField(blank=True, null=True, editable=False)
    language = models.CharField(max_length=20)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    STATUS_PENDING='pending'
    STATUS_COMPLETED='completed'
    STATUS_FAILED='failed'
    STATUS_CHOICES=[
        (STATUS_PENDING, 'Pendiente'),
        (STATUS_COMPLETED, 'Completo'),
        (STATUS_FAILED, 'Falló'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)