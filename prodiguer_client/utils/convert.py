# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.utils.convert.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Library conversion utility functions.

.. moduleauthor:: Insitut Pierre Simon Laplace (IPSL)


"""
import collections
import datetime
import json
import re
import types
import uuid



# Values considered to be abbreviations.
_ABBREVIATIONS = ("id", "uid", "uuid")

# ISO date formats.
_ISO_DATE_FORMATS = ["%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"]

# Default character set.
_JSON_CHARSET = "ISO-8859-1"

# Set of types to be ignored when jsonifying.
_JSONIFYING_TYPES_IGNORE = (int, float, long, type(None), unicode)

# Set of unicodeable types used in jsonifying.
_JSONIFYING_TYPES_UNICODEABLE = (basestring, datetime.datetime, uuid.UUID)


def str_to_pascal_case(target, separator='_'):
    """Converts a string to pascal case.

    :param str target: A string to be converted.
    :param str separator: A separator used to split target string into parts.

    :returns: The target string converted to pascal case.
    :rtype: str

    """
    result = ''
    if target is not None and len(target):
        if target[0:len(separator)] == separator:
            result = separator
        for text in target.split(separator):
            if text.lower() in _ABBREVIATIONS:
                result += text.upper()
            elif (len(text) > 0):
                result += text[0].upper()
                if (len(text) > 1):
                    result += text[1:]
    return result


def str_to_camel_case(target, separator='_'):
    """Converts a string to camel case.

    :param str target: A string to be converted.
    :param str separator: A separator used to split target string into parts.

    :returns: The target string converted to camel case.
    :rtype: str

    """
    result = ''
    if target is not None and len(target):
        text = str_to_pascal_case(target, separator)
        # Preserve initial separator
        if text[0:len(separator)] == separator:
            result += separator
            text = text[len(separator):]

        # Lower case abbreviations.
        if text.lower() in _ABBREVIATIONS:
            result += text.lower()

        # Lower case initial character.
        elif len(text):
            result += text[0].lower()
            result += text[1:]
    return result


def str_to_spaced_case(target, separator='_'):
    """Converts a string to spaced case.

    :param str target: A string for conversion.

    :returns: A string converted to spaced case.
    :rtype: str

    """
    if target is None:
        return ""
    elif separator is not None and len(target.split(separator)) > 1:
        return " ".join(target.split(separator))
    elif target.find(" ") == -1:
        return re.sub("([A-Z])", r" \g<0>", target).strip()
    else:
        return target


def str_to_underscore_case(target):
    """Converts a string to underscore case.

    :param str target: A string for conversion.

    :returns: A string converted to underscore case, e.g. account_number.
    :rtype: str

    """
    if target is None or not len(target):
        return unicode()

    result = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', target)
    result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', result)

    return result.lower()


class _JSONEncoder(json.JSONEncoder):
    """Extends json encoder so as to handle extended types.

    """
    def default(self, obj):
        """Returns default encodings for type not auto-encoded by base class.

        """
        if isinstance(obj, datetime.datetime):
            return unicode(obj.isoformat().replace('T', ' '))
        elif isinstance(obj, datetime.date):
            return unicode(obj.isoformat())
        elif isinstance(obj, datetime.time):
            return unicode(obj.isoformat())
        elif isinstance(obj, uuid.UUID):
            return unicode(obj)
        else:
            raise TypeError(repr(obj) + " is not JSON serializable")


class _JSONDecoder(json.JSONDecoder):
    """Extends json decoder so as to handle extended types.

    """
    def __init__(self, key_formatter, to_namedtuple=False):
        """Object constructor.

        """
        super(_JSONDecoder, self).__init__(encoding=_JSON_CHARSET,
                                           object_hook=self._to_object)
        self.key_formatter = key_formatter
        self.to_namedtuple = to_namedtuple

    def _to_object(self, obj):
        """Decodes dictionary to object.

        """
        # Parse values.
        for key, value in obj.items():
            for parser in [_JSONDecoder._to_datetime, _JSONDecoder._to_uuid]:
                if parser(obj, key, value):
                    break

        # Format keys.
        if self.key_formatter is not None:
            obj = dict_keys(obj, self.key_formatter)

        # Return dictionary | named tuple.
        return obj if not self.to_namedtuple else dict_to_namedtuple(obj)

    @staticmethod
    def _to_datetime(obj, attr, value):
        """Attempts to convert a unicode value to a datetime.

        """
        if isinstance(value, unicode) and len(value):
            try:
                float(value)
            except ValueError:
                for date_format in _ISO_DATE_FORMATS:
                    try:
                        value = datetime.datetime.strptime(value, date_format)
                    except (ValueError, TypeError):
                        pass
                    else:
                        obj[attr] = value
                        return True
        return False

    @staticmethod
    def _to_uuid(obj, attr, value):
        """Attempts to convert a unicode value to a UUID.

        """
        if isinstance(value, unicode) and len(value):
            try:
                value = uuid.UUID(value)
            except ValueError:
                pass
            else:
                obj[attr] = value
                return True
        return False


def json_to_dict(representation, key_formatter=None):
    """Converts a json encoded text blob to a dictionary.

    :param unicode representation: A json encoded text blob.
    :param function key_formatter: Dictionary key formatter.

    :returns: A dictionary.
    :rtype: dict

    """
    return _JSONDecoder(key_formatter).decode(representation)


def json_to_namedtuple(representation, key_formatter=None):
    """Converts a json encoded text blob to a namedtuple.

    :param unicode representation: A json encoded text blob.
    :param function key_formatter: Dictionary key formatter.

    :returns: A namedtuple.
    :rtype: namedtuple

    """
    return _JSONDecoder(key_formatter, to_namedtuple=True).decode(representation)


def _convert_file(filepath, convertor, key_formatter=None):
    """Converts a file.

    """
    with open(filepath, 'r') as file_:
        return convertor(file_.read(), key_formatter)


def json_file_to_dict(filepath, key_formatter=None):
    """Converts a json file to a dictionary.

    :param str filepath: A json file path.
    :param function key_formatter: Dictionary key formatter.

    :returns: A dictionary.
    :rtype: dict

    """
    return _convert_file(filepath, json_to_dict, key_formatter)


def json_file_to_namedtuple(filepath, key_formatter=None):
    """Converts a json file to a namedtuple.

    :param str filepath: A json file path.
    :param function key_formatter: Dictionary key formatter.

    :returns: A namedtuple.
    :rtype: namedtuple

    """
    return _convert_file(filepath, json_to_namedtuple, key_formatter)


def dict_to_json(obj, key_formatter=None):
    """Converts a dictionary to json.

    :param dict obj: A dictionary.
    :param function key_formatter: Dictionary key formatter.

    :returns: A json encoded string.
    :rtype: str

    """
    if key_formatter:
        return _JSONEncoder().encode(key_formatter(obj))
    else:
        return _JSONEncoder().encode(obj)


def dict_to_namedtuple(obj, key_formatter=None):
    """Converts a dictionary to a named tuple.

    :param dict obj: A dictionary.
    :param function key_formatter: Dictionary key formatter.

    :returns: A named tuple.
    :rtype: namedtuple

    """
    if key_formatter is not None:
        obj = key_formatter(obj)
    return collections.namedtuple('_Class', obj.keys())(**obj)


def dict_keys(obj, key_formatter=str_to_pascal_case):
    """Returns a dictionary with it's keys formatted accordingly.

    :param dict obj: A dictionary.
    :param function key_formatter: A dictionary key formating function.

    :returns: A dictionary with it's keys formatted accordingly.
    :rtype: dict

    """
    def _convert(value):
        """Converts a dictionary key value."""
        if isinstance(value, dict):
            return dict_keys(value, key_formatter)
        elif isinstance(value, types.ListType):
            return [dict_keys(i, key_formatter) for i in value]
        else:
            return value

    if not isinstance(obj, dict):
        return obj
    else:
        return { k: _convert(v) for k, v in obj.items()}


def dict_keys_to_lower_case(obj):
    """Returns a dictionary with it's keys formatted to lower case.

    :param dict obj: A dictionary.

    :returns: A dictionary with it's keys formatted accordingly.
    :rtype: dict

    """
    return dict_keys(obj, lambda k: k.lower())


def dict_keys_to_upper_case(obj):
    """Returns a dictionary with it's keys formatted to upper case.

    :param dict obj: A dictionary.

    :returns: A dictionary with it's keys formatted accordingly.
    :rtype: dict

    """
    return dict_keys(obj, lambda k: k.upper())


def dict_keys_to_camel_case(obj):
    """Returns a dictionary with it's keys formatted to camel case.

    :param dict obj: A dictionary.

    :returns: A dictionary with it's keys formatted accordingly.
    :rtype: dict

    """
    return dict_keys(obj, str_to_camel_case)


def dict_keys_to_pascal_case(obj):
    """Returns a dictionary with it's keys formatted to pascal case.

    :param dict obj: A dictionary.

    :returns: A dictionary with it's keys formatted accordingly.
    :rtype: dict

    """
    return dict_keys(obj, str_to_pascal_case)


def dict_keys_to_underscore_case(obj):
    """Returns a dictionary with it's keys formatted to underscore case.

    :param dict obj: A dictionary.

    :returns: A dictionary with it's keys formatted accordingly.
    :rtype: dict

    """
    return dict_keys(obj, str_to_underscore_case)


def _jsonify(obj):
    """Converts a dictionary in readiness for json encoding.

    """
    if isinstance(obj, _JSONIFYING_TYPES_IGNORE):
        return obj

    if isinstance(obj, _JSONIFYING_TYPES_UNICODEABLE):
        return unicode(obj)

    if isinstance(obj, collections.Mapping):
        mapped = [(str_to_camel_case(k), _jsonify(obj[k])) for k in obj.keys()]
        mapped = sorted(mapped, key = lambda i: i[0].lower())
        return collections.OrderedDict(mapped)

    if isinstance(obj, collections.Iterable):
        return [_jsonify(i) for i in obj]


def jsonify(data):
    """Converts input dictionary to json.

    :param dict data: Data in dictionary format.

    :returns: JSON encoded string.
    :rtype: str

    """
    return json.dumps(_jsonify(data), indent=4)
