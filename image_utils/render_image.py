from django.utils.html import format_html


class RenderImage:

    @staticmethod
    def renderHtmlImage(image_url):
        return format_html(
            '<img src={} height="100px" width="100px" style="display: block; object-fit: cover" />'.format(image_url))
