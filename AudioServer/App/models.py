from django.db import models

# Create your models here.


class Song(models.Model):
    Song_ID=models.IntegerField(max_length=100,unique=True,null=True)
    Name= models.TextField(max_length=100,null=True)
    duration = models.FloatField(max_length=20)
    Uploaded_Time=models.DateTimeField(null=True)
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)

    def __str__(self):
        return self.Name

class Podcast(models.Model):
    Podcast_ID=models.IntegerField(max_length=100,unique=True)
    Name = models.TextField(max_length=100)
    duration = models.FloatField()
    Uploaded_Time = models.DateTimeField()
    Host = models.CharField(max_length=100)
    Participants=models.CharField(max_length=100)
    audio_file = models.FileField(blank=True,null=True)
    image = models.ImageField(null=True)


    paginate_by = 2

    def __str__(self):
        return self.Name


class AudioBook(models.Model):
    AudioBook_ID=models.IntegerField(max_length=100,unique=True)
    Title= models.TextField(max_length=100)
    Author= models.TextField(max_length=100)
    Narrator=models.TextField(max_length=100)
    duration = models.FloatField(max_length=20)
    Uploaded_Time=models.DateTimeField()
    audio_file = models.FileField(blank=True,null=True)
    image = models.ImageField(null=True)


    paginate_by = 2

    def __str__(self):
        return self.Title


