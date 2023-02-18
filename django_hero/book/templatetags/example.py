from django import template
from django.template import Context, Template

register = template.Library()

@register.filter(name="get_name")
def get_name(value, arg):
    template = Template(value)
    context =Context({'name': arg})
    final_val = template.render(context)
    return final_val