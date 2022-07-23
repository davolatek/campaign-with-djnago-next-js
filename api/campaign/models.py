from tkinter import CASCADE
from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify


# Create your models here.


class Campaigns(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    logo = CloudinaryField("Image", overwrite=True, format="jpg")

    class Meta:
        ordering = ("-created_at",)
        verbose_name="Campaign"
        verbose_name_plural = "Campaigns"

    def __str__(self):
        return self.title


class Subcription(models.Model):
    email = models.EmailField(max_length=100)
    campaign = models.ForeignKey(to=Campaigns, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.email
