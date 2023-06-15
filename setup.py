import setuptools 

setuptools.setup(
  name='mnzipcode',
  version='0.0.8',
  author='Bekkage',
  description='mnzipcodes is a simple library for querying Mongolian zip codes.',
  package_data={
    'mnzipcode': ['data/*.json']
  },
  long_description_content_type= 'text/markdown',
  long_description="""
mnzipcode is a simple library for querying Mongolian zip codes.

### Installation

mnzipcode is available on PyPi:
```
# python -m pip install mnzipcode
```

Example usage:

```python
>>> import mnzipcode
>>> 
>>> obj = mnzipcode.ZipCode()
>>> 
>>> obj.matching_by_zipcode(11000)
{'name': 'Ulaanbaatar', 'stat': 'province', 'mnname': 'Улаанбаатар', 'year_established': 1942, 'area': 4704.4, 'population': 1539810, 'density': 327}
>>> 
>>> obj.matching_by_name('Дархан-Уул')
[{'name': 'Darkhan-Uul', 'zipcode': '45000', 'stat': 'province', 'mnname': 'Дархан-Уул', 'year_established': 1994, 'area': 3275.0, 'population': 107018, 'density': 33}, {'name': 'Дархан-Уул', 'zipcode': '81041', 'stat': 'bag'}, {'name': 'Дархан-Уул', 'zipcode': '81063', 'stat': 'bag'}]
>>> 
>>> obj.isReal(11000)
True
```

  """,
  package=['mnzipcode']
)