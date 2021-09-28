from django import template
from ENVIRONMENT_APP.models import StudentFile

register = template.Library()

@register.simple_tag
def total_studentfile():
    return StudentFile.objects.count()

@register.inclusion_tag('ENVIRONMENT_MANAGE_APP/latest_file.html')
def show_latest_file(count=5):
    latest_file = StudentFile.objects.order_by('-publish')[:count]
    return {'latest_file':latest_file}

