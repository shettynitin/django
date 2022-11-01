from django import template
register = template.Library()

@register.filter(name='cutt')
def cutt(value,arg):
    """
    This cuts all the values of "arg" from the string
    """
    return value.replace(arg,'@')
