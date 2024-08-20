# Dale Wright

# Parse JSON objects by key name
import fnmatch
class JsonParserException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class JsonParser:
    """
        The JsonParser class.

        Methods:

        __init__(self, obj, args)
            returns the JsonParser object

        get_args(self):
            returns the arguments

        get_json(self):
            returns the JSON object

        get_data(self):
            returns the parsed JSON data
    """
    
    def __init__(self, obj, args):

        if not obj:
            raise JsonParserException(
                msg='JSON object must be present'
            )
        if not args:
            raise JsonParserException(
                msg='No keys present to parse'
            )

        self.json_obj = obj
        self.args = args

    def get_args(self):
        return(self.args)
    
    def get_json(self):
        return(self.json_obj)

    
    def get_data(self):
        def search_dict(dct, keys_to_search):
            found = {}
            for key, value in dct.items():
                for pattern in keys_to_search:
                    if fnmatch.fnmatch(key, pattern):
                        if key not in found:
                            found[key] = value
                        else:
                            if not isinstance(found[key], list):
                                found[key] = [found[key]]
                            found[key].append(value)
                if isinstance(value, dict):
                    nested_found = search_dict(value, keys_to_search)
                    for nested_key, nested_value in nested_found.items():
                        if nested_key not in found:
                            found[nested_key] = nested_value
                        else:
                            if not isinstance(found[nested_key], list):
                                found[nested_key] = [found[nested_key]]
                            if isinstance(nested_value, list):
                                found[nested_key].extend(nested_value)
                            else:
                                found[nested_key].append(nested_value)
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            nested_found = search_dict(item, keys_to_search)
                            for nested_key, nested_value in nested_found.items():
                                if nested_key not in found:
                                    found[nested_key] = nested_value
                                else:
                                    if not isinstance(found[nested_key], list):
                                        found[nested_key] = [found[nested_key]]
                                    if isinstance(nested_value, list):
                                        found[nested_key].extend(nested_value)
                                    else:
                                        found[nested_key].append(nested_value)
            return found


        result = []
        for item in self.json_obj:
            if isinstance(item, dict):
                result.append(search_dict(item, self.args))
        return result