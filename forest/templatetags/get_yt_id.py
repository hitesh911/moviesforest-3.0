from django import template
register = template.Library()
@register.filter
def get_yt_id(url):
    try:
        yt_id = url.split("/embed/")[1]
    except:
        yt_id = ""
    return yt_id