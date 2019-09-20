from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=40, null=True)
    description = models.TextField(null=True)
    date = models.CharField(max_length=40, null=True)
    location = models.CharField(max_length=40, null=True)

    headerImage = models.ImageField(upload_to='images/', null=True)
    image1 = models.ImageField(upload_to='images/', null=True)
    image2 = models.ImageField(upload_to='images/', null=True)
    image3 = models.ImageField(upload_to='images/', null=True)

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    #modified = models.DateTimeField(auto_now=True, null=True, editable=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.date)
# References:
# DateTimeField https://docs.djangoproject.com/en/2.2/ref/models/fields/#datetimefield
