from django.db import models

class User(models.Model):
    name = models.CharField(max_length=40, null=False)
    login = models.EmailField(null=False)
    password = models.CharField(max_length=256, null=False)

    def __unicode__(self):
        return self.name

class Hashtag(models.Model):
    name = models.CharField(max_length=25, null=False)

    def __unicode__(self):
        return self.name

class News(models.Model):
    label = models.CharField(max_length=60, null=False)
    text = models.TextField(null=False)
    hashtags = models.ManyToManyField(Hashtag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.label