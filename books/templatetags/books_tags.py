from django import template

register = template.Library()


@register.filter(name="cut")
def cut(value, args):
    return value.replace(args, "")
