import inspect


def introspection_info(obj):
    dict_info = {'type': type(obj)}
    at_meth = dir(obj)
    attrs = []
    meths = []
    for el in at_meth:
        if '__' in el:
            meths.append(el)
        else:
            attrs.append(el)
        dict_info['attributes'] = attrs
        dict_info['methods'] = meths
        module = inspect.getmodule(obj)
        dict_info['module'] = module.name if module else "__main__"
        #dict_info['module'] = inspect.getmodule(obj)
    return dict_info


number_info = introspection_info(42)
print(number_info)
