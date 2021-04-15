from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse_lazy

url_regex = '^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
url_validator = RegexValidator(url_regex, "Invalid URL")

# Create your models here.
class Link(models.Model):
    long_url = models.CharField(
        max_length=255,
        validators=[url_validator]
    )
    short_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.long_url
    
    def get_absolute_url(self):
        return reverse_lazy('home')