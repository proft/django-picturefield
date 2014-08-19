from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe


class PictureFileWidget(AdminFileWidget):
    input_type = 'file'

    def render(self, name, value, attrs=None):
        input = super(forms.widgets.FileInput, self).render(name, value, attrs)
        if value:
            url = value.url if hasattr(value, 'url') else ''
            img = '<img src="%s" width="100" />' % url
            item = '<td style="vertical-align: middle;%s">%s</td>'
            output = []
            output.append('<table style="border-style: none;" class="picfield"><tr>')
            output.append(item % ('padding-right: 10px;', '<a target="_blank" href="%s">%s</a>' % (url, img)))
            output.append(item % ('', input))
            output.append('</tr><tr>')
            output.append(u'<td colspan="2"><input type="checkbox" name="{name}-clear" id="{name}_delete"/> <label for="{name}_delete">{label}</label></td>'.format(name=name, label=_('Delete')))
            output.append('</tr></table>')
            return mark_safe(u''.join(output))
        else:
            return mark_safe(input)

