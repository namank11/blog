from django.db import models

# Create your models here.


class Title(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Description(models.Model):
    topic = models.ForeignKey(Title, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Descriptions'

    def __str__(self):
        return f"{self.text[:50]}"
