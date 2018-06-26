from django.db import models

# this is where classes are made
class Blogpost(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title

