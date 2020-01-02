from importlib import import_module

def _import_module(module_path, module_name=None):
    if not module_name:  # note that we land here on '' as well
        return import_module(module_path, module_path.split('.')[-1])
    return import_module(module_path, module_name)