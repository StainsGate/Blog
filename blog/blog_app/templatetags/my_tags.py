from django import template
import re

register = template.Library()


@register.filter
def get_paragraph(content):
    paragraph = re.search(r'<p>.*</p>',content)
    if paragraph:
            str = paragraph.group(0)
            return str
    else:
        return '<p>The author is a idiot, he says nothing.</p>'