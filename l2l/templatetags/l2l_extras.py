from django import template
from datetime import datetime

register = template.Library()


@register.filter
def l2l_dt(value):
    try:
        if type(value) is datetime:
            try:
                value.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                print('Datetime object cannot be formatted')
                return 'N/A'
            finally:
                return value.strftime("%Y-%m-%d %H:%M:%S")
        if type(value) is str:
            try:
                datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                print('String object cannot be converted to datetime')
                return 'N/A'
            return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        else:
            raise TypeError('Input type not supported')
    except TypeError:
        print('Unsupported type')
        return "N/A"
