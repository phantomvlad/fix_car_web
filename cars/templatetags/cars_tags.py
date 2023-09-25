from django import template
from cars.models import Car

register = template.Library()

def get_cars():
    return Car.objects.all()

@register.inclusion_tag('cars/include/list_cars.html')
def get_cars_user(user, sort = None):
    if not sort:
        cars = Car.objects.filter(owner=user).order_by('-time_update')
    else:
        cars = Car.objects.filte(owner=user).order_by(sort)
    return {'cars': cars }