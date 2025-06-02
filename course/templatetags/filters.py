# templatetags/filters.py
from django import template
register = template.Library()

@register.filter
def get_cell(table_data, key):
    return table_data.get(key, '')

@register.filter
def get_cell(dictionary, key):
    return dictionary.get(key, "")
