# -*- coding: utf-8 -*-

from isounidecode import unidecode
from django.db.models import ImageField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from picturefield.settings import *
from picturefield.widgets import PictureFileWidget

try:
    from PIL import Image
except ImportError:
    import Image

class PictureField(ImageField):
    def __init__(self, verbose_name=None, name=None, min_size=MIN_SIZE, max_size=MAX_SIZE, *args, **kwargs):
        self.min_size = {}
        self.max_size = {}

        self.min_size['width'] = min_size[0]
        self.min_size['height'] = min_size[1]
        self.max_size['width'] = max_size[0]
        self.max_size['height'] = max_size[1]
        super(PictureField, self).__init__(verbose_name, name, *args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = PictureFileWidget
        return super(PictureField, self).formfield(**kwargs)

    def validate(self, value, model_instance):
        super(PictureField, self).validate(value, model_instance)
        if hasattr(value, 'file'):
            # format file name to ascii
            value.name = unidecode(value.name)

            # check size
            if value.width < self.min_size['width'] or value.height < self.min_size['height']:
                raise ValidationError(_(u'Size of the file is smaller than {}x{} px.').format(self.min_size['width'], self.min_size['height']))

            elif value.width > self.max_size['width'] or value.height > self.max_size['height']:
                raise ValidationError(
                    _(u'Size of the file is bigger than {}x{} px.').format(self.max_size['width'], self.max_size['height']))

            # check file size
            if value.size > MAX_UPLOAD_SIZE:
                raise ValidationError(_(u'Maximal size of file is {}.').format(filesize(MAX_UPLOAD_SIZE)))

            # check format
            try:
                im = Image.open(value)
                if im.format not in ALLOWED_FORMATS:
                    raise ValidationError(_(u'Unsupported file extension. You can upload {}.').format(', '.join(ALLOWED_FORMATS)))
            except ImportError:
                raise
            except Exception: # Python Imaging Library doesn't recognize it as an image
                raise ValidationError(self.error_messages['invalid_image'])
