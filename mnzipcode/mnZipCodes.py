#!/usr/bin/env python3 
import json 
import re
from os import path

class zipCode:
  def __init__(self) -> None:
    # LOAD ZIP CODE
    with open('mnzipcode/zip.json', 'r') as f: 
      zip_contents = f.read()

    self.zip_codes: dict = json.loads(zip_contents)

    # LOAD PROVINCE info
    with open('mnzipcode/province_info.json', 'r') as f: 
      province_info_contents = f.read()

    self.province_info: dict = json.loads(province_info_contents)

  @staticmethod
  def flatten_list(lst):
    result = []
    for item in lst:
      if isinstance(item, dict):
        result.append(item)
      elif isinstance(item, list):
        result.extend(zipCode.flatten_list(item))
    return result


  def find_label_by_zipcode(self, zipcode: int, items=None) -> list:
    if items==None:
      items = self.zip_codes
    
    for item in items:
      if re.search(str(zipcode), item['zipcode'], re.IGNORECASE):
        if 'sub_items' in item:
          if 'sub_items' in item['sub_items'][0]:
            return {
              'name': item['label'],
              'stat': 'province'
            }
          else:
            return {
              'name': item['label'],
              'stat': 'sum'
            }
        else: 
          return {
              'name': item['label'],
              'stat': 'bag'
            }
      if 'sub_items' in item:
        label = self.find_label_by_zipcode(zipcode, item['sub_items'])
        if label: 
          return label
        
    return None
  
  def find_zipcode_by_name(self, name: str, items=None):
    if items==None:
      items = self.zip_codes

    results: list = []
    for item in items:
      if re.search(name, item['label'], re.IGNORECASE):
        if 'sub_items' in item:
          if 'sub_items' in item['sub_items'][0]:
            results.append( {
              'name': item['label'],
              'zipcode': item['zipcode'],
              'stat': 'province'
            } )
          else:
            results.append( {
              'name': item['label'],
              'zipcode': item['zipcode'],
              'stat': 'sum'
            } )
        else: 
          results.append( {
            'name': item['label'],
            'zipcode': item['zipcode'],
            'stat': 'bag'
          } )
      if 'sub_items' in item: 
        sub_zipcodes = self.find_zipcode_by_name(name, item['sub_items'])
        if sub_zipcodes != []:
          
          results.append(sub_zipcodes)

    return zipCode.flatten_list(results)
  
  def get_province_info(self, province_mn_name: str) -> dict:
    for province in self.province_info:
      if province['mnname'] == province_mn_name:
        return province

  # 1
  def matching_by_zipcode(self, zipcode: int) -> dict:
    result = self.find_label_by_zipcode(zipcode)

    if result!=None:
      if result['stat'] == 'province':
        return {**result, **self.get_province_info(result['name'])}
      else:
        return result
      
  # 2
  def matching_by_name(self, name: str) -> list:
    results = self.find_zipcode_by_name(name)

    ret_data: list = []
    if results != []:
      for result in results:
        if result['stat'] == 'province':
          ret_data.append({**result, **self.get_province_info(result['name'])})
        else:
          ret_data.append(result)

      return ret_data 
  
  def isReal(self, zipcode: int) -> bool:
    result = self.find_label_by_zipcode(zipcode)

    if result != None:
      return True 
    return False