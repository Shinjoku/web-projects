from django import template

register = template.Library()


@register.filter()
def na_empresa(client_list, empresa_id):
    return client_list.filter(pk=empresa_id)
