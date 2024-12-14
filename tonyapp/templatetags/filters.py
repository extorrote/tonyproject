# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def format_product_type(value):
    return value.replace(" ", "_").lower()  # Ensures underscores and lower case
