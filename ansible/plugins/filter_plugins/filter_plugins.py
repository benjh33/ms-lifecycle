from jinja2.utils import soft_unicode

def map_format(value, pattern):
    if type(value) in [tuple, list]:
        return soft_unicode(pattern) % tuple(value)
    return soft_unicode(pattern) % value

def dict_format(value, pattern):
    print(value)
    return soft_unicode(pattern).format(**value) 

def flat_list_group_name(values):
    group_and_names = []
    for d in values:
        if d['count'] == 1:
            names = (d['name'], )
        else:
            names = (d['name'] + '_' + str(i) for i in range(d['count']))
        group_and_names.extend([dict(role=d['name'], name=n) for n in names])
    return group_and_names

class FilterModule(object):

    def filters(self):
        return {
                'map_format': map_format,
                'dict_format': dict_format,
                'flat_list_group_name': flat_list_group_name
                }
