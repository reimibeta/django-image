from django.utils.html import format_html


class RenderImage:
    _html = None
    _size = None

    def __init__(self):
        pass

    # size image
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    def set_size(self, size=None):
        if size:
            self.size = size
        else:
            self.size = (100, 100)

    # html
    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):
        self._html = value

    def set_html(self, url):
        width = 'width="{}px"'.format(self.size[0])
        height = 'height="{}px"'.format(self.size[1])
        style = 'style="display: block; object-fit: cover"'
        self.html = '<img src={} {} {} {} />'.format(url, width, height, style)

    def render(self, url, size=None):
        self.set_size(size)
        self.set_html(url)
        return format_html(self.html)


render_image = RenderImage()
