#!/usr/bin/env python3 
import json 
import re

class ZipCode:
  def __init__(self) -> None:
    # LOAD ZIP CODE
    with open('mnzipcode/data/zip.json', 'r') as f: 
      self.zip_codes = json.loads(f.read())

    # LOAD PROVINCE info
    with open('mnzipcode/data/province_info.json', 'r') as f: 
      self.province_info = json.loads(f.read())

  @staticmethod
  def flatten_list(lst):
    result = []
    for item in lst:
      if isinstance(item, dict):
        result.append(item)
      elif isinstance(item, list):
        result.extend(ZipCode.flatten_list(item))
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
            ret_data = {
              'name': item['label'],
              'stat': 'sum'
            }
            if 'дүүрэг' in item['label']:
              ret_data['stat'] = 'duureg'

            return ret_data
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
            ret_data: dict = {
              'name': item['label'],
              'zipcode': item['zipcode'],
              'stat': 'sum'
            }
            if 'дүүрэг' in item['label']:
              ret_data['stat'] = 'duureg'
            results.append(ret_data)
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

    return ZipCode.flatten_list(results)
  
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
    
  #3
  def isReal(self, zipcode: int) -> bool:
    result = self.find_label_by_zipcode(zipcode)

    if result != None:
      return True 
    return False