from django import template

from ..metrics import registry as metrics_registry

register = template.Library()


@register.simple_tag
def get_postgres_metrics():
    return metrics_registry.sorted


@register.simple_tag(takes_context=True)
def record_style(context):
    metric = context['metric']
    record = context['record']
    style = metric.get_record_style(record)
    if style:
        return 'record-%s' % style
    return ''


@register.simple_tag(takes_context=True)
def record_item_style(context):
    metric = context['metric']
    record = context['record']
    item = context['item']
    index = context['forloop']['counter0']
    style = metric.get_record_item_style(record, item, index)
    if style:
        return 'item-%s' % style
    return ''
