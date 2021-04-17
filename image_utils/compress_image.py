from PIL import Image, ExifTags
from io import BytesIO
import sys
import uuid
import os

from django.core.files.uploadedfile import InMemoryUploadedFile


class CompressDimension:

    def __init__(self, width=None, height=None):
        self.width = width if width else 400
        self.height = height if height else 400

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class CompressImage:
    image = None
    dimension = None
    output = None

    def __init__(self, size, image):
        # object.get("width"), object.get("height")
        self.dimension = CompressDimension(tuple(size))
        self.image = Image.open(image).convert('RGB')
        self.output = BytesIO()

    def fixed_size(self):
        width_percent = (
                self.dimension.width / float(self.image.size[0])
        )
        height_size = int(
            (float(self.image.size[1]) * float(width_percent))
        )
        return width_percent, height_size

    def resize(self, name):
        width, height = self.fixed_size()
        # output = BytesIO()
        # Resize/modify the image
        im = self.image.resize(
            (self.dimension.width, height),
            Image.ANTIALIAS
        )  # this is mush change
        # after modifications, save it to the output
        # im = im.rotate(90, expand=True)
        im.save(self.output, format='JPEG', quality=100)
        # If no ExifTags, no rotating needed.
        self.output.seek(0)
        # change the imagefield value to be the newley modifed image value image.name.split('.')[0]
        if not name:
            name = uuid.uuid4().hex[:8].upper()
        img = InMemoryUploadedFile(
            self.output, 'ImageField', "{}{}".format(
                name, self.ext()
            ), 'image/jpeg', sys.getsizeof(self.output), None)
        return img

    def resize_fixed(self):
        pass

    def ext(self):
        return os.path.splitext(self.image.name)[1]


class compress_image:

    def image(self, image, name=None, width=400, height=None):
        # Opening the uploaded image
        im = Image.open(image).convert('RGB')
        output = BytesIO()
        # Resize/modify the image
        width_percent = (width / float(im.size[0]))
        height_size = int((float(im.size[1]) * float(width_percent)))
        if not height:
            im = im.resize((width, height_size), Image.ANTIALIAS)
        else:
            im = im.resize((width, height), Image.ANTIALIAS)
        # after modifications, save it to the output
        # im = im.rotate(90, expand=True)
        im.save(output, format='JPEG', quality=100)
        # If no ExifTags, no rotating needed.
        output.seek(0)

        # change the imagefield value to be the newley modifed image value image.name.split('.')[0]
        if not name:
            name = uuid.uuid4().hex[:8].upper()
        img = InMemoryUploadedFile(output, 'ImageField', "{}{}".format(name, self.ext(image)), 'image/jpeg',
                                   sys.getsizeof(output), None)
        return img

    @staticmethod
    def ext(image):
        return os.path.splitext(image.name)[1]
