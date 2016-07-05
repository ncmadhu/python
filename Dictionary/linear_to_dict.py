#!/usr/bin/python

class AttributeDict(dict):


    marker = object()
    def __init__(self, value=None):
        if value is None:
            pass
        elif isinstance(value, dict):
            for key in value:
                self.__setitem__(key, value[key])
        elif isinstance(value, list):
            for idx in range(len(value)):
                nested_dict = value[idx]
                for key in nested_dict:
                    self.__setitem__(key,nested_dict[key])
        else:
            raise TypeError, 'expected dict'

    def __setitem__(self, key, value):
        if '.' in key:
            input_key, rest_key = key.split('.', 1)
            target = self.setdefault(input_key, AttributeDict())
            if not isinstance(target, AttributeDict):
                raise KeyError, 'cannot set "%s" in "%s" (%s)' % (rest_key, input_key, repr(target))
            target[rest_key] = value
        else:
            if isinstance(value, dict) and not isinstance(value, AttributeDict):
                value = AttributeDict(value)
            if isinstance(value, list) and not isinstance(value, AttributeDict):
                new_value = []
                for elem in range(len(value)):
                    new_value.append(AttributeDict(value[elem]))
                value = new_value
            dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        if '.' not in key:
            return dict.__getitem__(self, key)
        input_key, rest_key = key.split('.', 1)
        target = dict.__getitem__(self, input_key)
        if not isinstance(target, AttributeDict):
            raise KeyError, 'cannot get "%s" in "%s" (%s)' % (rest_key, input_key, repr(target))
        return target[rest_key]

    def __contains__(self, key):
        if '.' not in key:
            return dict.__contains__(self, key)
        input_key, rest_key = key.split('.', 1)
        target = dict.__getitem__(self, input_key)
        if not isinstance(target, AttributeDict):
            return False
        return rest_key in target

    def setdefault(self, key, value):
        if key not in self:
            self[key] = value
            return self[key]
        elif key in self:
            return self[key]

    __setattr__ = __setitem__
    __getattr__ = __getitem__

    
def form_dict(input_list):
    """
    Returns dictionary from given list of key and values separated by =.
    
    The key is given in linearised format.
    
    Example a.b.c=3 is transformed to d[a][b][c] = 3

    """

    key_value_pair = []
    for elem in input_list:
        key_value_pair.extend(elem.split('='))
    result_dict = convert_list_dict(key_value_pair)
    newdict = {}
    attr_dict = AttributeDict(newdict)
    for k, v in result_dict.iteritems():
        if (type(v) == str and v == "True"):
            v = True 
        elif (type(v) == str and v == "False"): 
            v = False
        attr_dict[k] = v
    return attr_dict


