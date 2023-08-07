"""
~~~~~~~~~
mnzipcode
~~~~~~~~~
mnzipcode is a simple library for querying Mongolian zip codes.
@author: bekkage (https://github.com/bekkage)

TODO: SUM INFO
"""

import json  
import bz2 
from os import path 
from sys import version_info


__author__: str = 'Bilguun Ganchuluun'
__email__: str = 'bilguunsec@gmail.com'
__package__: str = 'mnzipcode'
__version__: str = '0.1.24'

VALID_ZIPCODE_LENGTH: int = 5

def get_resource_path(relative_path) -> str:
  try: 
    # for PyInstaller
    from sys import _MEIPASS
    base_path: str = _MEIPASS
  except: 
    base_path: str = path.abspath('.')
  return path.join(base_path, relative_path)

DATA_JSON_PATH: dict = get_resource_path(path.join(path.dirname(path.abspath(__file__)), 'data.json.bz2'))
with bz2.open(DATA_JSON_PATH, 'rb') as f: 
  DATA = json.loads(f.read().decode('utf-8'))

# Functions 
def matching_by_zipcode(zipcode: int, data: dict = DATA['zipcode']) -> dict: 
  for _it in data:
    if _it['zipcode'] == str(zipcode):
      if 'sub_items' in _it: 
        filtered_dict: dict = _it.copy()
        filtered_dict.pop('sub_items', None) 
        return filtered_dict
      else: 
        return _it 
    
    if 'sub_items' in _it: 
      return_data = matching_by_zipcode(zipcode, _it['sub_items'])
      if return_data: 
        return return_data
  return None 

def similar_to(zipcode: int, data: dict = DATA['zipcode']) -> list: 
  similar_data: list = []
  for _it in data:
    if _it['zipcode'].startswith(str(zipcode)):
      if 'sub_items' in _it: 
        filtered_dict: dict = _it.copy()
        filtered_dict.pop('sub_items', None) 
        similar_data.append(filtered_dict)
      else: 
        similar_data.append(_it)
    
    if 'sub_items' in _it: 
      return_data = similar_to(zipcode, _it['sub_items'])
      if return_data: 
        [similar_data.append(_ret_data) for _ret_data in return_data]
  return similar_data 

def filter(data: dict = DATA['zipcode'], **filter_values) -> list:
  filtered_data: list = []
  for _it in data:
    if all([key in _it and _it[key] == value for key, value in filter_values.items()]):
      filtered__it_dict: dict = _it.copy()
      filtered__it_dict.pop('sub_items', None) 
      filtered_data.append(filtered__it_dict)
    
    if 'sub_items' in _it: 
      return_data = filter(data=_it['sub_items'], **filter_values)
      if return_data:
        [filtered_data.append(_ret_data) for _ret_data in return_data]

  return filtered_data
  
def is_real(zipcode: int) -> bool: 
  return bool(matching_by_zipcode(zipcode))