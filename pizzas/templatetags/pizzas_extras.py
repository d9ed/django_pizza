from django import template


register = template.Library()


@register.filter(name="add_sizes_list")
def add_sizes_list(sizes_list):
    return ' '.join([str(s.size) for s in sizes_list])
