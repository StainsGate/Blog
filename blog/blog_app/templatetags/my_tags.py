from django import template


register = template.Library()

@register.filter
def glance(strings):
    return strings[:60]

@register.filter
def short_glance(strings):
    return strings[:20]



