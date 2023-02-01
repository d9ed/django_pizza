from django import template

register = template.Library()


@register.filter(name="sizes_to_string")
def sizes_to_string(sizes_list):
    sizes_string = ' '.join([str(s.size) for s in sizes_list])
    return sizes_string
