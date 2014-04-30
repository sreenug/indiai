from django import template

register = template.Library()


@register.filter(name='placeholder')
def html_placeholder(field, args=None):
    if args == None:
        return field
    field.field.widget.attrs.update({"placeholder": args})
    field.field.widget.attrs.update({"class": 'form-control'})
    return field

