from django.contrib import admin

from example.images.models import Image
from image_utils.renders.render_image import render_image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    list_display_links = ['image', ]

    # readonly_fields = ('password',)

    def image(self, obj):
        image = Image.objects.filter(id=obj.id).first()
        print(image.thumbnail.url)
        if image:
            return render_image.render(image.thumbnail.url)
        else:
            return 'image not provided'


admin.site.register(Image, ImageAdmin)
