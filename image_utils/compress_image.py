from PIL import Image, ExifTags
from io import BytesIO
import sys
import uuid
import os

from django.core.files.uploadedfile import InMemoryUploadedFile


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
