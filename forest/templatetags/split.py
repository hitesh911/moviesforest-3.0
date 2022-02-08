from django import template
register =template.Library()
def split(lis , args):
    new_list = lis.split(args)
    return new_list 
register.filter("split",split)