from django.db import models

class Lead(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    lead_owner = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    client_code = models.CharField(max_length=50, blank=True)
    client_name = models.CharField(max_length=255, blank=True)
    project_name = models.CharField(max_length=255, blank=True)
    date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=100, blank=True)
    email_address = models.EmailField(blank=True)
    type = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=255, blank=True)
    manager_comments = models.TextField(blank=True)

    class Meta:
        db_table = 'intersted'

    def __str__(self):
        return f"{self.client_name} - {self.project_name}"
