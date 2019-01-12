from django import template
register=template.library()

@register.simple_tag
def multiply(qty, *args, **kwargs):
    # you would need to do any localization of the result here
    return [(qty-1) * 40]