from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """This cuts out all values of "arg" from the string

    Args:
        value (string): value
        arg (str): cut element
    """
    return value.replace(arg, '')

# register.filter('cut', cut)