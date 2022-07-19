from django.db import models
from django_extensions.db.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class HelpRequest(TimeStampedModel):
    full_name = models.CharField(max_length=255, null=False)
    organization_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    phone_number = PhoneNumberField(null=False)
    message = models.TextField(null=False)

    def __str__(self):
        return f'{self.full_name} {self.created}'


class Document(TimeStampedModel):
    help_request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE, related_name='documents')
    name = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to='help_requests/%Y-%m-%d/')

    def __str__(self):
        return self.name

