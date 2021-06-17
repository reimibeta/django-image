from django.db import models

from django_image.compress.compress_image import compress_image


class Image(models.Model):
    photo = models.ImageField(
        upload_to='images/',
        null=True
    )
    thumbnail = models.ImageField(
        upload_to='images/thumbnails/',
        blank=True, null=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        if str(self.photo.path) == str(self.photo.file):
            print('return true when on new file uploaded!')
        else:
            self.photo = compress_image.resize(
                self.photo,
                700,
                # "test"
            )
            self.thumbnail = compress_image.resize(
                self.photo,
                300,
                # 'test'
            )
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.thumbnail.url
