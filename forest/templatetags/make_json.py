from django import template
from json import loads
register = template.Library()
def make_json(dict):
    new_json = loads(dict)
    return new_json
register.filter("make_json" , make_json)