from django import template

register = template.Library()


def addplaceholder(value,token):
    value.field.widget.attrs['placeholder'] = token
    return value

def addclass(value,token):
    # value = value.label_tag(attrs={'class': token})

    value.field.widget.attrs["class"] = token
    return value

register.filter('addclass',addclass)
register.filter('addplaceholder',addclass)