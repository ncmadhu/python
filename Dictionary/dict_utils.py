def update_dictionary(d, u):
    """
    Returns dictionary d with updated values from u.
    
    example: updates d[k] with value of u[k]
    
    """

    for k, v in u.iteritems():
        if isinstance(v, dict):
            r = update_dictionary(d.get(k, {}), v)
            d[k] = r
        elif isinstance(v,list):
            res = []
            for elem in range(len(v)):
                if isinstance(v[elem],dict):
                    res.append(update_dictionary(d.get(k,{})[elem],v[elem]))
                else:
                    res.append(v[elem])
            d[k] = res
        else:
            d[k] = u[k]
    return d
    
    
def linearize_dict(obj):
    """
    Returns keys in a dictionary obj in a linearised format.
    
    example: returns obj[k][u] as k.u
    
    """

    result_list = []
    for k, v in obj.items():
        basevalue = str(k) + "."
        if isinstance(obj[k],dict):
            keylist = linearize_dict(obj[k])
            for item in keylist:
                result_list.append(basevalue + item)
        elif isinstance(obj[k],list):
            for element in obj[k]:
                element_list = linearize_dict(element)
                for elem in element_list:
                    result_list.append(basevalue + elem)                
        else:
            result_list.append(basevalue[:-1])
    return result_list
    
    
def check_dictionary(param, given_dict):
    """
    checks whether given key in linearised format is present in given_dict.
    
    example: if param is k.u function verifies whether given_dict[k][u] is present.
    
    """

    param_keys = param.split(".",1)
    root_key = param_keys.pop(0)
    if given_dict.has_key(root_key):
        if len(param_keys) > 0:
            next_level_input = given_dict[root_key]
            if isinstance(next_level_input, list):
                next_key = param_keys.pop(0)
                result_list = []
                ignore_list = []
                return_value = "SUCCESS"
                for item_dict in next_level_input:
                    ret_val = check_dictionary(next_key,item_dict)
                    if ret_val != "FAIL":
                        result_list.append(item_dict)
                    else:
                        ignore_list.append(item_dict)
                if len(result_list) > 0:
                    given_dict[root_key] = result_list
                    if len(ignore_list) > 0:
                        return "PARTIAL_SUCCESS"
                    else:
                        return "SUCCESS"
                else:
                    return "FAIL"
            else:
                return check_dictionary(param_keys.pop(0),next_level_input)
        else:
            return "SUCCESS"
    else:
        return "FAIL"
        
        
def convert_list_dict(input_list):
    """
    convert given list in to dictionary
    """

    result_dict = dict(map(None, *[iter(input_list)]*2))
    return result_dict
    
    
def dict_to_string(input_dict):
    """
    convert given dictionary to string
    """
    
    from json import dumps
    return dumps(input_dict)