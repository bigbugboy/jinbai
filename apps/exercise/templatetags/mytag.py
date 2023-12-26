from django import template
		

register = template.Library()


@register.filter
def numrange(num):
    return range(num)
