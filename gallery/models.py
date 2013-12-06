from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField(default=999)

    year = models.IntegerField(null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        if self.year:
            return u'%s - %s' %(self.name, self.year)
        else:
            return self.name

    def slug(self):
        return slugify(self.name)


class GalleryItem(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField(default=999)

    #media_type choices:
    image_media = 'Image'
    video_media = 'Video'
    audio_media = 'Audio'
    internet_media = 'Internet'
    media_type_choices = (
        (image_media, 'Image'),
        (video_media, 'Video'),
        (audio_media, 'Audio'),
        (internet_media, 'Internet'),
    )
    media_type = models.CharField(choices=media_type_choices, max_length=20)
    project = models.ForeignKey('Project', null=True, blank=True)
    image = models.ImageField(upload_to='%Y/images/')
    thumbnail = ImageSpecField(source='image',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 75})
    caption = models.TextField(null=True, blank=True)
    video_embed_code = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=300, null=True, blank=True)
    audio_file = models.FileField(upload_to='%Y/audio/', null=True, blank=True)

    def __unicode__(self):
        return self.name