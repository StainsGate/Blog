from django import template
from blog_app.models import Blog


register = template.Library()

@register.filter
def glance(strings):
    return strings[:60]



