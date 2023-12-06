from django import template
from users.models import CustomUser

register = template.Library()

@register.inclusion_tag('include/navbar.html')
def get_user_slug(user):
    user_slug = user.slug
    return {'user_slug': user_slug}