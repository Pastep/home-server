from django import template
from django.contrib.humanize.templatetags import humanize

import os
register = template.Library()

@register.filter
def filename(value):
    return os.path.basename(value.file.name)
@register.filter
def littleFilename(value):
    filename = os.path.basename(value.file.name)
    if len(filename) > 10:
        filename = f"{filename[0:8]}..."
    else:
        filename = filename[0:10]
    return filename
@register.filter
def extension(value):
    return os.path.basename(value.file.name).split('.')[-1]

@register.filter
def get_date(value):
    return humanize.naturaltime(value)

@register.filter
def getItem(dictionary, key):
    return dictionary[key]