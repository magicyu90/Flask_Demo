
DEFAULT_VALUE = {str(int): 0, str(float): 0.0, str(list): [], str(dict): {}, str(bool): False, str(str): ''}
redis_types = {}
redis_types['DEVICE_EVENT_STAT'] = {'CT_LIGHT_MACHINE': int, 'DR_LIGHT_MACHINE': int, 'CT_DETECTOR': int, 'DR_DETECTOR': int}

def redis_decode(key_types, redis_dict):
    result = {}
    # construct initial Python dict result with default value
    for k in key_types:
        type = key_types[k]
        result[k] = DEFAULT_VALUE[str(type)]

    for k in redis_dict.keys():
        v = redis_dict[k]
        if k in key_types:
            type = key_types[k]
            if type == list or type == bool:
                result[k] = eval(v)
            else:
                if v == '' and (type == int or type == float):
                    v = '0'
                result[k] = type(v)
        else:
            result[k] = v

    return result
