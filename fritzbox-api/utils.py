from typing import Any, List
import xml.etree.ElementTree as ET
import hashlib

class LoginFailedException(Exception):
  pass

def get_field_from_xml(xml: str, field: str) -> str:
  return ET.fromstring(xml).find(field).text


def build_login_hash(challenge: str, password: str) -> str:
  if password is None:
    raise Exception('Password is None')

  utf16_string = "{}-{}".format(challenge, password).encode('utf-16le')
  hashed_login = hashlib.md5(utf16_string).hexdigest()

  return "{}-{}".format(challenge, hashed_login)


def json_object_to_dict(json: Any, only_keys: List[str] = None) -> dict:
  if only_keys is not None:
    return { key: value for key, value in json.items() if key in only_keys }

  return dict(json)
