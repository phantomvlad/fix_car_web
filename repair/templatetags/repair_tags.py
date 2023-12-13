from django import template
from repair.models import Repair

register = template.Library()

@register.inclusion_tag('repair/include/list_repairs.html')
def get_repairs_car(car, sort = None):
    if not sort:
        repairs = Repair.objects.select_related('car', 'owner').filter(car=car).order_by('-time_create')
    else:
        repairs = Repair.objects.select_related('car', 'owner').filter(car=car).order_by(sort)
    return {'repairs': repairs}